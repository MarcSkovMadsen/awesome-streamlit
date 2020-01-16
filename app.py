"""Main module for the streamlit app"""
import streamlit as st

import awesome_streamlit as ast
import src.pages.about
import src.pages.gallery.index
import src.pages.home
import src.pages.resources
import src.pages.vision

ast.core.services.other.set_logging_format()

PAGES = {
    "Home": src.pages.home,
    "Resources": src.pages.resources,
    "Gallery": src.pages.gallery.index,
    "Vision": src.pages.vision,
    "About": src.pages.about,
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]

    with st.spinner(f"Loading {selection} ..."):
        ast.shared.components.write_page(page)
    st.sidebar.title("Contribute")
    st.sidebar.info(
        "This an open source project and you are very welcome to **contribute** your awesome "
        "comments, questions, resources and apps as "
        "[issues](https://github.com/MarcSkovMadsen/awesome-streamlit/issues) of or "
        "[pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls) "
        "to the [source code](https://github.com/MarcSkovMadsen/awesome-streamlit). "
    )
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This app is maintained by Marc Skov Madsen. You can learn more about me at
        [datamodelsanalytics.com](https://datamodelsanalytics.com).
"""
    )


if __name__ == "__main__":
    main()
