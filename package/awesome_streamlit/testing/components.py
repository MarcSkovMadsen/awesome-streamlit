"""In this module we define common components of the test_runner"""

from typing import Callable, List

import streamlit as st

from awesome_streamlit.testing import services
from awesome_streamlit.testing.models import TesTItem


def intro_section():
    """Writes the test runner Introductory Section"""
    st.markdown(
        """
### Introduction

This test runner collects a list of **one file apps** and tests
if they can exec(ute) successfully.

The exceptions are logged and shown below.

Currently we cannot test the frontend document tree generated. But I've created a
[feature request #432](https://github.com/streamlit/streamlit/issues/432) to be able to get the
front document HMTL tree. This will enable full backend testing of the frontend.
"""
    )


def test_collection_section(test_items_collector: Callable) -> List[TesTItem]:
    """The test collection section of the test runner

     Arguments:
        get_test_items_collector {Callable} -- A function returning the list of TesTItems to tested

    Returns:
        List[TesTItem] -- The list of test items collected
    """

    st.subheader("""Collect tests""")
    with st.spinner("Collecting ...."):
        # We need to copy in order not to mutate cached resource
        test_items = [
            TesTItem(name=item.name, location=item.location)
            for item in test_items_collector()
        ]

    st.info(f"Collected {len(test_items)} items")
    return test_items


def _progress_section(
    test_item: TesTItem, step: int, total_steps: int, progress_bar, location
):
    """Reports the progress of the inner loop of the test_run_section

    Arguments:
        test_item {TesTItem} -- The TesTItem to be tested
        step {int} -- The current iteration of the loop. A number between 1 and total_steps
        total_steps {int} -- The total number of iterations of the loop
        progress_bar {st.progressbar} -- An st.progressbar to output to
        location {st.empty} -- An st.empty to output the file location to
    """
    progress = int(float(100 * step) / float(total_steps))
    progress_bar.progress(progress)
    location.markdown(f"Current File: [{test_item.location}](test_item.location)")


def test_run_section(test_items: List[TesTItem]):
    """This section tests each test_item and reports the Test Results and Exception Log

    Arguments:
        test_item {TesTItem} -- The TesTItem to be tested
    """
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

    test_items_dataframe = services.test_items_dataframe.create_from_test_items(
        test_items
    )
    result_table_section.table(test_items_dataframe)

    test_items_count = len(test_items)
    for index, test_item in enumerate(test_items):
        _progress_section(
            test_item,
            index + 1,
            test_items_count,
            test_runner_progress_bar,
            test_runner_current_file_url,
        )

        st.markdown(f"#### ---{test_item.name}---\n\n")
        test_item.run_test()

        test_items_dataframe = services.test_items_dataframe.update(
            test_items_dataframe, test_item
        )
        result_table_section.table(test_items_dataframe)

        log = services.test_item.append_to_log(log, test_item)
        result_exception_section.markdown(log)

    # Report Final Results
    test_items_dataframe = services.test_items_dataframe.sort(test_items_dataframe)

    result_table_section.table(test_items_dataframe)
    test_runner_current_file_url.text("")
    test_runner_progress_bar.info(
        services.test_item.to_test_results_summary(test_items)
    )


# if __name__ == "__main__":
#     # The code below helps to visually and manually test the components during development
#     intro_section()

#     def test_items_collector():
#         return [
#             TesTItem(
#                 name="Test 1",
#                 location=(
#                     "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/"
#                     "gallery/spreadsheet.py",
#                 ),
#             )
#         ]

#     test_items = test_collection_section(test_items_collector=test_items_collector)

#     test_run_section(test_items)
