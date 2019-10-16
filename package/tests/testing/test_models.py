"""Here we test the models in the testing package"""
from awesome_streamlit.shared.models import Resource
from awesome_streamlit.testing.models import TestResult
from tests.shared.test_models import tag, author, resource
import pytest


@pytest.fixture
def test_result(resource):
    "TestResult fixture"
    return TestResult(
        resource=resource,
        python_code="print('hello world')",
        exception=None,
        traceback=None,
    )


def test__init__(test_result, resource):
    """Test of TestResult__init__"""
    test_result.resource == resource
    test_result.python_code == "print('hello world')"
    test_result.exception == None
    test_result.traceback == None

