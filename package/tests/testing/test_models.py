"""Here we test the models in the testing package"""
import pytest

# pylint: disable=redefined-outer-name
from awesome_streamlit.shared.models import Author, Resource, Tag
from awesome_streamlit.testing.models import TesTItem
from tests.testing.test_module_example_folder import test_module_example_file


@pytest.fixture
def tag() -> Tag:
    """Tag fixture"""
    return Tag(name="App")


@pytest.fixture
def author() -> Author:
    """Author fixture"""
    return Author(name="Marc Skov Madsen", url="https://datamodelsanalytics.com")


@pytest.fixture
def resource(author, tag) -> Resource:
    """Resource fixture"""

    return Resource(
        name="Sentiment Algorithm",
        url="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/gallery/sentiment_analyzer/sentiment_analyzer.py",
        is_awesome=True,
        tags=[tag],
        author=author,
    )


@pytest.fixture
def test_item():
    "TesTItem fixture"
    return TesTItem(name="Test Item", location="url")


def test__init__(test_item):
    """Test of TesTItem.__init__"""
    assert test_item.name == "Test Item"
    assert test_item.location == "url"


def test_create_from_app_file_resource(resource):
    """Test of TesTItem.create_from_resource"""
    # When
    test_item = TesTItem.create_from_app_file_resource(resource)

    # Then
    assert test_item.name == resource.name
    assert test_item.location == resource.url
    assert not test_item.python_code


def test_create_from_test_function():
    # Given: A module and test function
    # When
    test_item = TesTItem.create_from_test_function(
        test_module_example_file, "test_st_function_1"
    )
    # Then
    assert test_item.name == "test_st_function_1"
    assert (
        test_item.location
        == """tests.testing.test_module_example_folder.test_module_example_file::test_st_function_1"""
    )
    assert test_item.test_function == getattr(
        test_module_example_file, "test_st_function_1"
    )
    assert not test_item.python_code
