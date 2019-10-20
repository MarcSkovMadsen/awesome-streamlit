"""This page is for searching and viewing the list of awesome resources"""
import logging
from collections import defaultdict

import streamlit as st
from typing import List
import awesome_streamlit as ast
from awesome_streamlit.shared.models import Resource, Tag

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write():
    """Writes content to the app"""
    ast.shared.components.title_awesome("Resources")
    st.sidebar.title("Resources")
    show_awesome_resources_only = st.sidebar.checkbox(
        "Show Awesome Resources Only", value=True
    )

    tags = ast.shared.components.multiselect(
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


def filter_by_tags(resources: List[Resource], tags: List[Tag]) -> List[Resource]:
    """The resources having one of the specified Tags

    If tags is the empty list all resources are returned

    Arguments:
        resources {List[Resource]} -- A list of Resources
        tags {List[Tag]} -- A list of Tags

    Returns:
        [List[Resource]] -- A list of Resources
    """
    if tags:
        resources_ = []
        for resource in resources:
            if set(resource.tags).intersection(tags):
                resources_.append(resource)
        return resources_

    return resources


def filter_by_is_awesome(resources: List[Resource]) -> List[Resource]:
    """The resources being that is_awesome

    Arguments:
        resources {List[Resource]} -- A list of resources
    """
    return [resource for resource in resources if resource.is_awesome]


def sort_resources(resources: List[Resource]) -> List[Resource]:
    """The list of resources sorted by name

    Returns:
        [List[Resource]] -- The list of resources sorted by name
    """
    return sorted(resources, key=lambda x: x.name)


def get_resources(
    tags: List[Tag], awesome_resources_only: bool = True
) -> List[Resource]:
    resources = ast.database.RESOURCES
    if awesome_resources_only:
        resources = filter_by_is_awesome(resources)
    resources = sort_resources(resources)
    resources = filter_by_tags(resources, tags)
    return resources


def to_markdown(resources: List[Resource]) -> str:
    """Converts the specified resources to MarkDown

    Arguments:
        resources {List[Resource]} -- [description]

    Returns:
        [str] -- Bulleted Markdown List of Resources
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

    return markdown


def get_resources_markdown(tags: List[Tag], awesome_resources_only: bool = True) -> str:
    """A bulleted Markdown list of resources filtered as specified

    Arguments:
        tags {[type]} -- A list of tags to filter to. If the list is empty [] then we
do no filtering on Tags

    Keyword Arguments:
        awesome_resources_only {bool} -- [description] (default: {True})

    Returns:
        str -- A bulleted Markdown list of resources filtered as specified
    """
    resources = get_resources(tags, awesome_resources_only)
    return to_markdown(resources)


if __name__ == "__main__":
    write()
