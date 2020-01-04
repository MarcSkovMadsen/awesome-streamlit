"""
This file implements a function you can use to make Streamlit output more Notebook like

The functionally was developed by [David Chudzicki](https://github.com/dchudz). See

- [Announcement]\
(https://discuss.streamlit.io/t/implementation-of-end-code-block-using-streamlit-for-notebook/1505)
- [Repo](https://github.com/dchudz/streamlit_end_code_block)

Here we have modified it for inclusion in the gallery at awesome-streamlit.org.
"""
import sys
import traceback

import pandas as pd
import streamlit as st
from streamlit.source_util import open_python_file

_CURRENT_END_LINE = 0
_SPACE_FOR_CODE = st.empty()

assert sys.version_info >= (3, 4)


def awesome_streamlit_hack(filename: str) -> str:
    """We need this when running this file via the 'exec' statement as a part of the
    awesome-streamlit.org gallery"""
    if filename == "<string>":
        return "gallery/notebook_style/notebook_style.py"

    return filename


def end_code_block(display=True):
    """Ends the current code block and sends it to streamlit output.

    Keyword Arguments:
        display: whether to show this code block in the output
    """
    global _CURRENT_END_LINE  # pylint: disable=global-statement
    global _SPACE_FOR_CODE  # pylint: disable=global-statement
    frame = traceback.extract_stack()[-2]  # stack[-1] would be this frame itself
    # stack[-2] is the frame in the user's "notebook" calling us
    # (as long as the user is calling us directly)
    filename, lineno = frame.filename, frame.lineno
    filename = awesome_streamlit_hack(filename)
    with open_python_file(filename) as source_file:
        source_lines = source_file.readlines()
    # `lineno-1` means we skip showing the call to us
    lines_to_display = source_lines[_CURRENT_END_LINE : (lineno - 1)]
    _CURRENT_END_LINE = lineno
    if display:
        _SPACE_FOR_CODE.code("".join(lines_to_display), "python")
    _SPACE_FOR_CODE = st.empty()


_____ = end_code_block


def example():
    """An example of the use of end_code_block"""
    _____(display=False)
    message = "hello world"
    st.write(message)
    _____()

    dataframe = pd.DataFrame({"x": [1, 2], "y": [2, 3]})
    st.write(dataframe)  # pylint: disable=pointless-statement
    _____()

    st.write("bye")
    _____()


st.write(__doc__)
example()
