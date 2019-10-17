"""Models related to testing"""
import traceback as traceback_module
from types import ModuleType
from typing import Callable, Optional

from awesome_streamlit.core.services import get_file_content_as_string
from awesome_streamlit.shared.models import Resource


class TesTItem:
    """Model of a TesTItem

    This class has been partially capitalized in order not to be collected by PyTest,
    that normally collects classes starting with 'Test'.
    """

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
    def create_from_app_file_resource(cls, resource: Resource) -> "TesTItem":
        """Creates a TesTItem from a Resource"""
        # python_code = get_file_content_as_string(resource.url)

        return cls(name=resource.name, location=resource.url)

    @classmethod
    def create_from_test_function(cls, module: ModuleType, function: str) -> "TesTItem":
        """Creates a test_function from a module function

        Arguments:
            module {ModuleType} -- The module
            function {str} -- The function string

        Returns:
            [TesTItem] -- A TesTItem
        """
        test_function = getattr(module, function)
        # python_code = inspect.getsource(test_function)
        return cls(
            name=function,
            location=f"{module.__name__}::{function}",
            test_function=test_function,
        )

    def run_test(self):
        """Runs the TesTItem"""
        if self.test_function:
            raise NotImplementedError()

        self.exception = None
        self.traceback = ""

        try:
            self.python_code = get_file_content_as_string(self.location)
            exec(self.python_code, globals())  # pylint: disable=exec-used
        except Exception as exception:  # pylint: disable=broad-except
            self.traceback = traceback_module.format_exc()
            self.exception = exception
