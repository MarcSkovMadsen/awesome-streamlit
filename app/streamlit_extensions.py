"""Extensions of the streamlit api

For now these are hacks and hopefully a lot of them will be removed again as the streamlit api is
extended"""
import importlib
import logging

import streamlit as st

import config

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write_page(page):  # pylint: disable=redefined-outer-name
    """Writes the specified page/module

    Our multipage app is structured into sub-files with a `def write()` function

    Arguments:
        page {module} -- A module with a 'def write():' function
    """
    try:
        if config.RELOAD_MODULES:
            importlib.import_module(page.__name__)
            importlib.reload(page)
    except ImportError as _:
        logging.info(
            """Info. Cannot reload %s.
            Please use streamlit run '%s' directly while developing
            or reload manually by navigating to another page and back
            """,
            page,
            page.__file__,
        )
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
        f'<iframe width="{width}" height="{height}" src="{src}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        unsafe_allow_html=True,
    )
