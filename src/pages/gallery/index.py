"""The Gallery index page is used to navigate between examples

Very much inspired by:
Author: [Nhan Nguyen](https://github.com/virusvn)
Source: https://github.com/virusvn/streamlit-components-demo/blob/master/app.py

Credits to Nhan for sharing that code
"""
import logging
from typing import List

import streamlit as st

import awesome_streamlit as ast

# Get an instance of a logger
logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)

JSON_URL = """https://raw.githubusercontent.com/virusvn/streamlit-components-demo/
master/streamlit_apps.json"""


def write():
    """This method writes the Gallery index page which is used to navigate between gallery apps"""
    ast.shared.components.title_awesome("Gallery")
    apps = get_apps()

    st.sidebar.title("Gallery")
    is_awesome = st.sidebar.checkbox("Awesome apps only", True)
    show_source_code = st.sidebar.checkbox("Show Source Code", True)
    if is_awesome:
        apps = ast.core.services.resources.filter_by_is_awesome(apps)

    tags = st.multiselect("Select Tag(s)", get_tags(apps))
    apps = ast.core.services.resources.filter_by_tags(apps, tags)

    authors = get_authors(apps)
    author_all = ast.shared.models.Author(name="All", url="")
    authors = [author_all] + authors
    author = st.selectbox("Select Author", authors)

    if author != author_all:
        apps = get_apps_by_author(apps, author)

    app_index = 0
    if author == ast.database.apps_in_gallery.DEFAULT_APP_IN_GALLERY.author:
        if ast.database.apps_in_gallery.DEFAULT_APP_IN_GALLERY in apps:
            app_index = apps.index(ast.database.apps_in_gallery.DEFAULT_APP_IN_GALLERY)

    apps = ast.core.services.resources.sort_resources(apps)
    run_app = st.selectbox("Select the App", apps, index=app_index)
    app_credits = st.empty()

    app_credits.markdown(
        f"""Resources: [Author]({run_app.author.url}), [App Code]({run_app.url})"""
    )

    # Fetch the content
    python_code = ast.core.services.other.get_file_content_as_string(run_app.url)

    # Run the child app
    if python_code is not None:
        try:
            with st.spinner(f"Loading {run_app.name} ..."):
                exec(python_code, globals())  # pylint: disable=exec-used
        except Exception as exception:  # pylint: disable=broad-except
            st.write("Error occurred when executing [{0}]".format(run_app))
            st.error(str(exception))
            logging.error(exception)

        if show_source_code:
            st.header("Source code")
            st.code(python_code)


def get_apps() -> List[ast.shared.models.Resource]:
    """The list of resources

    Returns:
        List[ast.shared.models.Resource] -- The list of resources
    """
    return [
        resource
        for resource in ast.database.RESOURCES
        if ast.database.tags.APP_IN_GALLERY in resource.tags
    ]


def get_tags(
    resources: List[ast.shared.models.Resource]
) -> List[ast.shared.models.Tag]:
    """The list of Tags

    Returns:
        List[ast.shared.models.Resource] -- The list of Tags
    """
    tags = set()
    for resource in resources:
        for tag in resource.tags:
            tags.add(tag)
    return sorted(list(tags), key=lambda x: x.name)


@st.cache
def get_authors(
    resources: List[ast.shared.models.Resource]
) -> List[ast.shared.models.Author]:
    """The list of Authors of the specified resources

    The list is sorted by Author.name

    Arguments:
        resources {List[ast.shared.models.Resource]} -- A list of Resources
        tags {List[ast.shared.models.Resource]} -- A list of Tags

    Returns:
        List[ast.shared.models.Author] -- [description]
    """
    authors = list({resource.author for resource in resources if resource.author})
    return sorted(authors, key=lambda x: x.name)


@st.cache
def get_apps_by_author(
    resources: List[ast.shared.models.Resource], author: ast.shared.models.Author
) -> List[ast.shared.models.Resource]:
    """The Resources by the specified Author

    Arguments:
        resources {List[ast.shared.models.Resource]} -- A list of resources
        author {ast.shared.models.Author} -- A list of authors

    Returns:
        List[ast.shared.models.Resource] -- [description]
    """
    resources = [resource for resource in resources if resource.author == author]
    return sorted(resources, key=lambda x: x.name)


if __name__ == "__main__":
    write()
