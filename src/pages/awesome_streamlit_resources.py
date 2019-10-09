"""This page is for searching and viewing the list of awesome resources"""
import streamlit as st

import db


def write():
    """Method used to write page in app.py"""
    st.subheader("Resources")

    tags = st.multiselect("Filter", db.TAGS)

    if not tags:
        resources = db.RESOURCES
    else:
        resources = []
        for resource in db.RESOURCES:
            if set(resource.tags).intersection(tags):
                resources.append(resource)
    resources = sorted(resources, key=lambda x: x.name)
    markdown_bullets = [resource.to_markdown_bullet() for resource in resources]
    markdown = "\n".join(markdown_bullets)
    st.write(markdown)

    if st.sidebar.checkbox("Show Resource JSON"):
        st.subheader("Source JSON")
        st.write(db.RESOURCES)
