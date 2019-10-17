"""Module of tasks for running sphinx"""
from invoke import task
import logging


@task
def build(command):
    """Build local version of site and open in a browser

    The generated documentation can be found in the source/_build folder
    """
    with command.cd("docs"):
        command.run("sphinx-build -b html . _build")
        command.run("start _build/index.html")


@task()
def livereload(command):
    """Start autobild documentation server and open in browser.

    The documentation server will automatically rebuild the documentation and refresh your browser when you update it.
    """
    with command.cd("docs"):
        command.run("sphinx-autobuild . _build/html --open-browser --port 8003")


@task(pre=[build])
def test(command):
    """Checks for broken internal and external links and runs the doc8 .rst linter to identify problems.

    Runs
    - the Sphinx 'dummy' builder to identify internal problems.
    - the Sphinx 'linkcheck' build to identify broken external links.
    - doc8 linter to identify .rst syntax errors
    """
    with command.cd("docs"):
        logging.info("\nRunning the 'dummy' builder")
        logging.info(
            "The input is only parsed and checked for consistency. This is useful for linting purposes."
        )
        command.run("sphinx-build . _build/ -b dummy", echo=True, warn=True)

        logging.info("\nRunning the 'linkcheck' builder")
        logging.info(
            "echo This builder scans all documents for external links, tries to open them with requests"
        )
        command.run("sphinx-build . _build/ -b linkcheck", echo=True, warn=True)

        logging.info("\nRunning the 'doc8' linter to identify .rst syntax errors")
        command.run("doc8 .", echo=True, warn=True)
