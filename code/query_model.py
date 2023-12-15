#!/usr/bin/env python3

import logging
log = logging.getLogger("query_model")

from itertools import groupby
from rdflib import Namespace
from probs_runner import PROBS
from probs_models.observations import (
    ProductionObs,
    ImportsObs,
    ExportsObs,
    ProcessInputObs,
    #ProcessOutputObs,
)
from probs_models.models import pactot
from probs_models.system import ObjectType
from probs_models.recipes import Recipe


PROBS_SYS = Namespace("http://ukfires.org/probs/system/")
PROBS_RECIPE = Namespace("https://ukfires.org/probs/ontology/recipe/")
SYS = Namespace("http://ukfires.org/analyses/UK-wood/system/")

# TODO Which is correct?
# QUANTITYKIND = Namespace("http://qudt.org/2.1/vocab/quantitykind#")
QUANTITYKIND = Namespace("http://qudt.org/vocab/quantitykind/")

NAMESPACES = {
    "sys": SYS,
    "probssys": PROBS_SYS,
    "probs": PROBS,
    "recipe": PROBS_RECIPE,
    # "rdf": RDF,
    # "rdfs": RDFS,
    # "prov": Namespace("http://www.w3.org/ns/prov#"),
    # "quantitykind": Namespace("http://qudt.org/2.1/vocab/quantitykind#"),
}


def query_observations(rdfox, model_uri):
    results = rdfox.query_records(
        """
        SELECT ?Observation ?object ?process ?TimePeriod ?Region ?Role ?Metric ?MeasurementValue ?Quality ?Bound
        WHERE {
            ?Observation :hasRole ?Role ;
                         :hasTimePeriod ?TimePeriod ;
                         :hasRegion ?Region ;
                         :bound ?Bound ;
                         :metric ?Metric ;
                         :measurement ?MeasurementValue .
            OPTIONAL { ?Observation :quality ?Quality }
            OPTIONAL { ?Observation :processDefinedBy ?process . ?model :hasProcess ?process .}
            OPTIONAL { ?Observation :objectDefinedBy ?object . ?model :hasObject ?object . }
            FILTER(
               ((?Role IN (:Import, :Export, :SoldProduction, :Consumption)) && BOUND(?object)) ||
               ((?Role IN (:ProcessInput, :ProcessOuptut)) && BOUND(?process) && BOUND(?object))
            )
        }
        ORDER BY ?object ?process ?TimePeriod ?Region ?Role
        """,
        initBindings={
            "model": model_uri,
            "TimePeriod": PROBS["TimePeriod_YearOf2019"],
        },
        initNs=NAMESPACES,
    )

    return results


def _create_observation_object(d):
    """Convert dict of query results to a probs_models Observation object."""

    # objectTypes = []
    # for t in objectType.split("|"):
    #     if t not in obj_dict:
    #         log.error(f'Unknown object type "{objectType}"')
    #         continue
    #     objectTypes.append(t)
    # if not objectTypes:
    #     continue

    # TODO Make it work for spans of multiple object type
    objectTypes = [d["object"]]
    processes = [d["process"]]

    kw = {
        "value": float(d["MeasurementValue"]),
        "quality": d["Quality"] or 1.0,
        "obs_id": d["Observation"],
        "metric": d["Metric"],
    }

    if any(o is None for o in objectTypes):
        raise ValueError("Missing object in observation:\n{}".format(
            "\n".join(f"    {k}: {v}" for k, v in d.items())
        ))

    if d["Role"] == PROBS.SoldProduction:
        return ProductionObs(objectTypes, **kw)
    elif d["Role"] == PROBS.ProcessInput:
        if any(p is None for p in processes):
            raise ValueError("Missing process in observation:\n{}".format(
                "\n".join(f"    {k}: {v}" for k, v in d.items())
            ))
        return ProcessInputObs(objectTypes, processes, **kw)
    elif d['Role'] == PROBS.ProcessOutput:
        raise ValueError(f'Role "{d["Role"]}" has not been implemented yet!')
        #return ProcessOutputObs(objectTypes, processes, **kw)
    elif d["Role"] == PROBS.Import:
        return ImportsObs(objectTypes, **kw)
    elif d["Role"] == PROBS.Export:
        return ExportsObs(objectTypes, **kw)
    else:
        raise ValueError(f'Unknown role "{d["Role"]}"')

    # return pd.DataFrame([
    #     (str(object_name), _strip_sys(process_id) if process_id else "", role_names[role], float(value), quality,
    #      bound_names[bound], str(class_code), str(dataset), comment, is_inferred, obs_id[len(PROBS):])
    #     for obs_id, _, object_name, process_id, _, _, role, value, quality, bound, class_code, dataset, comment, is_inferred
    #     in res
    # ], columns=["ObjectType","Process","ObsType","Value", "Quality", "Bound", "Provenance","Dataset","Comment","IsInferred?","Observation"])


