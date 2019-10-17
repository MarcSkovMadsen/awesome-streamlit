"""The purpose of this app is to test that the list of resources can be executed be Streamlit"""
# todo: Add timing to table and results
# todo: Handle FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
# pylint: disable=invalid-name

import pandas as pd
import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit import testing
from awesome_streamlit.core.services import (get_file_content_as_string,
                                             test_item.to_dataframe)
from awesome_streamlit.shared.models import Resource
from awesome_streamlit.testing.models import TesTItem

ast.shared.components.title_awesome("Test Runner")
st.markdown(
    """
    This test runner collects a list of **one file apps** and tests
    if they can exec(ute) successfully.

    Exception Logs are collected.


    """
)
st.error("IMPORTANT: THIS IS WORK IN PROGRESS AND IMMATURE!")
st.subheader("""Collect tests""")
with st.spinner("Collecting ...."):
    test_items = testing.services.test_items.get_from_resources()

tests_count = len(test_items)
st.info(f"Collected {tests_count} items")
test_items_dataframe = test_item.to_dataframe(test_items)

st.subheader("""Run tests""")
log = ""


test_run_progress = st.progress(0)
test_current_file_url = st.empty()

st.subheader("Results")
result_section = st.empty()
result_done_section = st.empty()
result_select_section = st.empty()

st.subheader("Exceptions log")
result_exception_section = st.empty()

st.subheader("----- SCREEN OUTPUT BELOW ------")

result_section.table(test_items_dataframe)

for index, test_item in enumerate(test_items):
    progress = int(float(100 * index) / float(tests_count))
    test_run_progress.progress(progress)
    test_current_file_url.markdown(
        f"Current File: [{test_item.location}](test_item.location)"
    )

    test_item.run_test()

    test_items_dataframe = test_items_dataframe.set_index("test")
    test_items_dataframe = test_items_dataframe.set_value(
        test_item.name, "result", test_item.result_str
    )
    test_items_dataframe = test_items_dataframe.set_value(
        test_item.name, "exception", str(test_item.exception)
    )
    # test_items_dataframe = test_items_dataframe.sort_values("exception")
    test_items_dataframe = test_items_dataframe.reset_index("test")
    result_section.table(test_items_dataframe)

    if not test_item.result:
        log += f"# {test_item.name}\n\n"
        log += f"File: [{test_item.location}]({test_item.location})\n\n"
        log += f"{test_item.traceback}\n\n"
    result_exception_section.markdown(log)

test_items_dataframe = (
    test_items_dataframe.sort_values("test")
    .sort_values("location")
    .sort_values("result")
    .reset_index(drop=True)
)
result_section.table(test_items_dataframe)

passed_count = sum([test_item.result for test_item in test_items])
failed_count = tests_count - passed_count
test_current_file_url.text("")
test_run_progress.info(
    f"All tests have run: {failed_count} failed, {passed_count} passed."
)
