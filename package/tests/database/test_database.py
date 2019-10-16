"""Test of the database module"""
from awesome_streamlit.database import AUTHORS, RESOURCES, TAGS


def test_tags():
    """Test TAGS"""
    assert isinstance(TAGS, list)
    assert len(TAGS) > 0


def test_authors():
    """Test AUTHORS"""
    assert isinstance(AUTHORS, list)
    assert len(AUTHORS) > 0


def test_resources():
    """Test RESOURCES"""
    assert isinstance(RESOURCES, list)
    assert len(RESOURCES) > 0
