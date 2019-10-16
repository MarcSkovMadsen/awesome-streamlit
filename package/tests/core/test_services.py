"""In this module we test the services"""
from awesome_streamlit.core import services


def test_get_file_content_as_string():
    """Test we can get_file_content_as_string"""
    # Given
    url = "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/license.md"
    # When
    result = services.get_file_content_as_string(url)
    # Then
    assert result.startswith("# Attribution-ShareAlike 4.0 International")
