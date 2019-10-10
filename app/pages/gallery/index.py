"""Gallery page used to navigate between examples"""
# IMPORTANT NOTES
# - For now modules from APPS have to be reloaded every time we use them
# In order for this to work they should be added to the APPS.__init__ file
# pylint: disable=invalid-name
import importlib

import streamlit as st
import streamlit_extensions as st_extensions
from . import spacyio, spreadsheet

APPS = {"SpacyIO": spacyio, "Spreadsheet": spreadsheet}


def write():
    """Used to write the contents of this page in app.py"""
    st.write(
        f"# Awesome Streamlit Gallery "
        "[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/"
        "d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)]"
        "(https://github.com/MarcSkovMadsen/awesome-streamlit)"
    )
    if len(APPS) > 1:
        selection = st.selectbox("Select App", list(APPS.keys()))
    else:
        selection = list(APPS.keys())[0]
    page = APPS[selection]

    st_extensions.write_page(page)
