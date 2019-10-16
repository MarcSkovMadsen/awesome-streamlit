"""Module of Invoke tasks regarding the `package. To be invoked from the command line. Try

invoke --list

from the command line for a list of all available commands.
"""

from invoke import task


@task
def build(command):
    """Builds the awesome-streamlit package)"""
    with command.cd("package"):
        command.run("python setup.py sdist bdist_wheel")
