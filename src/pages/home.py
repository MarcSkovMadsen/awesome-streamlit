import streamlit as st
import pages.awesome_streamlit_vision
import pages.awesome_streamlit_readme
import importlib


def write():
    st.write(
        """
We believe that [Streamlit](https://streamlit.io/) is truly awesome.

Streamlit is [announced](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace) as being **The fastest way to build custom Machine Learning tools** but we believe it has the potential to become much more awesome than that.

We believe Streamlit has the **potential to become the Iphone of Data Science, Technical Writing, Web Apps, Code, Python and more**.

The purpose of this application is to

- Share list of awesome Streamlit resources
- Share a vision on how awesome Streamlit can be
- Provide awesome Streamlit examples (See side bar on the left).
"""
    )
    if st.checkbox("Show Resources:"):
        importlib.reload(pages.awesome_streamlit_readme)
        pages.awesome_streamlit_readme.write()
    if st.checkbox("Show Vision:"):
        importlib.reload(pages.awesome_streamlit_vision)
        pages.awesome_streamlit_vision.write()
    else:
        st.write(
            """[![Streamlit Video](https://miro.medium.com/max/700/1*p3XPm-x0TUIuMmQQa4mjHQ.gif)](https://miro.medium.com/max/700/1*p3XPm-x0TUIuMmQQa4mjHQ.gif)"""
        )

