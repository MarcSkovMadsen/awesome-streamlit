"""Organizes and shares business logic, data and functions
with the awesome_streamlit.testing package

  - Database interactions: Select, Insert, Update, Delete
  - REST API interactions, get, post, put, delete
  - Pandas transformations
"""
import random
from typing import List

import streamlit as st

from awesome_streamlit import database
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
        for resource in database.RESOURCES
        if database.resources.APP_IN_GALLERY in resource.tags
    ] + database.resources.STREAMLIT_EXAMPLE_APPS_FAILED_TEST
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


# Refactor to get_log_string
def append_to_log(log: str, test_item: TesTItem) -> str:
    """Appends the traceback a TesTItem to the log

    Arguments:
        log {str} -- A log
        test_item {TesTItem} -- A TesTItem

    Returns:
        str -- A new log with the exception appended
    """
    if not test_item.result:
        log += f"#### ---{test_item.name}---\n\n"
        log += f"File: [{test_item.location}]({test_item.location})\n\n"
        log += f"{test_item.traceback}\n\n"
    return log


def to_test_results_summary(test_items: List[TesTItem]) -> str:
    """Summary of failed and passed tests count

    Arguments:
        test_items {List[TesTItem]} -- A list of TesTItems

    Returns:
        str -- Summary of failed and passed tests count
    """
    passed_count = sum([test_item.result for test_item in test_items])
    failed_count = len(test_items) - passed_count
    return f"All tests have run: {failed_count} failed, {passed_count} passed."
