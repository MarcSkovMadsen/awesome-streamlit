"""This module provides services related to Resources"""
from collections import defaultdict
from typing import Dict, List, Optional

from awesome_streamlit.database.resources import RESOURCES
from awesome_streamlit.shared.models import Author, Resource, Tag


def filter_by_tags(resources: List[Resource], tags: List[Tag]) -> List[Resource]:
    """The resources having all of the specified Tags

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
            if set(tags).issubset(resource.tags):
                resources_.append(resource)
        return resources_

    return resources


def filter_by_is_awesome(resources: List[Resource]) -> List[Resource]:
    """The resources being that is_awesome

    Arguments:
        resources {List[Resource]} -- A list of resources

    Returns:
        List[Resource] - A list of awesome resources
    """
    return [resource for resource in resources if resource.is_awesome]


def filter_by_author(resources: List[Resource], author: Author) -> List[Resource]:
    """The resources by the specified author

    Arguments:
        resources {List[Resource]} -- A list of resources

    Returns:
        List[Resource] - A list of resources by the specified author
    """
    return [resource for resource in resources if resource.author == author]


def sort_resources(resources: List[Resource]) -> List[Resource]:
    """The list of resources sorted by name

    Returns:
        [List[Resource]] -- The list of resources sorted by name
    """
    return sorted(resources, key=lambda x: x.name)


def get_resources(
    tags: List[Tag], author: Optional[Author] = None, awesome_resources_only: bool = True
) -> List[Resource]:
    """A list of resources

    Arguments:
        tags {List[Tag]} -- If non-empty then the list of Resources is reduced to
        Resources having one of the specified tags

    Keyword Arguments:
        author {Author} -- If an author is specified the list of resources is reduced to
        resources by that author (default: {None})
        awesome_resources_only {bool} -- If True then the list is reduced to
        Resources with is_awesome equal to True(default: {True})

    Returns:
        List[Resource] -- A list of Resources
    """
    resources = RESOURCES
    if author:
        resources = filter_by_author(resources, author)
    if awesome_resources_only:
        resources = filter_by_is_awesome(resources)
    resources = sort_resources(resources)
    resources = filter_by_tags(resources, tags)
    return resources


def to_markdown(resources: List[Resource], report_by_tag: bool = True) -> str:
    """Converts the specified resources to MarkDown

    Arguments:
        resources {List[Resource]} -- [description]

    Optional Arguments:
        report_by_tag {bool} - If True the text is split into sections by Tags

    Returns:
        [str] -- Bulleted Markdown List of Resources
    """

    if report_by_tag:
        markdown_bullets = []
        resources_dict: Dict[Tag, List[Resource]] = defaultdict(list)
        for resource in resources:
            resources_dict[resource.tags[0]].append(resource)

        for tag in sorted(resources_dict.keys(), key=lambda x: x.name):
            markdown_bullets.append(f"\n### {tag.name}\n")
            for resource in resources_dict[tag]:
                markdown_bullets.append(resource.to_markdown_bullet())
    else:
        markdown_bullets = [resource.to_markdown_bullet() for resource in resources]

    markdown = "\n".join(markdown_bullets)

    return markdown


def get_resources_markdown(
    tags: List[Tag], author: Optional[Author] = None, awesome_resources_only: bool = True
) -> str:
    """A bulleted Markdown list of resources filtered as specified

    Arguments:
        tags {List[Tag]} -- A list of tags to filter to. If the list is empty [] then we
do no filtering on Tags

    Keyword Arguments:
        Author {Author} -- An author to filter to. If author is None
then we do no filtering on author. (default: {None})
        awesome_resources_only {bool} -- [description] (default: {True})

    Returns:
        str -- A bulleted Markdown list of resources filtered as specified
    """
    resources = get_resources(tags, author, awesome_resources_only)
    return to_markdown(resources, not tags)
