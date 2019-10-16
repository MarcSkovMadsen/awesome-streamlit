"""The purpose of this app is to test that the list of resources can be executed be Streamlit"""
import ast.shared.components as st_awesome
import random
# todo: Add timing to table and results
# todo: Handle FutureWarning: set_value is deprecated and will be removed in a future release. Please use .at[] or .iat[] accessors instead
import traceback
# pylint: disable=invalid-name
import urllib.request
from typing import List, NamedTuple, Optional

import pandas as pd
import streamlit as st

import db
from awesome_streamlit.shared.models import Resource


class TestResult(NamedTuple):
    resource: Resource
    python_code: str
    exception: Optional[Exception] = None
    traceback: str = ""

    @property
    def result(self) -> bool:
        if self.exception:
            return False
        return True

    @property
    def result_str(self) -> str:
        if self.exception:
            return "failed"
        return "passed"


@st.cache
def get_file_content_as_string(url: str) -> str:
    """The url content as a string

    Arguments:
        url {str} -- The url to request

    Returns:
        str -- The text of the url
    """
    data = urllib.request.urlopen(url).read()
    return data.decode("utf-8")


@st.cache
def get_test_resources() -> List[Resource]:
    resources = [
        resource for resource in db.RESOURCES if db.APP_IN_GALLERY in resource.tags
    ] + db.STREAMLIT_EXAMPLE_APPS_FAILED_TEST
    random.shuffle(resources)
    return resources


def get_test_result(resource) -> TestResult:
    exception_ = None
    traceback_ = ""

    # Run the child app
    python_code = ""
    try:
        python_code = get_file_content_as_string(resource.url)
        exec(python_code, globals())  # pylint: disable=exec-used
    except Exception as exception:
        traceback_ = traceback.format_exc()
        exception_ = exception

    return TestResult(
        resource=resource,
        exception=exception_,
        traceback=traceback_,
        python_code=python_code,
    )


@st.cache
def get_test_results_dataframe(resources: List[Resource]) -> pd.DataFrame:
    return pd.DataFrame(
        [(resource.name, resource.author.name, "", "") for resource in app_resources],
        columns=["test", "author", "result", "exception"],
    )


st_awesome.title("Test Runner")
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
    app_resources = get_test_resources()

tests_count = len(app_resources)
st.info(f"Collected {tests_count} items")
test_results_dataframe = get_test_results_dataframe(app_resources)

st.subheader("""Run tests""")
test_results: List[TestResult] = []
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

result_section.table(test_results_dataframe)

for index, resource in enumerate(app_resources):
    progress = int(float(100 * index) / float(tests_count))
    test_run_progress.progress(progress)
    test_current_file_url.markdown(f"Current File: [{resource.url}](resource.ulr)")

    test_result = get_test_result(resource)
    test_results.append(test_result)
    # resource_filter = test_results_dataframe["test"] == resource.name
    # test_results_dataframe[resource_filter]["result"] = test_result.passed
    test_results_dataframe = test_results_dataframe.set_index("test")
    test_results_dataframe = test_results_dataframe.set_value(
        resource.name, "result", test_result.result_str
    )
    test_results_dataframe = test_results_dataframe.set_value(
        resource.name, "exception", str(test_result.exception)
    )
    # test_results_dataframe = test_results_dataframe.sort_values("exception")
    test_results_dataframe = test_results_dataframe.reset_index("test")
    result_section.table(test_results_dataframe)

    if not test_result.result:
        log += f"------ {test_result.resource.name} ---------\n\n"
        log += f"File: {test_result.resource.url}\n\n"
        log += f"{test_result.traceback}\n\n"
    result_exception_section.text(log)

test_results_dataframe = (
    test_results_dataframe.sort_values("test")
    .sort_values("author")
    .sort_values("result")
    .reset_index(drop=True)
)
result_section.table(test_results_dataframe)

passed_count = sum([test_result.result for test_result in test_results])
failed_count = tests_count - passed_count
test_current_file_url.text("")
test_run_progress.info(
    f"All tests have run: {failed_count} failed, {passed_count} passed."
)
