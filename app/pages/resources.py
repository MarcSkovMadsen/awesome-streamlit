"""This page is for searching and viewing the list of awesome resources"""
from collections import defaultdict
import streamlit as st

import db
import streamlit_extensions as st_extensions


def write():
    """Method used to write page in app.py"""
    st.write(
        f"# Awesome Streamlit Resources "
        "[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/"
        "d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)]"
        "(https://github.com/MarcSkovMadsen/awesome-streamlit)"
    )

    tags = st_extensions.multiselect("Select Tag(s)", options=db.TAGS, default=[])
    st.info(
        """Please note that resources can belong to multiple categories!
    We list each resource under **one category only**"""
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
