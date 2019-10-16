"""Test of components module"""

"""Components for the Awesome Streamlit App and other use cases

Hopefully a lot of the components  will be removed again as the streamlit api is extended"""
import awesome_streamlit as ast
import awesome_streamlit.experiments.hello_world as test_page


def test__reload_module():
    """Test that we can _reload_module without an error"""
    ast.shared.components._reload_module(test_page)


def test_write_page():  # pylint: disable=redefined-outer-name
    ast.shared.components.write_page(test_page)


def video_youtube(src: str, width="100%", height=315):
    """An extension of the video widget

    Arguments:
        src {str} -- A youtube url like https://www.youtube.com/embed/B2iAodr0fOo

    Keyword Arguments:
        width {str} -- The width of the video (default: {"100%"})
        height {int} -- The height of the video (default: {315})
    """
    st.write(
        f'<iframe width="{width}" height="{height}" src="{src}" frameborder="0" '
        'allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" '
        "allowfullscreen></iframe>",
        unsafe_allow_html=True,
    )


def multiselect(label, options, default, format_func=str):
    """multiselect extension that enables default to be a subset list of the list of objects
     - not a list of strings

     Assumes that options have unique format_func representations

     cf. https://github.com/streamlit/streamlit/issues/352
     """
    options_ = {format_func(option): option for option in options}
    default_ = [format_func(option) for option in default]
    selections = st.multiselect(
        label, options=list(options_.keys()), default=default_, format_func=format_func
    )
    return [options_[format_func(selection)] for selection in selections]


def title_awesome(body: str):
    """Uses st.write to write the title as f'Awesome Streamlit {body}'
    - plus the awesome badge
    - plus a link to the awesome-streamlit GitHub page

    Arguments:
        body {str} -- [description]
    """
    st.write(
        f"# Awesome Streamlit {body} "
        "[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/"
        "d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)]"
        "(https://github.com/MarcSkovMadsen/awesome-streamlit)"
    )
