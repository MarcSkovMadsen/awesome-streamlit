"""Main module for the streamlit app"""
# IMPORTANT NOTES
# - For now modules from pages have to be reloaded every time we use them
# In order for this to work they should be added to the pages.__init__ file
# pylint: disable=invalid-name
import streamlit as st
import streamlit_extensions as st_extensions

from src.pages import home, resources, vision
from src.pages.gallery import index as gallery

PAGES = {"Home": home, "Resources": resources, "Gallery": gallery, "Vision": vision}

selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
st_extensions.write_page(page)

st.sidebar.info(
    "You can **contribute** your awesome comments, questions, resources, apps, bug reports and "
    "feature requests "
    "as [issues](https://github.com/MarcSkovMadsen/awesome-streamlit/issues) or "
    "[pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls)."
    "\n\n"
    "You can find the **source** of this app "
    "[here](https://github.com/MarcSkovMadsen/awesome-streamlit)."
    "\n\n"
    "This app is maintained by Marc Skov Madsen. "
    "You can learn more about me at [datamodelsanalytics.com](https://datamodelsanalytics.com)"
)
