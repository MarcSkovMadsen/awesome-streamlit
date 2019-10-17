"""The purpose of this app is to test that the list of resources can be executed be Streamlit"""
# todo: Add timing to table and results
# todo: Handle FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
# pylint: disable=invalid-name

from typing import Callable, List

import pandas as pd
import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit import testing
from awesome_streamlit.core.services import get_file_content_as_string
from awesome_streamlit.shared.models import Resource
from awesome_streamlit.testing.models import TesTItem
from awesome_streamlit.testing.services.test_item import (
    to_dataframe as test_items_to_dataframe,
)


def write_title():
    ast.shared.components.title_awesome("Test Runner")


def write_intro_section():
    """Writes the test runner Introductory Section"""
    st.subheader("Introduction")
    st.markdown(
        """
        This test runner collects a list of **one file apps** and tests
        if they can exec(ute) successfully.

        Exception Logs are collected.


        """
    )
    st.error("IMPORTANT: THIS IS WORK IN PROGRESS AND IMMATURE!")


def write_test_collection_section(get_test_items_func: Callable) -> List[TesTItem]:
    st.subheader("""Collect tests""")
    with st.spinner("Collecting ...."):
        test_items = get_test_items_func()

    st.info(f"Collected {len(test_items)} items")
    return test_items


def write_progress_section(test_item, step, total_steps, progress_bar, file_location):
    progress = int(float(100 * step) / float(total_steps))
    progress_bar.progress(progress)
    file_location.markdown(f"Current File: [{test_item.location}](test_item.location)")


def update_test_items_dataframe(
    test_item: TesTItem, test_items_dataframe: pd.DataFrame
) -> pd.DataFrame:
    test_items_dataframe = test_items_dataframe.set_index("test")
    test_items_dataframe = test_items_dataframe.set_value(
        test_item.name, "result", test_item.result_str
    )
    test_items_dataframe = test_items_dataframe.set_value(
        test_item.name, "exception", str(test_item.exception)
    )
    test_items_dataframe = test_items_dataframe.reset_index("test")
    return test_items_dataframe


def test_items_dataframe_sort(test_items_dataframe: pd.DataFrame) -> pd.DataFrame:
    return (
        test_items_dataframe.sort_values("test")
        .sort_values("location")
        .sort_values("result")
        .reset_index(drop=True)
    )


def append_to_log(log: str, test_item: TesTItem) -> str:
    if not test_item.result:
        log += f"#### ---{test_item.name}---\n\n"
        log += f"File: [{test_item.location}]({test_item.location})\n\n"
        log += f"{test_item.traceback}\n\n"
    return log


def test_items_get_results_summary(test_items: List[TesTItem]) -> str:
    passed_count = sum([test_item.result for test_item in test_items])
    failed_count = len(test_items) - passed_count
    return f"All tests have run: {failed_count} failed, {passed_count} passed."


def write_test_run_section(test_items: List[TesTItem]):
    # Setup Sub Section
    st.subheader("""Run tests""")

    test_runner_progress_bar = st.progress(0)
    test_runner_current_file_url = st.empty()

    st.subheader("Results")
    result_table_section = st.empty()

    st.subheader("Exceptions log")
    result_exception_section = st.empty()
    log = ""

    st.subheader("Screen output")

    test_items_dataframe = test_items_to_dataframe(test_items)
    result_table_section.table(test_items_dataframe)

    test_items_count = len(test_items)
    for index, test_item in enumerate(test_items):
        write_progress_section(
            test_item,
            index,
            test_items_count,
            test_runner_progress_bar,
            test_runner_current_file_url,
        )

        st.markdown(f"#### ---{test_item.name}---\n\n")
        test_item.run_test()

        test_items_dataframe = update_test_items_dataframe(
            test_item, test_items_dataframe
        )
        result_table_section.table(test_items_dataframe)

        log = append_to_log(log, test_item)
        result_exception_section.markdown(log)

    # Report Final Results
    test_items_dataframe = test_items_dataframe_sort(test_items_dataframe)

    result_table_section.table(test_items_dataframe)
    test_runner_current_file_url.text("")
    test_runner_progress_bar.info(test_items_get_results_summary(test_items))


write_title()
write_intro_section()
test_items = write_test_collection_section(
    testing.services.test_item.get_from_resources
)
write_test_run_section(test_items)
