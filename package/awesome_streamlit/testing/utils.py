"""Utils needed for testing of Streamlit applications"""
from typing import List, Callable


def collect_tests_in_module(
    module, module_startswith: str = "test_", function_startswith: str = "test_st_"
) -> List[Callable]:
    """A list of Streamlit Test Functions that satisfies

    - Belonging to a file in the specified module or one of its submodules
    - The file starts with file_startswith
    - The function starts with function starts_with

    Arguments:
        module {str} -- Only collect from this module and below

    Keyword Arguments:
        file_startswith {str} -- Only collect from these files (default: {"test_"})
        function_startswith {str} -- Only collect these functions (default: {"test_st_"})

    Returns:
        List[Callable[[],[]] -- A list of Streamlit Test Functions
    """
    raise NotImplementedError()
