"""This page is for searching and viewing the list of awesome resources"""
import logging

import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit.core.services import resources

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    """Writes content to the app"""
    ast.shared.components.title_awesome("Resources")
    st.sidebar.title("Resources")
    show_awesome_resources_only = st.sidebar.checkbox(
        "Show Awesome Resources Only", value=True
    )

    tags = ast.shared.components.multiselect(
        "Select Tag(s)", options=ast.database.TAGS, default=[]
    )

    st.info(
        """Please note that resources can have multiple tags!
    We list each resource under **a most important tag only!**"""
    )
    resource_section = st.empty()

    with st.spinner("Loading resources ..."):
        markdown = resources.get_resources_markdown(tags, show_awesome_resources_only)
        resource_section.markdown(markdown)

    if st.sidebar.checkbox("Show Resource JSON"):
        st.subheader("Source JSON")
        st.write(ast.database.RESOURCES)

    tags = None


if __name__ == "__main__":
    write()
