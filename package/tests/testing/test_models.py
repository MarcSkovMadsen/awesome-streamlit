"""Here we test the models in the testing package"""
# pylint: disable=redefined-outer-name
from awesome_streamlit.shared.models import Resource
from awesome_streamlit.testing.models import TestItem
from tests.shared.test_models import tag, author, resource
import pytest


@pytest.fixture
def test_item():
    "TestItem fixture"
    return TestItem(name="Test Item", location="url")


def test__init__(test_item):
    """Test of TestItem__init__"""
    assert test_item.name == "Test Item"
    assert test_item.location == "url"

