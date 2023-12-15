#!/usr/bin/env python3

import functools
import logging
import shutil

from pathlib import Path

from doit import get_var

from probs_runner import (
    probs_convert_data,
    load_datasource,
)


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


def _prep_system_defs_datasource(datasource_path):
    # Copy the systems-definitions output files into a probs-runner datasource folder
    datasource_path.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(Path("system-definitions/_build/probs_rdf/output.ttl"),
                    datasource_path / "system_definitions.ttl")
    (datasource_path / "load_data.rdfox").write_text("import system_defs_datasource/system_definitions.ttl")


def task_build_system_defs_datasource():
    datasource_path = Path("build/system_defs_datasource")
    return {
        "targets": [
            datasource_path / "system_definitions.ttl",
            datasource_path / "load_data.rdfox",
        ],
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
            (_prep_system_defs_datasource, [datasource_path],)
        ],
    }


DATASOURCE_PATHS = [
    Path("build/system_defs_datasource"),
    Path("datasources/UK_wood_data")
]

@log_to_file("build/log_convert_data.txt")
def _convert_data(targets):
    datasources = [load_datasource(p) for p in DATASOURCE_PATHS]
    script_source_dir = get_script_source_dir()
    probs_convert_data(datasources, targets[0], script_source_dir=script_source_dir)


def task_build_rdf():
    return {
        "targets": ["build/data_store.nt.gz"],
        "file_dep": [f for p in DATASOURCE_PATHS for f in p.glob("*")],
        "actions": [
            (_convert_data, [], {}),
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
