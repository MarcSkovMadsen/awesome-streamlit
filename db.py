"""Simple 'database' of models

Here you maintain the list of awesome resources
"""
from src.shared.models import Resource, Tag

CODE = Tag("Code")
APP = Tag("Apps")
PAGE = Tag(name="App included here")
STREAMLITIO = Tag(name="Streamlit.io")
THEBEGINNING = Tag(name="The beginning")
SOCIAL = Tag(name="Social")
TECHNICAL = Tag(name="Technical")
ALTERNATIVE = Tag(name="Alternatives")

# Please note that in the README.md resources will be listed
# under the first tag in the tags list only
RESOURCES = [
    Resource(name="Streamlit.io", url="https://streamlit.io/", tags=[STREAMLITIO]),
    Resource(
        name="Streamlit Docs", url="https://streamlit.io/docs/", tags=[STREAMLITIO]
    ),
    Resource(
        name="Streamlit Community",
        url="https://discuss.streamlit.io/top/quarterly",
        tags=[STREAMLITIO],
    ),
    Resource(
        "The announcing blog",
        url="https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace",
        tags=[STREAMLITIO, THEBEGINNING],
    ),
    Resource(
        "The announcing community post",
        url="https://discuss.streamlit.io/t/streamlit-has-launched/105/3",
        tags=[STREAMLITIO, THEBEGINNING],
    ),
    Resource(
        "LinkedIn post that started awesome-streamlit.org",
        url="https://www.linkedin.com/feed/update/urn:li:activity:6586497522896818176",
        tags=[THEBEGINNING, SOCIAL],
    ),
    Resource(
        "LinkedIn #streamlit",
        url="https://www.linkedin.com/search/results/all/?keywords=%23streamlit",
        tags=[SOCIAL],
    ),
    Resource(
        name="Twitter #streamlit",
        url="https://twitter.com/search?q=%23streamlit&src=typed_query",
        tags=[SOCIAL],
    ),
    ### Awesome Applications
    Resource(
        name="SpacyIO Application",
        url="https://gist.github.com/ines/b320cb8441b590eedf19137599ce6685",
        tags=[APP, PAGE],
    ),
    Resource(
        name="Kaggle Mushrooms Dashboard",
        url="https://github.com/pierpaolo28/Data-Visualization/tree/master/Streamlit",
        tags=[APP],
    ),
    Resource(
        name="Hacker News technical discussion of how Streamlit work",
        url="https://news.ycombinator.com/item?id=21158487",
        tags=[TECHNICAL],
    ),
    Resource(
        name="Jupyter Voila",
        url="https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93",
        tags=[ALTERNATIVE],
    ),
    Resource(name="Plotly Dash", url="https://plot.ly/dash/", tags=[ALTERNATIVE]),
    Resource(
        name="Bokeh",
        url="https://bokeh.pydata.org/en/latest/index.html",
        tags=[ALTERNATIVE],
    ),
    Resource(
        name="Sentiment Analyzer Tool",
        url=(
            "https://www.linkedin.com/posts/patidarparas13_code-ml-machinelearning-"
            "ugcPost-6585745929062703104-ttkv"
        ),
        tags=[APP, CODE, SOCIAL],
    ),
]

TAGS = []
for resource in RESOURCES:
    for tag in resource.tags:
        TAGS.append(tag)
TAGS = sorted(list(set(TAGS)))
