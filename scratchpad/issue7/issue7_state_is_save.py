"""This is a minimum replicating example of this issue
https://github.com/MarcSkovMadsen/awesome-streamlit/issues/7"""
import streamlit as st

pages = ["Home", "Resources"]
tags = ["Awesome", "Social"]

page = st.sidebar.radio("Navigate", options=pages)
st.title(page)
if page == "Resources":
    selection = st.multiselect("Select tag", tags)
    st.write(selection)
