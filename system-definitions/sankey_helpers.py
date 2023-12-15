"""Helper functions for drawing Sankey diagrams from the modelled data."""
from io import StringIO
from floweaver.partition import Partition
from floweaver import (
    ProcessGroup, Bundle, Waypoint, Elsewhere, weave, QuantitativeScale,
    CategoricalScale
)
import attr
import pandas as pd
from pathlib import Path
import logging
from rdflib import URIRef, Namespace, Literal
from IPython.display import Image
from uuid import uuid4
from itertools import groupby


from semantic_sankeys.resolver import resolve_sankey_elements
from semantic_sankeys.util import RDFoxFacts, NAMESPACES, PROBS, add_triples
from semantic_sankeys.sankey_elements import (
    SankeyElements,
    SankeyProcess,
    SankeyObject,
    validate_elements
)
from semantic_sankeys.build_sdd import build_sdd, ProcessGroupExtra
from semantic_sankeys.graphviz_graph import sdd_ordering, sdd_to_graph
from semantic_sankeys.guesser import guess_sankey_elements_within


HERE = Path(__file__).parent

SYSTEM_RDF_FILENAME = HERE / "../build/probs_enhanced_data.nt.gz"
FLOWS_FILENAME = HERE / "../build/flows.csv"
MODEL_URI = URIRef("http://ukfires.org/analyses/UK-wood/model/Model")

PORT = 12116

def load_flows(filename):
    flows = pd.read_csv(filename)
    flows["is_trade"] = False
    flows.loc[flows["source"].str.startswith("imports "), "is_trade"] = True
    flows.loc[flows["target"].str.startswith("exports "), "is_trade"] = True
    # flows["source"] = [URIRef(x) for x in flows["source"]]
    # flows["target"] = [URIRef(x) for x in flows["target"]]
    return flows


def get_leaf_nodes(rdfox, model_uri):
    """Identify leaf nodes (processes and objects) from the model definition."""

    result = rdfox.query_records("""
    SELECT ?leaf WHERE {
        { ?model probs:hasProcess ?leaf }
        UNION
        { ?model probs:hasObject ?leaf }
    }
    """, initBindings={"model": model_uri})

    leaf_uris = {row["leaf"] for row in result}
    return leaf_uris


def guess_elements(process, levels=1, include_objects=None, resolve=False):
    with open(SYSTEM_RDF_FILENAME, "rb") as f:
        with RDFoxFacts(f, port=PORT, namespaces=NAMESPACES) as rdfox:
            elements = guess_sankey_elements_within(rdfox, process, levels, include_objects)
            if resolve:
                dataset_leaves = get_leaf_nodes(rdfox, MODEL_URI)
                resolve_sankey_elements(rdfox, elements, dataset_leaves)
    return elements


def elements_to_code(elements, sys_prefix, insert_cell=False):
    """Convert Sankey elements to Python code.

    If `insert_cell` is True, and we are in an IPython session, insert the code
    as a new code cell.

    """
    code = _elements_to_code(elements, sys_prefix)
    # code = f"# Guessed as {spec_type.__name__} of {parent_id}\n" + code

    if insert_cell:
        try:
            from IPython import get_ipython
            shell = get_ipython()
            shell.set_next_input(code)
            return None
        except:
            pass

    return code


def resolve_elements(elements):
    #dataset_leaves = get_leaf_nodes(rdfox, MODEL_URI)            
    with open(SYSTEM_RDF_FILENAME, "rb") as f:
        with RDFoxFacts(f, port=PORT, namespaces=NAMESPACES) as rdfox:
            dataset_leaves = get_leaf_nodes(rdfox, MODEL_URI)
            resolve_sankey_elements(rdfox, elements, dataset_leaves)
    return elements


TEMP = Namespace("http://temp/")

def create_object_partition(endpoint, name, palette):
    """Create an object representing a partition in RDF, so that we can run
    queries against it in combination with the rules for leafObjects etc.

    `palette` should be a dictionary mapping URIs of Objects to colours.

    """
    n = TEMP[name]
    for k, color in palette.items():
        item = URIRef(TEMP[uuid4()])
        add_triples(
            endpoint,
            [
                (item, PROBS.objectType, k),
                (item, PROBS.color, Literal(color)),
                (n, PROBS.hasItem, item),
            ],
        )
    return n


def get_partition(g, name):
    res = g.query(
        """
    SELECT ?groupIRI ?leaf ?label
    WHERE {
        ?partition probs:hasItem ?item .
        ?item probs:objectType ?groupIRI .
        ?groupIRI probs:leafObject ?leaf .
    }
    ORDER BY ?groupIRI
    """,
        initBindings={"partition": name},
    )
    return [
        (k, [str(row["leaf"]) for row in group])
        for k, group in groupby(res, lambda row: row["groupIRI"])
    ]


