"""Models related to testing"""
from typing import NamedTuple, Optional
from awesome_streamlit.shared.models import Resource


class TestResult(NamedTuple):
    """Model of a TestResult"""

    resource: Resource
    python_code: str
    exception: Optional[Exception] = None
    traceback: str = ""

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
