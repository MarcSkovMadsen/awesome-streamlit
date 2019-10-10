"""Extensions of the streamlit api

For now these are hacks and hopefully a lot of them will be removed again as the streamlit api is
extended"""
import logging
import sys

import streamlit as st

import config

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write_page(page):  # pylint: disable=redefined-outer-name
    """Writes the specified page/module

    Our multipage app is structured into sub-files with a `def write()` function

    Arguments:
        page {module} -- A module with a 'def write():' function
    """
    if config.DEBUG:
        logging.info("Writing: %s", page)
        logging.info("In sys.modules: %s", page in sys.modules)
    page.write()


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
