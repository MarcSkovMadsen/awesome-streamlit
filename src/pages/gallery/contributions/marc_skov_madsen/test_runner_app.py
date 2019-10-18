"""The purpose of this app is to test that the list of resources can be executed be Streamlit"""
# pylint: disable=invalid-name
from typing import List
import awesome_streamlit as ast


def test_items_collector() -> List[ast.testing.models.TesTItem]:
    """The TesTItems to be tested

    Returns:
        List[testing.models.TesTItem] -- The TesTItems to be tested
    """
    return ast.testing.services.test_item.get_from_resources()


ast.testing.test_runner_app.write(test_items_collector=test_items_collector)
