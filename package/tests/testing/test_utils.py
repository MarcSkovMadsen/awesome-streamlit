"""In this module we test the functionality of the utils module"""
from awesome_streamlit.testing import utils
from . import test_module_example


def test_collect_tests_in_module():
    """Test of collect_tests_in_module"""
    # When
    test_functions = utils.collect_tests_in_module(test_module_example)
    # Then
    assert test_functions == [
        (test_module_example, "test_st_function_1"),
        (test_module_example, "test_st_function_2"),
    ]
