"""Basic Hello World Test"""
import awesome_streamlit as ast


def test_awesome_streamlit_experiments_write_hello_world():
    """Can be used to minimum one test is run in package/tests by
    invoke test.pytest from the root"""
    ast.experiments.hello_world.write()
