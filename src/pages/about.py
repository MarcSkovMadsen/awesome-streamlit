"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading About ..."):
        ast.shared.components.title_awesome(" - About")
        st.markdown(
            """## Contributions

This an open source project and you are very welcome to **contribute** your awesome
comments, questions, resources and apps as
[issues](https://github.com/MarcSkovMadsen/awesome-streamlit/issues) or
[pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls)
to the [source code](https://github.com/MarcSkovMadsen/awesome-streamlit).

For more details see the [Contribute](https://github.com/marcskovmadsen/awesome-streamlit#contribute) section of the README file.

## The Developer

This project is developed by Marc Skov Madsen. You can learn more about me at
[datamodelsanalytics.com](https://datamodelsanalytics.com).

Feel free to reach out if you wan't to join the project as a developer. You can find my contact details at [datamodelsanalytics.com](https://datamodelsanalytics.com).

[<img src="https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/assets/images/datamodelsanalytics.png?raw=true" style="max-width: 700px">](https://datamodelsanalytics.com)
""",
            unsafe_allow_html=True,
        )
