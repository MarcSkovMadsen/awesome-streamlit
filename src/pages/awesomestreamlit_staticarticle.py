import streamlit as st
import pathlib

url = pathlib.Path(__file__).parent.parent.parent / "awesome-streamlit.md"
with open(url, mode="r") as file:
    readme_md_contents = "".join(file.readlines())
st.markdown(readme_md_contents)
