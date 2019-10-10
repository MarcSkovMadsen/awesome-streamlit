"""This page is for searching and viewing the list of awesome resources"""
from collections import defaultdict
import streamlit as st

import db
import streamlit_extensions as st_extensions
from src.shared import components as st_awesome


def write():
    """Method used to write page in app.py"""
    st_awesome.title("Resource")

    tags = st_extensions.multiselect("Select Tag(s)", options=db.TAGS, default=[])
    st.info(
        """Please note that resources can have multiple tags!
    We list each resource under **a most important tag only**"""
    )
    if not tags:
        resources = db.RESOURCES
    else:
        resources = []
        for resource in db.RESOURCES:
            if set(resource.tags).intersection(tags):
                resources.append(resource)
    resources = sorted(resources, key=lambda x: x.name)

    resources_dict = defaultdict(list)
    for resource in resources:
        resources_dict[resource.tags[0]].append(resource)

    markdown_bullets = []
    for tag in sorted(resources_dict.keys(), key=lambda x: x.name):
        markdown_bullets.append(f"### {tag.name}\n")
        for resource in resources_dict[tag]:
            markdown_bullets.append(resource.to_markdown_bullet())
        markdown_bullets.append("\n")
    markdown = "\n".join(markdown_bullets)
    st.write(markdown)
    # print markdown and copy to README.md to keep it updated
    # print(markdown)
    if st.sidebar.checkbox("Show Resource JSON"):
        st.subheader("Source JSON")
        st.write(db.RESOURCES)


if __name__ == "__main-_":
    write()
