"""The Gallery index page is used to navigate between examples

Very much inspired by:
Author: [Nhan Nguyen](https://github.com/virusvn)
Source: https://github.com/virusvn/streamlit-components-demo/blob/master/app.py

Credits to Nhan for sharing that code
"""
import json
import logging
import urllib.request
from typing import Dict

import streamlit as st

import db
import src.st_awesome
import src.st_extensions
from typing import List
import src.shared.models

# Get an instance of a logger
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

JSON_URL = "https://raw.githubusercontent.com/virusvn/streamlit-components-demo/master/streamlit_apps.json"


def write():
    """This method writes the Gallery index page which is used to navigate between gallery apps"""
    src.st_awesome.title("Gallery")
    with st.spinner("Loading Gallery ..."):
        apps = get_resources()
        authors = get_authors(apps)
    index_default_author = authors.index(db.DEFAULT_RESOURCE.author)
    author = st.selectbox("Select Author", authors, index=index_default_author)
    apps_by_author = get_resources_by_author(apps, author)
    if author == db.DEFAULT_RESOURCE.author:
        app_index = apps_by_author.index(db.DEFAULT_RESOURCE)
    else:
        app_index = 0
    run_app = st.selectbox("Select the app", apps_by_author, index=app_index)
    app_credits = st.empty()

    app_credits.markdown(
        f"""Resources: [{author.name}]({run_app.author.url}), [Source Code]({run_app.url})"""
    )
    st.sidebar.title("Gallery")
    show_source_code = st.sidebar.checkbox("Show Source Code", True)

    # Fetch the content
    python_code = get_file_content_as_string(run_app.url)

    # Run the child app
    if python_code is not None:
        try:
            with st.spinner(f"Loading {run_app.name} ..."):
                exec(python_code, globals())  # pylint: disable=exec-used
        except Exception as exception:
            st.write("Error occurred when executing [{0}]".format(run_app))
            st.error(str(exception))
            logging.error(exception)

        if show_source_code:
            st.header("Source code")
            st.code(python_code)


@st.cache
def get_resources() -> List[src.shared.models.Resource]:
    """The list of resources

    Returns:
        List[src.shared.models.Resource] -- The list of resources
    """
    return [resource for resource in db.RESOURCES if db.APP_IN_GALLERY in resource.tags]


@st.cache
def get_authors(
    resources: List[src.shared.models.Resource]
) -> List[src.shared.models.Author]:
    """The list of Authors of the specified resources

    The list is sorted by Author.name

    Arguments:
        resources {List[src.shared.models.Resource]} -- A list of Resources

    Returns:
        List[src.shared.models.Author] -- [description]
    """
    author_set = {resource.author for resource in resources if resource.author}
    return sorted(list(author_set), key=lambda x: x.name)


@st.cache
def get_resources_by_author(
    resources: List[src.shared.models.Resource], author: src.shared.models.Author
) -> List[src.shared.models.Resource]:
    """The Resources by the specified Author

    Arguments:
        resources {List[src.shared.models.Resource]} -- A list of resources
        author {src.shared.models.Author} -- A list of authors

    Returns:
        List[src.shared.models.Resource] -- [description]
    """
    return [resource for resource in resources if resource.author == author]


@st.cache
def get_file_content_as_string(url: str) -> str:
    """The url content as a string

    Arguments:
        url {str} -- The url to request

    Returns:
        str -- The text of the url
    """
    data = urllib.request.urlopen(url).read()
    return data.decode("utf-8")


if __name__ == "__main__":
    write()
