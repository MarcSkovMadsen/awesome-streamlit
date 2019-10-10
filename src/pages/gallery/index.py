"""Gallery page used to navigate between examples"""
# IMPORTANT NOTES
# - For now modules from APPS have to be reloaded every time we use them
# In order for this to work they should be added to the APPS.__init__ file
# pylint: disable=invalid-name
import streamlit as st
import src.st_extensions
import src.st_awesome
import src.pages.gallery.spacyio
import src.pages.gallery.spreadsheet

APPS = {
    "SpacyIO": src.pages.gallery.spacyio,
    "Spreadsheet": src.pages.gallery.spreadsheet,
}


def write():
    """Used to write the contents of this page in app.py"""
    src.st_awesome.title("Gallery")
    if len(APPS) > 1:
        selection = st.selectbox("Select App", list(APPS.keys()))
    else:
        selection = list(APPS.keys())[0]
    page = APPS[selection]

    src.st_extensions.write_page(page)
