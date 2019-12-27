"""Streamlit v. 0.52 ships with a first version of a **file uploader** widget. You can find the
**documentation**
[here](https://streamlit.io/docs/api.html?highlight=file%20upload#streamlit.file_uploader).

For reference I've implemented an example of file upload here. It's available in the gallery at
[awesome-streamlit.org](https://awesome-streamlit.org).
"""
from enum import Enum
from io import BytesIO, StringIO
from typing import Union

import pandas as pd
import streamlit as st

STYLE = """
<style>
img {
    max-width: 100%;
}
</style>
"""

FILE_TYPES = ["csv", "py", "png", "jpg"]


class FileType(Enum):
    """Used to distinguish between file types"""

    IMAGE = "Image"
    CSV = "csv"
    PYTHON = "Python"


def get_file_type(file: Union[BytesIO, StringIO]) -> FileType:
    """The file uploader widget does not provide information on the type of file uploaded so we have
    to guess using rules or ML. See
    [Issue 896](https://github.com/streamlit/streamlit/issues/896)

    I've implemented rules for now :-)

    Arguments:
        file {Union[BytesIO, StringIO]} -- The file uploaded

    Returns:
        FileType -- A best guess of the file type
    """

    if isinstance(file, BytesIO):
        return FileType.IMAGE
    content = file.getvalue()
    if (
        content.startswith('"""')
        or "import" in content
        or "from " in content
        or "def " in content
        or "class " in content
        or "print(" in content
    ):
        return FileType.PYTHON

    return FileType.CSV


def main():
    """Run this function to display the Streamlit app"""
    st.info(__doc__)
    st.markdown(STYLE, unsafe_allow_html=True)

    file = st.file_uploader("Upload file", type=FILE_TYPES)
    show_file = st.empty()
    if not file:
        show_file.info("Please upload a file of type: " + ", ".join(FILE_TYPES))
        return

    file_type = get_file_type(file)
    if file_type == FileType.IMAGE:
        show_file.image(file)
    elif file_type == FileType.PYTHON:
        st.code(file.getvalue())
    else:
        data = pd.read_csv(file)
        st.dataframe(data.head(10))

    file.close()


main()
