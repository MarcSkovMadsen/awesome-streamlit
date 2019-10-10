"""Main module for the streamlit app"""
# IMPORTANT NOTES
# - For now modules from pages have to be reloaded every time we use them
# In order for this to work they should be added to the pages.__init__ file
# pylint: disable=invalid-name
import streamlit as st
import st_extensions

# Dont write 'from src.pages import home'. Autoreload will not work.
# cf. https://github.com/MarcSkovMadsen/awesome-streamlit/issues/2
import src.pages.home as home
import src.pages.resources as resources
import src.pages.vision as vision
import src.pages.gallery.index as index

# Please import all other modules that needs livereload here
# Dont write 'from src.pages.gallery import spacyio'. Autoreload will not work!
# Dont write 'from src.shared.components.st_awesome import as st_awesome'. Autoreload will not work!
# cf. https://github.com/MarcSkovMadsen/awesome-streamlit/issues/2
import src.shared.components.st_awesome  # pylint: disable=unused-import
import src.pages.gallery.spacyio  # pylint: disable=unused-import
import src.pages.gallery.spreadsheet  # pylint: disable=unused-import

PAGES = {"Home": home, "Resources": resources, "Gallery": index, "Vision": vision}

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
