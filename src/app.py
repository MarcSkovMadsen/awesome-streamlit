"""Main module for the streamlit app"""
# IMPORTANT NOTES
# - For now modules from pages have to be reloaded every time we use them
# In order for this to work they should be added to the pages.__init__ file
# pylint: disable=invalid-name
import importlib

import streamlit as st

import pages.awesome_streamlit_resources
import pages.awesome_streamlit_vision
import pages.home
import pages.spreadsheet

PAGES = {
    "Home": pages.home,
    "Resources": pages.awesome_streamlit_resources,
    "Vision": pages.awesome_streamlit_vision,
    "Spreadsheet": pages.spreadsheet,
}

selection = st.sidebar.selectbox("Select Page", list(PAGES.keys()))
st.sidebar.info(
    "You can add your awesome comments, questions, bug reports and feature requests "
    "[here](https://github.com/MarcSkovMadsen/awesome-streamlit/issues)"
)
st.sidebar.info(
    "You can find the source of this project "
    "[here](https://github.com/MarcSkovMadsen/awesome-streamlit)"
)
page = PAGES[selection]
importlib.reload(page)  # Hack? To enable how reloading

if selection not in ["Vision", "Resources"]:
    st.write(
        "# Awesome Streamlit "
        "[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/"
        "d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)]"
        "(https://github.com/MarcSkovMadsen/awesome-streamlit)"
    )
page.write()
