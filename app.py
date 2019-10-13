"""Main module for the streamlit app"""
# IMPORTANT NOTES
# - For now modules from pages have to be reloaded every time we use them
# In order for this to work they should be added to the pages.__init__ file
# pylint: disable=invalid-name
import streamlit as st

# Import all needed packages
# Dont write 'from src.pages import home'. Autoreload will not work!
# Dont write 'import src.pages.home as home'. Autoreload will not work!
# Use the same convention for importing in submodules. Otherwise Autoreload will not work!
# cf. https://github.com/MarcSkovMadsen/awesome-streamlit/issues/2
import config
import src.st_extensions
import src.pages.home
import src.pages.resources
import src.pages.vision
import src.pages.gallery.index

# Please import all other modules that needs livereload here
# Dont write 'from src.pages.gallery import spacyio'. Autoreload will not work!
# Dont write 'from src.shared.components.st_awesome as st_awesome'. Autoreload will not work!
# Use the same convention for importing in submodules. Otherwise Autoreload will not work!
# cf. https://github.com/MarcSkovMadsen/awesome-streamlit/issues/2
if config.DEBUG:
    import src.st_awesome  # pylint: disable=unused-import

PAGES = {
    "Home": src.pages.home,
    "Resources": src.pages.resources,
    "Gallery": src.pages.gallery.index,
    "Vision": src.pages.vision,
}
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
try:
    src.st_extensions.write_page(page)
except Exception as _:
    st.error("Error. Something wen't wrong! Please refresh the app")
st.sidebar.title("Contributions")
st.sidebar.info(
    "You are very welcome to **contribute** your awesome comments, questions, "
    "resources, apps or code.\n"
    "- [Create Issue](https://github.com/MarcSkovMadsen/awesome-streamlit/issues)\n"
    "- [Create Pull Request](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls)\n"
    "- [View Source Code](https://github.com/MarcSkovMadsen/awesome-streamlit)\n\n"
)
st.sidebar.title("About")
st.sidebar.info(
    "This app is maintained by Marc Skov Madsen. "
    "You can learn more about me at [datamodelsanalytics.com](https://datamodelsanalytics.com)."
)
