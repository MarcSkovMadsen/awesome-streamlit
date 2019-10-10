"""Page for viewing the awesome Streamlit vision"""
import pathlib

import streamlit as st


def write():
    """Method used to write the page in the app.py file"""
    url = pathlib.Path(__file__).parent.parent.parent / "AWESOME-STREAMLIT.md"
    with open(url, mode="r") as file:
        readme_md_contents = "".join(file.readlines())
    readme_md_contents = readme_md_contents.split("\n", 3)[-1]
    st.write(
        f"# Awesome Streamlit Vision "
        "[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/"
        "d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)]"
        "(https://github.com/MarcSkovMadsen/awesome-streamlit)"
    )
    st.markdown(readme_md_contents)
