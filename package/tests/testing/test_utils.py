"""In this module we test the functionality of the utils module"""
from awesome_streamlit.testing import utils
from . import test_module


def test_collect_tests_in_module():
    """Test of collect_tests_in_module"""
    # When
    tests = utils.collect_tests_in_module(test_module)
    # Then
    assert tests == [test_module.test_st_function_1]