def get_relevant_observations(rdfox, model_uri):
    """Query for relevant observations."""
    results = query_observations(rdfox, model_uri)
    return [_create_observation_object(d) for d in results]                     #this returns a list 


def query_processes(rdfox, model_uri):
    results = rdfox.query_records(
        """
        SELECT ?process ?producesOrConsumes ?recipeObject ?recipeQuantity ?recipeMetric
        WHERE {
            ?model :hasProcess ?process .
            OPTIONAL {
                ?process recipe:hasRecipe ?recipe .
                ?recipe ?producesOrConsumes [ recipe:object ?recipeObject ;
                                              recipe:quantity ?recipeQuantity ;
                                              recipe:metric ?recipeMetric ] .
                FILTER( ?producesOrConsumes = :produces || ?producesOrConsumes = :consumes )
            }
        }
        ORDER BY ?process
        """,
        initBindings={"model": model_uri},
        initNs=NAMESPACES,
    )

    def _group_to_recipe_list(v, producesOrConsumes):
        items = [
            {
                "object": item["recipeObject"],
                "quantity": item["recipeQuantity"],
                "metric": item["recipeMetric"],
            }
            for item in v
            if item["producesOrConsumes"] == producesOrConsumes
        ]
        if items and any(v is not None for v in items[0].values()):
            return items
        return []

    # Do this in two stages so we can use the generator twice
    grouped = [(k, list(v)) for k, v in groupby(results, lambda d: d["process"])]
    return [
        (
            k,
            _group_to_recipe_list(v, PROBS["produces"]),
            _group_to_recipe_list(v, PROBS["consumes"]),
        )
        for k, v in grouped
    ]


class LinearRecipe(Recipe):
    """A Recipe with a fixed, linear set of inputs and outputs."""

    own_params = []

    def __init__(self, process_uri, input_tuples, output_tuples, should_balance=None):
        if not (input_tuples or output_tuples):
            raise ValueError(f"Process {process_uri} has no inputs nor outputs")
        self._process_uri = process_uri
        self.input_tuples = input_tuples
        self.output_tuples = output_tuples

        if should_balance is None:
            # by default, if sink or source, should not balance
            should_balance = bool(input_tuples and output_tuples)

            # don't add a constraint if everything is measured in kg already
            inputs_in_kg = (unit == "kg" for _, unit, _ in input_tuples)
            outputs_in_kg = (unit == "kg" for _, unit, _ in output_tuples)
            if should_balance and all(inputs_in_kg) and all(outputs_in_kg):
                log.debug("Skipping should_balance for %s because all inputs/outputs are in kg already",
                          process_uri)
                should_balance = False
        self.should_balance = should_balance

        if output_tuples:
            # Find biggest output value -> set main_output to its name. This is
            # used later to determine the scaling of the supply and use matrices
            # so it's important.
            idx = max(range(len(output_tuples)), key=lambda i: output_tuples[i][2])
            self.main_output = output_tuples[idx][0]
        elif input_tuples:
            idx = max(range(len(input_tuples)), key=lambda i: input_tuples[i][2])
            self.main_input = input_tuples[idx][0]

    @property
    def process_uri(self):
        return self._process_uri

    def recipe(self, _):
        return self.input_tuples, self.output_tuples

    def __repr__(self):
        return f"<LinearRecipe for {self.process_uri}>"


