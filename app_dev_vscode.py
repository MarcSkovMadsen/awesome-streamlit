"""Use this module for development with VS Code and the integrated debugger"""
import ptvsd
import streamlit as st

import app

# pylint: disable=invalid-name
markdown = st.markdown(
    """
## Ready to attach the VS Code Debugger!

![Python: Remote Attach](https://awesome-streamlit.readthedocs.io/en/latest/_images/vscode_python_remote_attach.png)

for more info see the [VS Code section at awesome-streamlit.readthedocs.io]
(https://awesome-streamlit.readthedocs.io/en/latest/vscode.html#integrated-debugging)
"""
)


ptvsd.enable_attach(address=("localhost", 5678))
ptvsd.wait_for_attach()

markdown.empty()

app.main()
