"""Page for viewing the awesome Streamlit vision"""
import pathlib

import streamlit as st

import awesome_streamlit as ast


@st.cache
def get_vision_markdown() -> str:
    """Returns the Vision

    Returns:
        str -- The vision as a string of MarkDown
    """
    url = pathlib.Path(__file__).parent.parent.parent / "AWESOME-STREAMLIT.md"
    with open(url, mode="r") as file:
        readme_md_contents = "".join(file.readlines())
    return readme_md_contents.split("\n", 3)[-1]


def write():
    """Method used to write the page in the app.py file"""
    ast.shared.components.title_awesome("Vision")
    with st.spinner("Loading  ..."):
        vision = get_vision_markdown()
        st.markdown(vision)
