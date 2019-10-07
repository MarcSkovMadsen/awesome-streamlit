import streamlit as st
import pathlib


def write():
    url = pathlib.Path(__file__).parent.parent.parent / "README.md"
    with open(url, mode="r") as file:
        readme_md_contents = "".join(file.readlines())
    st.markdown(readme_md_contents)
