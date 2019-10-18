"""Module of tasks for running sphinx"""
import logging
import pathlib
import shutil

from invoke import task

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

ROOT = pathlib.Path(__file__).parent.parent
ROOT_FILES = [
    "README.md",
    "AWESOME-STREAMLIT.md",
    "code-of-conduct.md",
    "contributing.md",
]


@task
def copy_from_project_root(command):  # pylint: disable=unused-argument
    """We need to copy files like README.md into docs/_copy_of_project_root
    for inclusion in the Docs"""
    target = ROOT / "docs/_copy_of_project_root"
    target.mkdir(parents=True, exist_ok=True)
    for file in ROOT_FILES:
        root_file = ROOT / file
        if root_file.exists():
            target_file = target / file
            shutil.copy(root_file, target_file)
            logging.info("Successfully copied %s to %s", root_file, target_file)
        else:
            logging.error("Error. Could not find %s!", root_file)

    from distutils.dir_util import copy_tree

    root_assets = ROOT / "assets"
    target_assets = target / "assets"
    copy_tree(str(root_assets), str(target_assets))
    logging.info("Successfully copied %s to %s", root_assets, target_assets)


@task(pre=[copy_from_project_root])
def build(command):
    """Build local version of site and open in a browser

    The generated documentation can be found in the source/_build folder
    """
    with command.cd("docs"):
        command.run("sphinx-build -b html . _build")
        command.run("start _build/index.html")


@task(pre=[copy_from_project_root])
def livereload(command):
    """Start autobild documentation server and open in browser.

    The documentation server will automatically rebuild the documentation and
    refresh your browser when you update it.
    """
    with command.cd("docs"):
        command.run("sphinx-autobuild . _build/html --open-browser --port 8003")


@task(pre=[build])
def test(command):
    """Checks for broken internal and external links and
    runs the doc8 .rst linter to identify problems.

    Runs
    - the Sphinx 'dummy' builder to identify internal problems.
    - the Sphinx 'linkcheck' build to identify broken external links.
    - doc8 linter to identify .rst syntax errors
    """
    with command.cd("docs"):
        logging.info("\nRunning the 'dummy' builder")
        logging.info(
            """The input is only parsed and checked for consistency.
This is useful for linting purposes."""
        )
        command.run("sphinx-build . _build/ -b dummy", echo=True, warn=True)

        logging.info("\nRunning the 'linkcheck' builder")
        logging.info(
            "echo This builder scans all documents for external links and "
            "tries to open them with requests"
        )
        command.run("sphinx-build . _build/ -b linkcheck", echo=True, warn=True)

        logging.info("\nRunning the 'doc8' linter to identify .rst syntax errors")
        command.run("doc8 .", echo=True, warn=True)
