"""This page is for searching and viewing the list of awesome resources"""
import logging
from collections import defaultdict

import streamlit as st

import awesome_streamlit as ast
import config
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


@st.cache
def get_sorted_resources(awesome_resources_only: bool = True):
    """The list of resources sorted by name

    Keyword Arguments:
        awesome_resources_only {bool} -- If True only awesome resources
will be included in the list (default: {True})

    Returns:
        [type] -- The list of resources sorted by name
    """
    resources = sorted(ast.database.RESOURCES, key=lambda x: x.name)
    if awesome_resources_only:
        resources = filter_by_is_awesome(resources)
    return resources


@st.cache
def get_resources_markdown(tags, awesome_resources_only=True) -> str:
    """A bulleted Markdown list of resources filtered as specified

    Arguments:
        tags {[type]} -- A list of tags to filter to. If the list is empty [] then we
do no filtering on Tags

    Keyword Arguments:
        awesome_resources_only {bool} -- [description] (default: {True})

    Returns:
        str -- A bulleted Markdown list of resources filtered as specified
    """
    resources = get_sorted_resources(awesome_resources_only)
    resources = filter_by_tags(resources, tags)
    return to_markdown(resources)


def write():
    """Writes content to the app"""
    src.st_awesome.title("Resources")
    st.sidebar.title("Resources")
    show_awesome_resources_only = st.sidebar.checkbox(
        "Show Awesome Resources Only", value=True
    )

    tags = src.st_extensions.multiselect(
        "Select Tag(s)", options=ast.database.TAGS, default=[]
    )

    st.info(
        """Please note that resources can have multiple tags!
    We list each resource under **a most important tag only!**"""
    )
    resource_section = st.empty()

    with st.spinner("Loading resources ..."):
        markdown = get_resources_markdown(tags, show_awesome_resources_only)
        resource_section.markdown(markdown)

    if st.sidebar.checkbox("Show Resource JSON"):
        st.subheader("Source JSON")
        st.write(ast.database.RESOURCES)

    tags = None


if __name__ == "__main-_":
    write()