def show_elements(elements, solution=None, sample= None, show_solution_variation=False, object_type_palette=None, **kwargs):
    """
    Parameters:

    ...

    sample: if a sample number is specified, show only results for that Monte Carlo based on the "sample" column in the data file.
    """
    dataset = load_flows(FLOWS_FILENAME)
    validate_elements(elements)
    sdd = build_sdd(elements)
    sdd = sdd_ordering(sdd)

    # Work out the partition to use for material types

    if solution is not None:
        if isinstance(solution, int):
            solution = dataset.solution.unique().tolist()[solution]
        flows = dataset.query("solution == '10'")

    if object_type_palette is not None:
        with open(SYSTEM_RDF_FILENAME, "rb") as f:
            with RDFoxFacts(f, port=PORT, namespaces=NAMESPACES) as rdfox:
                n = create_object_partition(
                    rdfox, "ObjectPartition-%s" % uuid4(), object_type_palette
                )
                flow_partition = Partition.Simple("material", get_partition(rdfox.graph, n))
        sdd = attr.evolve(sdd, flow_partition=flow_partition)
        link_color = CategoricalScale(
            "type",
            # Need to convert rdflib.URIRef to string for floweaver
            {str(k): v for k, v in object_type_palette.items()},
            default="#888"
        )
    else:
        link_color = None



    if sample is not None: 
        dataset = dataset.query("sample == @sample")

        result = weave(sdd, flows, link_color=link_color)

    elif show_solution_variation:
        grouped = (
            dataset.groupby(["source", "target", "material"], as_index=False)["value"]
            .agg({"value": "mean", "std": "std"})
        )
        grouped["is_trade"] = False
        grouped.loc[grouped["source"].str.startswith("imports "), "is_trade"] = True
        grouped.loc[grouped["target"].str.startswith("exports "), "is_trade"] = True
        result = weave(
            sdd,
            grouped,
            #link_color=QuantitativeScale("std", intensity="value", domain=(0,1)),
            link_color=QuantitativeScale("std", domain=(0, 4e9 * 0.5)),
            link_width="value",
            measures=["value", "std"]
        )
    else:
        flows = dataset.query("solution == 'Only solution found'")
        result = weave(sdd, flows, link_color=link_color)

    kwargs.setdefault("height", 300)
    return result.to_widget(debugging=True, **kwargs)


def resolve_and_show_elements(elements, **kwargs):
    resolve_elements(elements)
    return show_elements(elements, **kwargs)


def guess_and_show(process, levels=1, include_objects=None, **kwargs):
    elements = guess_elements(process, levels, include_objects, resolve=True)
    return show_elements(elements, **kwargs)


def show_skeleton(process, levels=1, include_objects=None, ports_at_ends=False):
    elements = guess_elements(process, levels, include_objects, resolve=True)
    sdd = build_sdd(elements, port_titles=True)
    G = sdd_to_graph(sdd, ports_at_ends)
    G.layout(prog="dot")
    data = G.draw(format="png", prog="dot")
    return Image(data)


def _elements_to_code(elements, sys_prefix):
    lines = []
    lines = [
        "SankeyElements(",
        "    processes=[",
    ]
    for p in elements.processes:
        lines.append("        " + _process_to_code(p, sys_prefix) + ",")
    lines += [
        "    ],",
        "    objects=[",
    ]
    for obj in elements.objects:
        lines.append("        " + _object_to_code(obj, sys_prefix) + ",")
    lines += [
        "    ],",
        ")"
    ]
    return "\n".join(lines)


def _process_to_code(p, sys_prefix):
    x = []
    uri = p.process
    if uri.startswith(sys_prefix):
        uri = "SYS." + uri[len(sys_prefix):]
    x.append(uri)
    if p.label is not None:
        x.append(f"label={p.label!r}")
    if p.include_objects != set():
        x.append(f"include_objects={p.include_objects!r}")
    return "SankeyProcess(" + ", ".join(x) + ")"


def _object_to_code(p, sys_prefix):
    x = []
    uri = p.object
    if uri.startswith(sys_prefix):
        uri = "SYS." + uri[len(sys_prefix):]
    x.append(uri)
    if p.label is not None:
        x.append(f"label={p.label!r}")
    if p.input_port is not None:
        x.append(f"input_port={p.input_port!r}")
    if p.output_port is not None:
        x.append(f"output_port={p.output_port!r}")
    if p.produced_via:
        x.append(f"produced_via={p.produced_via!r}")
    if p.consumed_via:
        x.append(f"consumed_via={p.consumed_via!r}")
    return "SankeyObject(" + ", ".join(x) + ")"
