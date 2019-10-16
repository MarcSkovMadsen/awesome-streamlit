"""In this module we test the functionality of the utils module"""
import pathlib

import pytest

from awesome_streamlit.testing import utils

from . import test_module_example_folder
from .test_module_example_folder import test_module_example_file


def test_collect_test_modules_without_submodules():
    """Test of collect_tests_in_module"""
    # When
    test_modules = utils.collect_test_sub_modules(test_module_example_file)
    # Then
    assert test_modules == []


def test_collect_test_modules_with_submodules():
    """Test of collect_tests_in_module"""
    # When
    test_modules = utils.collect_test_sub_modules(test_module_example_folder)
    # Then
    assert test_modules == [test_module_example_file]


def test_collect_test_functions_in_module_without_submodules():
    """Test of collect_tests_in_module"""
    # When
    test_functions = utils.collect_test_functions(test_module_example_file)
    # Then
    assert test_functions == [
        (test_module_example_file, "test_st_function_1"),
        (test_module_example_file, "test_st_function_2"),
    ]


def test_collect_test_functions_in_module_with_submodules():
    """Test of collect_tests_in_module"""
    # When
    test_functions = utils.collect_test_functions(test_module_example_folder)
    # Then
    assert test_functions == [
        (test_module_example_file, "test_st_function_1"),
        (test_module_example_file, "test_st_function_2"),
    ]

@pytest.mark.xfail(reason="Not ImplementedError")
def test_load_module_from_path():
    """Test of load_module_from_path"""
    # When
    path = str(pathlib.Path(__file__).parent / "test_module_example_folder")
    module = utils.load_module_from_path(path)
    # Then
    assert module == test_module_example_folder
