"""Organizes and shares business logic, data and functions
with the awesome_streamlit.testing package

  - Database interactions: Select, Insert, Update, Delete
  - REST API interactions, get, post, put, delete
  - Pandas transformations
"""
import random
from typing import List

import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit.shared.models import Resource
from awesome_streamlit.testing.models import TestItem


@st.cache
def _get_test_resources() -> List[Resource]:
    """The subset of all Resources that can be tested

    Returns:
        List[Resource] -- A list of TestItems
    """
    resources = [
        resource
        for resource in ast.database.RESOURCES
        if ast.database.resources.APP_IN_GALLERY in resource.tags
    ] + ast.database.resources.STREAMLIT_EXAMPLE_APPS_FAILED_TEST
    random.shuffle(resources)
    return resources


@st.cache
def get_test_items_from_resources() -> List[TestItem]:
    """A list of TestItems generated from the Awesome Streamlit database of Resources

    Returns:
        List[TestItem] -- A list of TestItems
    """
    return [
        TestItem.create_from_app_file_resource(resource)
        for resource in _get_test_resources()
    ]