RECIPE_METRIC_UNITS = {
    QUANTITYKIND.Mass: "kg",
    QUANTITYKIND.Area: "m2",
    QUANTITYKIND.Volume: "m3",
    QUANTITYKIND.NumberOfItems: "NumberOfItems",
    QUANTITYKIND.GreenMass: "GreenMass",
    QUANTITYKIND.Dimensionless: "-",
}


def _recipe_items_to_tuples(items):
    for x in items:
        if x["metric"] not in RECIPE_METRIC_UNITS:
            raise ValueError(f"unsupported metric {x['metric']} in recipe")
        assert x["quantity"] is not None, "missing value"

    tuples = [
        (x["object"], RECIPE_METRIC_UNITS[x["metric"]], float(x["quantity"]))
        for x in items
    ]
    return tuples


def _create_recipe_object(item):
    """Define a recipe for process_uri."""
    k, produces, consumes = item
    input_tuples = _recipe_items_to_tuples(consumes)
    output_tuples = _recipe_items_to_tuples(produces)
    return LinearRecipe(k, input_tuples, output_tuples)


def test_value(param):
    "Return a suitable test value for the parameter"
    name, unit, description, comment, dist_type, dist_values = param
    # XXX only Uniform for now...
    assert dist_type == "Uniform" and len(dist_values) == 2
    a, b = dist_values
    return (a + b) / 2


def validate_recipes(object_types, defined_recipes):
    """Validate the recipes -- does everything included in the recipes correspond
    to a known object?"""
    obj_dict = {obj.name: obj for obj in object_types}
    for r in defined_recipes:
        recipe_name = r.process_uri
        test_params = {k[0]: test_value(k) for k in getattr(r, "own_params", [])}
        inputs, outputs = r.recipe(test_params)
        for k, unit, value in inputs + outputs:
            if k not in obj_dict:
                raise ValueError(f'Unknown object "{k}" in recipe for "{recipe_name}"')
            if not value >= 0:
                raise ValueError(
                    f'Expect value for "{k}" in recipe for "{recipe_name}" to be positive'
                )


def get_recipe_builders(rdfox, model_uri, object_types):
    """Query for relevant observations."""
    results = query_processes(rdfox, model_uri)
    recipe_builders = [_create_recipe_object(d) for d in results]
    validate_recipes(object_types, recipe_builders)
    return recipe_builders


def query_object_types(rdfox, model_uri):
    results = rdfox.query_records(
        """
        SELECT ?object ?units ?scale ?isTraded
        WHERE {
            ?model :hasObject ?object . 
            OPTIONAL { ?object :objectUnits ?units . }
            OPTIONAL { ?object :objectScale ?scale . }
            OPTIONAL { ?object :objectIsTraded ?isTraded . }
        }
        ORDER BY ?object
        """,
        initBindings={"model": model_uri},
        initNs=NAMESPACES,
    )

    return results


def _create_object_type_object(item):
    """Define an object type for query results data."""
    return ObjectType(
        name=item["object"],
        unit=item["units"] or "kg", 
        scale=item["scale"] or 1e9,
        is_traded=item["isTraded"] or False,
    )


def get_object_types(rdfox, model_uri):
    """Query for model object types."""
    results = query_object_types(rdfox, model_uri)
    return [_create_object_type_object(d) for d in results]


def adjust_obs_scaling(observations, object_types):
    obj_dict = {obj.name: obj for obj in object_types}
    for obs in observations:
        # Sort out scaling
        scales = [obj_dict[t].scale for t in obs.objects]
        if not all(s == scales[0] for s in scales):
            raise ValueError("Model cannot deal with summing differently scaled variables")
        obs.params["value"] /= scales[0]


def query_model_from_endpoint(rdfox, model_uri):
    """Query to find object types, recipe builders and observations."""

    log.info("Loading object types...")
    object_types = get_object_types(rdfox, model_uri)

    log.info("Loading recipes...")
    recipe_builders = get_recipe_builders(rdfox, model_uri, object_types)

    log.info("Loading observations from RDF...")
    obs = get_relevant_observations(rdfox, model_uri)           # [_create_observation_object(d) for d in results] = obs which means that obs is a list 

    # XXX this should probably happen within build_model
    adjust_obs_scaling(obs, object_types)

    if not obs:
        log.error("No observations found!")

    return object_types, recipe_builders, obs
