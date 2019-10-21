"""The purpose of this app is to test that the list of resources can be executed be Streamlit"""
# pylint: disable=invalid-name
from typing import Callable, List

from awesome_streamlit.shared.components import title_awesome
from awesome_streamlit.testing import components
from awesome_streamlit.testing.models import TesTItem


def write(test_items_collector: Callable[..., List[TesTItem]]):
    """The main section of the test runner"""
    title_awesome("Test Runner")
    components.intro_section()
    test_items = components.test_collection_section(
        test_items_collector=test_items_collector
    )
    components.test_run_section(test_items)
