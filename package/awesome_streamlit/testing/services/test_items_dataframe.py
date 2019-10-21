"""In this module we define services of a Test Results DataFrame.

The Test Results DataFrame is used for reporting the collected tests and their test results
"""
from typing import List

import pandas as pd
import streamlit as st

from awesome_streamlit.testing.models import TesTItem


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
def create_from_test_items(test_items: List[TesTItem]) -> pd.DataFrame:
    """Converts a List of TesTItems to a Pandas Dataframe

    Arguments:
        test_items {List[TesTItem]} -- A list of TesTItems

    Returns:
        pd.DataFrame -- A pandas dataframe with columns=['test', 'location', 'result', 'exception']
    """

    return pd.DataFrame(
        [
            (test_item.name, _to_short_string(test_item.location), "", "")
            for test_item in test_items
        ],
        columns=["test", "location", "result", "exception"],
    )


def update(test_items_dataframe: pd.DataFrame, test_item: TesTItem) -> pd.DataFrame:
    """Updates the test_items_dataframe with the result and exception of the test_item

    Arguments:
        test_items_dataframe {pd.DataFrame} -- A DataFrame of TesTItems to be updated
        test_item {TesTItem} -- The TesTItem to use for the update

    Returns:
        pd.DataFrame -- A new, updated dataframe
    """
    test_items_dataframe = test_items_dataframe.set_index("test")
    test_items_dataframe = test_items_dataframe.set_value(
        test_item.name, "result", test_item.result_str
    )
    test_items_dataframe = test_items_dataframe.set_value(
        test_item.name, "exception", str(test_item.exception)
    )
    test_items_dataframe = test_items_dataframe.reset_index("test")
    return test_items_dataframe


def sort(test_items_dataframe: pd.DataFrame) -> pd.DataFrame:
    """Sorts the TesTItems dataframe by result, test, location and resets the index

    Arguments:
        test_items_dataframe {pd.DataFrame} -- A TesTItem dataframe

    Returns:
        pd.DataFrame -- A new, sorted TesTItem dataframe
    """
    return (
        test_items_dataframe.sort_values("location")
        .sort_values("test")
        .sort_values("result")
        .reset_index(drop=True)
    )
