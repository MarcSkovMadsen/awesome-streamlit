"""Gallery page used to navigate between examples

Very much inspired by:
Author: [Nhan Nguyen](https://github.com/virusvn)
Source: https://github.com/virusvn/streamlit-components-demo/blob/master/app.py

Thanks
"""
import json
import logging
import urllib.request
from typing import Dict, List

import streamlit as st

# Get an instance of a logger
logger = logging.getLogger(__name__)

JSON_URL = "https://raw.githubusercontent.com/virusvn/streamlit-components-demo/master/streamlit_apps.json"


def write():
    author = st.sidebar.selectbox("Select Author", ["Streamlit"])

    components()


def components():

    apps = get_apps(JSON_URL)  # type: Dict[str, str]
    logger.info(apps)
    app_names = []

    for name, _ in apps.items():
        app_names.append(name)

    run_app = st.sidebar.selectbox("Select the app", app_names)
    show_source_code = st.sidebar.checkbox("Show Source Code", True)

    # Fetch the content
    python_code = get_file_content_as_string(apps[run_app])

    # Run the child app
    if python_code is not None:
        try:
            st.header("App")
            exec(python_code)
            st.header("Source code")
            st.markdown("Author: []()")
            st.markdown("Source: []()")
            st.code(python_code)
        except Exception as e:
            st.write("Error occurred when executing [{0}]".format(run_app))
            st.error(str(e))
            logger.error(e)


@st.cache
def get_apps(url: str) -> Dict[str, str]:
    json_obj = fetch_json(url)
    apps = {}
    for item in json_obj:
        if item["url"] is not None and item["url"].endswith(".py"):
            # can overwrite if same name
            apps[item["name"]] = item["url"]

    return apps


@st.cache
def fetch_json(url: str):
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    return output


@st.cache
def get_file_content_as_string(url: str):
    data = urllib.request.urlopen(url).read()
    return data.decode("utf-8")


if __name__ == "__main__":
    write()
