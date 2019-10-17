"""Organizes and shares business logic, data and functions
with the awesome_streamlit.testing package

  - Database interactions: Select, Insert, Update, Delete
  - REST API interactions, get, post, put, delete
  - Pandas transformations
"""
import random
from typing import List

import pandas as pd
import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit.shared.models import Resource
from awesome_streamlit.testing.models import TesTItem


@st.cache
def _get_list_of_test_resources() -> List[Resource]:
    """The subset of all Resources that can be tested

    Returns:
        List[Resource] -- A list of TesTItems
    """
    resources = [
        resource
        for resource in ast.database.RESOURCES
        if ast.database.resources.APP_IN_GALLERY in resource.tags
    ] + ast.database.resources.STREAMLIT_EXAMPLE_APPS_FAILED_TEST
    random.shuffle(resources)
    return resources


@st.cache
def get_from_resources() -> List[TesTItem]:
    """A list of TesTItems generated from the Awesome Streamlit database of Resources

    Returns:
        List[TesTItem] -- A list of TesTItems
    """
    return [
        TesTItem.create_from_app_file_resource(resource)
        for resource in _get_list_of_test_resources()
    ]


def _to_short_string(text: str, max_length: int = 75) -> str:
    """Caps the string at 75 characters. If longer than 75 it's capped at max_length-3
    and '...' is appended

    Arguments:
        text {str} -- A text string

    Keyword Arguments:
        max_length {int} -- The maximum number of characters (default: {75})

    Returns:
        str -- The capped string
    """
    if len(text) < max_length:
        return text

    return text[0:72] + "..."


@st.cache
def to_dataframe(test_items: List[TesTItem]) -> pd.DataFrame:
    """Converts a List of TesTItems to a Pandas Dataframe

    Arguments:
        test_items {List[TesTItem]} -- A list of TesTItems

    Returns:
        pd.DataFrame -- A pandas dataframe with
columns columns=['test', 'location', 'result', 'exception']
    """

    return pd.DataFrame(
        [
            (test_item.name, _to_short_string(test_item.location), "", "")
            for test_item in test_items
        ],
        columns=["test", "location", "result", "exception"],
    )
