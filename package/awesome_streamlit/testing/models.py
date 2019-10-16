"""Models related to testing"""
import inspect
from typing import Optional, Callable
from types import ModuleType
from awesome_streamlit.shared.models import Resource
from awesome_streamlit.core.services import get_file_content_as_string


class TestItem:
    """Model of a TestItem"""

    def __init__(  # pylint: disable=too-many-arguments
        self,
        name: str,
        location: str,
        python_code: Optional[str] = None,
        test_function: Optional[Callable] = None,
        exception: Optional[Exception] = None,
        traceback: str = "",
    ):
        self.name = name
        self.location = location
        self.python_code = python_code
        self.test_function = test_function
        self.exception = exception
        self.traceback = traceback

    @property
    def result(self) -> bool:
        """True if no exception. False otherwise"""
        if self.exception:
            return False
        return True

    @property
    def result_str(self) -> str:
        """'passed' if no exception. 'failed' otherwise"""
        if self.exception:
            return "failed"
        return "passed"

    @classmethod
    def create_from_app_file_resource(cls, resource: Resource) -> "TestItem":
        """Creates a TestItem from a Resource"""
        python_code = get_file_content_as_string(resource.url)

        return cls(name=resource.name, location=resource.url, python_code=python_code)

    @classmethod
    def create_from_test_function(cls, module: ModuleType, function: str) -> "TestItem":
        """Creates a test_function from a module function

        Arguments:
            module {ModuleType} -- The module
            function {str} -- The function string

        Returns:
            [TestItem] -- A TestItem
        """
        test_function = getattr(module, function)
        python_code = inspect.getsource(test_function)
        return cls(
            name=function,
            location=f"{module.__name__}::{function}",
            test_function=test_function,
            python_code=python_code,
        )
