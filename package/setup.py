"""Setup.py file for the trading_analytics Python package. The package can be installed by running

pip install -e .

or similar where . is replaced by the path to package root
"""
from setuptools import setup, find_packages
import os

THIS_FILE_PATH = os.path.dirname(__file__)
with open(f"{THIS_FILE_PATH}/README.md") as f:
    README = f.read()

s = setup(
    name="awesome-streamlit",
    version="20191014.1",
    license="MIT",
    description=README,
    url="https://github.com/marcskovmadsen/awesome-streamlit",
    packages=find_packages("awesome_streamlit"),
    install_requires=["streamlit>=0.47.4"],
    python_requires=">= 3.7",
    author="Marc Skov Madsen",
    author_email="marc.skov.madsen@gmail.com",
)
