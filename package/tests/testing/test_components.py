from awesome_streamlit.testing import components
from awesome_streamlit.testing.models import TesTItem


def test_st_intro_section():
    """Test of the intro_section"""
    # When
    components.intro_section()
    # Then:
    # raise NotImplementedError as we cannot yet test this


def test_st_test_collection_section():
    """Test of the test_collection_section"""
    # Given
    test_items = [TesTItem(name="Test 1", location="url")]

    def test_items_collector():
        return test_items

    # Then
    actual = components.test_collection_section(
        test_items_collector=test_items_collector
    )
    assert actual == test_items
