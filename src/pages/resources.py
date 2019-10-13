"""This page is for searching and viewing the list of awesome resources"""
import logging
from collections import defaultdict

import streamlit as st

import config
import db
import src.st_awesome
import src.st_extensions

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


@st.cache
def filter_by_tags(resources, tags):
    """The resources having one of the specified Tags

    If tags is the empty list all resources are returned

    Arguments:
        resources {[type]} -- A list of Resources
        tags {[type]} -- A list of Tags

    Returns:
        [type] -- A list of Resources
    """
    if tags:
        resources_ = []
        for resource in resources:
            if set(resource.tags).intersection(tags):
                resources_.append(resource)
        return resources_

    return resources


@st.cache
def filter_by_is_awesome(resources):
    """The resources being that is_awesome

    Arguments:
        resources {[type]} -- A list of resources
    """
    return [resource for resource in resources if resource.is_awesome]


@st.cache
def to_markdown(resources):
    """Converts the specified resources to MarkDown

    Arguments:
        resources {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    resources_dict = defaultdict(list)
    for resource in resources:
        resources_dict[resource.tags[0]].append(resource)
    markdown_bullets = []
    for tag in sorted(resources_dict.keys(), key=lambda x: x.name):
        markdown_bullets.append(f"\n### {tag.name}\n")
        for resource in resources_dict[tag]:
            markdown_bullets.append(resource.to_markdown_bullet())
    markdown = "\n".join(markdown_bullets)
    if config.DEBUG:
        print(markdown)

    return markdown


def write():
    """Writes content to the app"""
    src.st_awesome.title("Resources")
    st.sidebar.title("Resources")

    tags = src.st_extensions.multiselect("Select Tag(s)", options=db.TAGS, default=[])

    with st.spinner("Loading resources ..."):
        logging.info(tags)
        resources = filter_by_tags(db.RESOURCES, tags)

        if st.sidebar.checkbox("Show Awesome Resources Only", value=True):
            resources = filter_by_is_awesome(resources)

        resources = sorted(resources, key=lambda x: x.name)

    st.info(
        """Please note that resources can have multiple tags!
    We list each resource under **a most important tag only!**"""
    )

    markdown = to_markdown(resources)
    st.write(markdown)

    if st.sidebar.checkbox("Show Resource JSON"):
        st.subheader("Source JSON")
        st.write(db.RESOURCES)

    tags = None


if __name__ == "__main-_":
    write()
