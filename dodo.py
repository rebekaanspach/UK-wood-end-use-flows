#!/usr/bin/env python3

import time
import sys
import functools
import logging
import urllib.parse

from pathlib import Path
from doit import get_var

from rdflib import Namespace, Graph, BNode, Literal, URIRef

from probs_runner import (
    probs_enhance_data,
    probs_endpoint,
)
from probs_runner.runners import NAMESPACES


sys.path.insert(0, "code")
import solve_model


DOIT_CONFIG = {'default_tasks': ['solve_model']}


def log_to_file(output_file):
    """Decorator to log to specified file while running function."""
    def decorator_log_to_file(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = logging.getLogger('')
            logger.setLevel(logging.DEBUG)
            Path(output_file).parent.mkdir(parents=True, exist_ok=True)
            fh = logging.FileHandler(output_file)
            fh.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            logger.addHandler(fh)
            logger.info("=" * 40)
            logger.info("Starting doit run")
            logger.info("=" * 40)
            result = func(*args, **kwargs)
            logger.removeHandler(fh)
            return result
        return wrapper
    return decorator_log_to_file


def setup_logging_to_console():
    """Log WARNING messages from all loggers to stderr."""
    console = logging.StreamHandler()
    console.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)


setup_logging_to_console()


def get_script_source_dir():
    source_dir = get_var("script_source_dir")
    if source_dir is None:
        raise RuntimeError("Argument script_source_dir is required")
    source_dir = Path(source_dir)
    if not source_dir.exists():
        raise RuntimeError("script_source_dir does not exist")
    return source_dir


def task_extract_rdf():
    return {
        "targets": ["system-definitions/_build/probs_rdf/output.ttl"],
        "file_dep": list(Path("system-definitions").glob("*.md")),
        "actions": [
            # Clean is needed for now at least, since Sphinx extension is not
            # properly responding to things being removed and caches them too
            # aggressively.
            #
            # Also when using jupyter-cache to avoid rerunning every notebook
            # every time, the cache needs to be cleared when the rdf output
            # changes (the --all option does this).
            "jupyter-book clean --all system-definitions",
            (
                "jupyter-book build system-definitions -v --builder=custom --custom-builder=probs_rdf "
                "--config system-definitions/_config_extract_rdf.yml"
            ),
        ],
    }


@log_to_file("build/log_enhance_data.txt")
def _enhance_data(dependencies, targets):
    script_source_dir = get_script_source_dir()
    probs_enhance_data(dependencies, targets[0], script_source_dir=script_source_dir)


@log_to_file("build/log_solve_model.txt")
def _solve_model(dependencies, targets):
    script_source_dir = get_script_source_dir()
    solve_model.solve_model_mc(dependencies[0], targets[0], script_source_dir, num_samples=1)


def task_enhance_data():
    return {
        "targets": ["build/probs_enhanced_data.nt.gz"],
        "file_dep": [
            "example_data_store/build/data_store.nt.gz",
            "model/model_definition.ttl",
            "model/extra_observations.ttl",
            "system-definitions/_build/probs_rdf/output.ttl",
        ],
        "actions": [
            (_enhance_data, [], {}),
        ],
    }


def task_solve_model():
    return {
        "targets": ["build/flows.csv"],
        "file_dep": [
            "build/probs_enhanced_data.nt.gz",
        ],
        "actions": [
            (_solve_model, [], {}),
        ],
    }


def task_build_docs():
    return {
        "targets": ["system-definitions/_build/html/index.html"],
        "file_dep": (
            list(Path("system-definitions").glob("*.md")) +
            list(Path("system-definitions").glob("*.yml"))
        ),
        "actions": [
            "jupyter-book build system-definitions -v"
        ],
    }


# Define a useful starting point for a test query

DEFAULT_QUERY = """
SELECT ?Observation ?p ?o
WHERE {
    ?Observation a :Observation; ?p ?o .
}
ORDER BY ?Observation ?p ?o
"""


def _rdfox_endpoint(dependencies):
    # Define some useful prefixes and a test query
    prefixes = [
        f"PREFIX {p}: <{v}>"
        for p, v in NAMESPACES.items()
    ]
    content = "\n".join(prefixes) + "\n" + DEFAULT_QUERY
    query = urllib.parse.quote(content)

    script_source_dir = get_script_source_dir()
    with probs_endpoint(dependencies[0], script_source_dir=script_source_dir) as rdfox:
        print("Started endpoint")
        print(f"Open {rdfox.server}/console/default?query={query} in your browser.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping endpoint")


def task_rdfox_endpoint():
    """Start a RDFox endpoint to query the data"""
    return {
        "file_dep": ["build/probs_enhanced_data.nt.gz"],
        "uptodate": [False],
        "actions": [_rdfox_endpoint],
    }
