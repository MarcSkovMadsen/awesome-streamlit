"""Test of the models"""
import pytest

from awesome_streamlit.shared.models import Author, Resource, Tag


@pytest.fixture
def tag() -> Tag:
    """Tag fixture"""
    return Tag(name="new tag")


@pytest.fixture
def author() -> Author:
    """Author fixture"""
    return Author(name="Marc Skov Madsen", url="https://awesome-streamlit.org")


@pytest.fixture
def resource(author, tag) -> Resource:
    """Resource fixture"""
    return Resource(
        name="awesome-streamlit.org",
        url="https://awesome-streamlit.org",
        is_awesome=True,
        tags=[tag],
        author=author,
    )


def test_tag__init__(tag):
    """Test Tag __init__"""
    assert tag.name == "new tag"


def test_tag__str__(tag):
    """Test Tag __str__"""
    assert str(tag) == "new tag"


def test_author__init__(author):
    """Test Author __init__"""
    assert author.name == "Marc Skov Madsen"
    assert author.url == "https://awesome-streamlit.org"


def test_author__str__(author):
    """Test Author __str__"""
    assert str(author) == "Marc Skov Madsen"


def test_resource__init__(resource, author, tag):
    """Test Resource __init__"""
    assert resource.name == "awesome-streamlit.org"
    assert resource.url == "https://awesome-streamlit.org"
    assert resource.is_awesome
    assert resource.tags == [tag]
    assert resource.author == author


def test_resource__str__(resource):
    assert str(resource) == resource.name


def test_resource_to_markdown_bullet(resource):
    """I can convert a resource to a a markdown bullet string"""
    assert resource.to_markdown_bullet() == (
        "- [awesome-streamlit.org](https://awesome-streamlit.org) by "
        "[Marc Skov Madsen](https://awesome-streamlit.org) (#new tag)"
    )


def test_screenshot_file(resource):
    # When:
    resource.name = "Hello-streamlit deployed on Glitch"
    # Then:
    assert resource.screenshot_file == "hello-streamlit-deployed-on-glitch.png"
