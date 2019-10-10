"""Page for viewing the awesome Streamlit vision"""
import pathlib

import streamlit as st
from src.shared import components as st_awesome


def write():
    """Method used to write the page in the app.py file"""
    url = pathlib.Path(__file__).parent.parent.parent / "AWESOME-STREAMLIT.md"
    with open(url, mode="r") as file:
        readme_md_contents = "".join(file.readlines())
    readme_md_contents = readme_md_contents.split("\n", 3)[-1]
    st_awesome.title("Vision")
    st.markdown(readme_md_contents)
