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
import src.st_awesome
import streamlit as st
import db

# Get an instance of a logger
logger = logging.getLogger(__name__)

JSON_URL = "https://raw.githubusercontent.com/virusvn/streamlit-components-demo/master/streamlit_apps.json"


@st.cache
def get_resources():
    return [resource for resource in db.RESOURCES if db.INGALLERY in resource.tags]


@st.cache
def get_authors(resources):
    return list({resource.author for resource in resources if resource.author})


@st.cache
def get_apps_by_author(apps, author):
    return [app for app in apps if app.author == author]


def write():
    src.st_awesome.title("Gallery")
    app_credits = st.empty()

    with st.spinner("Loading Gallery ..."):
        apps = get_resources()
        authors = get_authors(apps)

    author = st.sidebar.selectbox("Select Author", authors)
    apps_by_author = get_apps_by_author(apps, author)
    run_app = st.sidebar.selectbox("Select the app", apps_by_author)
    app_credits.markdown(
        f"""
            Author: [{run_app.author.name}]({run_app.author.url})

            Source: [url]({run_app.url})
            """
    )

    show_source_code = st.sidebar.checkbox("Show Source Code", True)

    # Fetch the content
    python_code = get_file_content_as_string(run_app.url)

    # Run the child app
    if python_code is not None:
        try:
            st.header("App")
            with st.spinner("Loading ..."):
                exec(python_code, globals())
            st.header("Source code")
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
