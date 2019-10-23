"""In this module we test the services"""
import urllib.request

import pytest

from awesome_streamlit.core import services


def test_get_file_content_as_string():
    """Test we can get_file_content_as_string"""
    # Given
    url = "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/license.md"
    # When
    result = services.get_file_content_as_string(url)
    # Then
    assert result.startswith("# Attribution-ShareAlike 4.0 International")


def test_get_file_content_as_string_httperror():
    """Test that filename is included in HTTPError description"""
    # Given
    url = (
        "https://raw.githubusercontent.com/MarcSkovMadsen/this_file_does_not_exists.md"
    )
    # When/ Then
    with pytest.raises(urllib.error.HTTPError) as exception:
        result = services.get_file_content_as_string(url)
    assert str(exception.value) == "HTTP Error 400: Bad Request: " + url
