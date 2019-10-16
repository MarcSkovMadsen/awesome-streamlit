"""Utils needed for testing of Streamlit applications"""
from types import ModuleType
from typing import List, Tuple

ATTRS_NOT_TO_SEARCH = [
    "@py_builtins",
    "@pytest_ar",
    "__builtins__",
    "__cached__",
    "__doc__",
    "__file__",
    "__loader__",
    "__name__",
    "__package__",
    "__spec__",
]


def collect_test_sub_modules(
    parent: ModuleType, startswith: str = "test_"
) -> List[ModuleType]:
    """A list of sub modules with names that starts with starts_with

    Does NOT include the parent

    Arguments:
        module {ModuleType} -- The parent module from which to start

    Keyword Arguments:
        startswith {str} -- The module should start with this (default: {"test_"})

    Returns:
        List[ModuleType] -- A list of the submodules that starts with starts_with.
    """
    test_modules: List[ModuleType] = []

    for item in dir(parent):
        if item not in ATTRS_NOT_TO_SEARCH:
            child = getattr(parent, item)
            if isinstance(child, ModuleType):
                child_name = child.__name__.split(".")[-1]
                if child_name.startswith(startswith):
                    test_modules.append(child)
                test_modules += collect_test_sub_modules(child)

    return test_modules


def collect_test_functions(
    module, module_startswith: str = "test_", function_startswith: str = "test_st_"
) -> List[Tuple[ModuleType, str]]:
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
    module_name = module.__name__.split(".")[-1]
    # Collect functions in current module
    if module_name.startswith(module_startswith):
        test_functions = [
            (module, item)
            for item in dir(module)
            if item.startswith(function_startswith) and callable(getattr(module, item))
        ]
    else:
        test_functions = []

    # Collect functions in sub modules
    for sub_module in collect_test_sub_modules(module, startswith=module_startswith):
        test_functions += collect_test_functions(
            sub_module,
            module_startswith=module_startswith,
            function_startswith=function_startswith,
        )

    return test_functions


def load_module_from_path(path: str) -> ModuleType:
    """Loads a module from the specified path

    Arguments:
        path {str} -- The full path to the module

    Returns:
        ModuleType -- The module at the specified path
    """
    raise NotImplementedError()
