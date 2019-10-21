"""Test of components module"""

import awesome_streamlit.experiments.hello_world as test_page
# pylint: disable=protected-access
from awesome_streamlit.shared import components


def test__reload_module():
    """Test that we can _reload_module without an error"""
    components._reload_module(test_page)


def test_st_write_page():  # pylint: disable=redefined-outer-name
    """Test that we can write hello world to the page"""
    # When
    components.write_page(test_page)
    # Then: 'hello world' should be written to the page
    # raise NotImplementedError


def test_st_video_youtube():
    """Test that the video component can show the youtube video specified"""
    # When:
    components.video_youtube(src="https://www.youtube.com/embed/B2iAodr0fOo")
    # Then: Then the youtube video should be shown
    # raise NotImplementedError


def test_st_multiselect():
    """Tests the multiselect extension"""
    # Given:
    class Option:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name

    label = "Test"
    options = [Option("option 1"), Option("option 2")]
    default = [options[0]]
    # When:
    selections = components.multiselect(  # pylint: disable=unused-variable
        label=label, options=options, default=default
    )
    # Then: the user should be able to use the multiselect and
    # get the selections back as a list of objects
    # raise NotImplementedError


def test_st_title_awesome():
    """Test the title_awesome component"""
    # When
    components.title_awesome("Gallery")
    # Then the title should be written in Markdown
    # with the text 'Awesome Streamlet Gallery' and the Awesome badge on the right
    # raise NotImplementedError


def test_st_write_svg():
    """Test the write_svg component"""
    # Given
    svg = """
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
<circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
</svg>
"""
    # When
    components.write_svg(svg=svg)
    # Then
    # raise notImplementedError because we annot yet test the result
