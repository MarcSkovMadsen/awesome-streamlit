"""
## Awesome Data Explorer

This app explores data in the Awesome Public Datasets repository.

Author: [Ali Avni Cirik](https://www.linkedin.com/in/aliavnicirik)\n
Source: [Github](https://github.com/aliavni/awesome-data-explorer)
"""
from pathlib import Path
from typing import Dict, Tuple, Union

import altair as alt
import git
import pandas as pd
import requests
import streamlit as st
import yaml

CORRECTIONS = {
    "DOI: ": "DOI ",
    "see: ": "see ",
    "from: ": "from ",
    "tables: ": "tables ",
    "1981â€“2016": "1981-2016",
}

@st.cache
def get_awesome_data_repo():
    """Clones the data catalogue"""
    try:
        git.Git(".").clone("https://github.com/awesomedata/apd-core")
    except git.GitCommandError:
        repo = git.Repo("apd-core")
        repo.remotes.origin.pull()


@st.cache
def get_categories_and_file_names() -> Dict:
    """Returns a dictionary of categories and files

    Returns
    -------
    Dict
        Key is the name of the category, value is a dictionary with information on files in that \
        category
    """
    path = Path("apd-core/core")
    category_files: Dict = {}
    for i in path.glob("**/*"):
        if i.is_dir():
            continue

        category, file_name = i.parts[-2:]

        file = Path("apd-core/core") / category / file_name
        # print(file)
        try:
            with file.open() as open_file:
                open_file_content = open_file.read()
                for old, new in CORRECTIONS.items():
                    open_file_content = open_file_content.replace(old, new)
                data_info = yaml.load(open_file_content, Loader=yaml.FullLoader)

            if category in category_files:
                category_files[category][file_name] = data_info
            else:
                category_files[category] = {file_name: data_info}
        except UnicodeDecodeError as err:
            category_files[category][file_name] = "NOT READABLE"
            # logging.exception("Error. Could not read %s", file.name, exc_info=err)

    return category_files


def get_data_info(category: str, file_name: str) -> Dict:
    """Returns a dictionary of information on the specified file

    Parameters
    ----------
    category : str
        The name of the category, like 'Sports'
    file_name : str
        A name of a file

    Returns
    -------
    Dict
        Information on the file
    """
    path = Path("apd-core/core") / category / file_name

    with path.open() as open_file:
        data = yaml.load(open_file.read(), Loader=yaml.FullLoader)
    return data


def create_info_table(selected_data_info: Dict):
    """Writes the information to the table

    Parameters
    ----------
    selected_data_info : Dict
        The information to show
    """
    info_table = pd.DataFrame()

    data_description = selected_data_info["description"]
    if data_description:
        line = pd.Series(data_description)
        line.name = "Description"
        info_table = info_table.append(line)

    keywords = selected_data_info["keywords"]
    if keywords:
        keywords = ", ".join(keywords.lower().split(","))
        line = pd.Series(keywords)
        line.name = "Keywords"
        info_table = info_table.append(line)

    if len(info_table) > 0:
        info_table.columns = [""]
        st.table(info_table)


@st.cache()
def check_url(url: str) -> Tuple[bool, Union[str, requests.Response]]:
    """Returns information on the availability of the url

    Parameters
    ----------
    url : str
        The url to test

    Returns
    -------
    Tuple[bool, Union[str, Response]]
        Whether the url is available and a string reponse
    """
    try:
        response = requests.head(url, allow_redirects=False)
        return True, response
    except requests.exceptions.SSLError:
        return False, "SSL error"
    except requests.exceptions.ConnectionError:
        return False, "Connection error"
    except requests.exceptions.InvalidSchema:
        return False, "Invalid schema"
    except requests.exceptions.MissingSchema:
        return check_url("https://" + url)


def show_homepage(data_info):
    """Shows information on the availability of the url to the user"""
    homepage = data_info["homepage"]

    if homepage.startswith("http:"):
        homepage = homepage.replace("http:", "https:")

    url_status, response = check_url(homepage)

    if url_status:
        if response.status_code in [301, 302]:
            st.info(f"{homepage}\n\nRedirects to {response.headers['Location']}")
        else:
            st.success(f"{homepage}")
    else:
        if response == "Connection error":
            st.error(f"{homepage}\n\nThere is a connection issue to this website.")
        elif response == "SSL error":
            st.warning(f"There might be an SSL issue with {homepage}\n\nProceed with caution!")
        else:
            st.info(f"{homepage}")


def main():
    """Run this to run the programme"""
    st.title("Awesome Data Explorer")
    st.markdown("This app explores data in the Awesome Public Datasets repository.")

    title = st.empty()

    get_awesome_data_repo()

    categories_and_files = get_categories_and_file_names()

    category_file_count = {k: f"{k} ({len(v)})" for k, v in categories_and_files.items()}
    selected_topic = st.sidebar.selectbox(
        "Select topic",
        options=sorted(categories_and_files.keys()),
        format_func=category_file_count.get,
    )

    category_data = categories_and_files[selected_topic]

    data_titles = {k: v.get("title") for k, v in category_data.items()}

    selected_data = st.sidebar.selectbox(
        "Select data", options=sorted(category_data.keys()), format_func=data_titles.get
    )

    show_data_count_by_topic = st.sidebar.checkbox("Show data count by topic", value=True)

    selected_data_info = category_data[selected_data]

    title.title(selected_data_info["title"])
    data_image = selected_data_info.get("image", None)
    if data_image and data_image != "none":
        st.image(data_image, width=200)

    create_info_table(selected_data_info)

    show_homepage(selected_data_info)

    if show_data_count_by_topic:
        st.title(body="Data count by topic")
        source = pd.DataFrame(
            {
                "Topic": list(categories_and_files.keys()),
                "Number of data": [len(i) for i in categories_and_files.values()],
            }
        )

        chart = (
            alt.Chart(source)
            .mark_bar()
            .encode(alt.Y("Topic", title=""), alt.X("Number of data", title=""))
            .properties(height=600)
        )

        text = chart.mark_text(align="left", baseline="middle", dx=3).encode(text="Number of data")

        st.altair_chart(chart + text)

    st.sidebar.title("About")
    st.sidebar.info(
        "This app shows available data in [Awesome Public Datasets]"
        "(https://github.com/awesomedata/awesome-public-datasets) repository.\n\n"
        "It is maintained by [Ali](https://www.linkedin.com/in/aliavnicirik/). "
        "Check the code at https://github.com/aliavni/awesome-data-explorer"
    )


main()
