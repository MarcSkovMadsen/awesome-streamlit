"""Setup.py file for the trading_analytics Python package. The package can be installed by running

pip install -e .

or similar where . is replaced by the path to package root
"""
import pathlib

from setuptools import setup

README_FILE_PATH = pathlib.Path(__file__).parent / "README.md"
with open(README_FILE_PATH) as f:
    README = f.read()

s = setup(  # pylint: disable=invalid-name
    name="awesome-streamlit",
    version="20191018.1",
    license="MIT",
    description="""This package supports the Awesome Streamlit Project and
    provides highly experimental features!""",
    long_description_content_type="text/markdown",
    long_description=README,
    url="https://github.com/marcskovmadsen/awesome-streamlit",
    author="Marc Skov Madsen",
    author_email="marc.skov.madsen@gmail.com",
    packages=["awesome_streamlit"],
    install_requires=["streamlit>=0.47.4"],
    python_requires=">= 3.7",
    zip_safe=False,
)
