"""The purpose of this app is to test that the list of resources can be executed be Streamlit"""
# pylint: disable=invalid-name
from typing import List

import streamlit as st

import awesome_streamlit as ast
from awesome_streamlit.database.apps_in_gallery import GITHUB_RAW_GALLERY_URL
from awesome_streamlit.testing.models import \
    TesTItem  # Special Capitalization is due to PyTest

st.markdown(
    """# Important Notes

This app requires the Awesome Streamlit package.
The Awesome Streamlit package can be installed using

`pip install awesome-streamlit`
"""
)
st.info(
    """**Click a button below to start testing** a Test Suite or
study the **test_runner_app source code** below."""
)

simple = st.button("Single File")
advanced = st.button("The Awesome Streamlit Gallery")

if simple or advanced:
    if simple:

        def test_items_collector() -> List[TesTItem]:
            """A function to collect a list of test items based on a set of hardcode testitems"""
            return [
                TesTItem(
                    name="Spreadsheet",
                    location=GITHUB_RAW_GALLERY_URL + "spreadsheet/spreadsheet.py",
                )
            ]

    else:

        def test_items_collector() -> List[TesTItem]:
            """A function to collect a list of test items based a items in this gallery"""
            return [
                test_item
                for test_item in ast.testing.services.test_item.get_from_resources()
                if test_item.name != "Awesome Streamlit Test Runner"
            ]

    ast.testing.test_runner_app.write(test_items_collector=test_items_collector)
    simple = False
    advanced = False
else:
    location = GITHUB_RAW_GALLERY_URL + "test_runner_app/test_runner_app.py"
    # Todo: Get code from local file instead of url to make sure it's always updated
    python_code = ast.core.services.other.get_file_content_as_string(location)
    st.markdown("### Source Code")
    st.code(python_code)
