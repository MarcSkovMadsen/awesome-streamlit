"""Simple 'database' of models

Here you maintain the list of awesome resources
"""
from src.shared.models import Author, Resource, Tag

# Tags
ALTERNATIVE = Tag(name="Alternatives")
APP = Tag("Apps")
CODE = Tag("Code")
DEPLOYMENT = Tag(name="Deployment")
PAGE = Tag(name="App included here")
SOCIAL = Tag(name="Social")
STREAMLITIO = Tag(name="Streamlit.io")
TECHNICAL = Tag(name="Technical")
AWESOMESTREAMLIT = Tag(name="The beginning")
INGALLERY = Tag(name="Included in Awesome Streamlit Gallery")

# Authors
STREAMLIT = Author(name="Streamlit", url="https://streamlit.io/")
AWESOME_STREAMLIT = Author(
    name="Awsome-Streamlit", url="https://github.com/marcskovmadsen/awesome-streamlit"
)

# Please note that in the README.md resources will be listed
# under the first tag in the tags list only
AUTHORS = [
    Author(name="Streamlit", url="https://streamlit.io/"),
    Author(
        name="Awsome-Streamlit",
        url="https://github.com/marcskovmadsen/awesome-streamlit",
    ),
]

RESOURCES = [
    Resource(
        name="Streamlit.io",
        url="https://streamlit.io/",
        tags=[STREAMLITIO],
        is_awesome=True,
    ),
    Resource(
        name="Streamlit Docs",
        url="https://streamlit.io/docs/",
        tags=[STREAMLITIO],
        is_awesome=True,
    ),
    Resource(
        name="Streamlit Community",
        url="https://discuss.streamlit.io/top/quarterly",
        tags=[STREAMLITIO],
        is_awesome=True,
    ),
    Resource(
        "The announcing blog",
        url="https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace",
        tags=[STREAMLITIO],
        is_awesome=True,
    ),
    Resource(
        "The announcing community post",
        url="https://discuss.streamlit.io/t/streamlit-has-launched/105/3",
        tags=[STREAMLITIO],
        is_awesome=True,
    ),
    Resource(
        "LinkedIn post that started awesome-streamlit.org",
        url="https://www.linkedin.com/feed/update/urn:li:activity:6586497522896818176",
        tags=[AWESOMESTREAMLIT, SOCIAL],
        is_awesome=True,
    ),
    Resource(
        "LinkedIn #streamlit",
        url="https://www.linkedin.com/search/results/all/?keywords=%23streamlit",
        tags=[SOCIAL],
        is_awesome=True,
    ),
    Resource(
        name="Twitter #streamlit",
        url="https://twitter.com/search?q=%23streamlit&src=typed_query",
        tags=[SOCIAL],
        is_awesome=True,
    ),
    ### Awesome Applications
    Resource(
        name="SpacyIO Application",
        url="https://gist.github.com/ines/b320cb8441b590eedf19137599ce6685",
        tags=[APP, PAGE],
        is_awesome=True,
    ),
    Resource(
        name="Kaggle Mushrooms Dashboard",
        url="https://github.com/pierpaolo28/Data-Visualization/tree/master/Streamlit",
        tags=[APP],
        is_awesome=True,
    ),
    Resource(
        name="Hacker News technical discussion of how Streamlit work",
        url="https://news.ycombinator.com/item?id=21158487",
        tags=[TECHNICAL],
        is_awesome=True,
    ),
    Resource(
        name="Jupyter Voila",
        url="https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93",
        tags=[ALTERNATIVE],
        is_awesome=True,
    ),
    Resource(
        name="Plotly Dash",
        url="https://plot.ly/dash/",
        tags=[ALTERNATIVE],
        is_awesome=True,
    ),
    Resource(
        name="Bokeh",
        url="https://bokeh.pydata.org/en/latest/index.html",
        tags=[ALTERNATIVE],
        is_awesome=True,
    ),
    Resource(
        name="Sentiment Analyzer Tool",
        url=(
            "https://www.linkedin.com/posts/patidarparas13_code-ml-machinelearning-"
            "ugcPost-6585745929062703104-ttkv"
        ),
        tags=[APP, CODE, SOCIAL],
        is_awesome=True,
    ),
    Resource(
        name="Streamlit-components-demo App",
        url=("https://fullstackstation.com/streamlit-components-demo"),
        tags=[APP],
        is_awesome=True,
    ),
    Resource(
        name="Streamlit-components-demo Code",
        url=("https://github.com/virusvn/streamlit-components-demo"),
        tags=[CODE],
        is_awesome=True,
    ),
    Resource(
        name="Deploying Streamlit app to EC2 instance",
        url="https://medium.com/@pokepim/deploying-streamlit-app-to-ec2-instance-7a7edeffbb54",
        tags=[CODE],
        is_awesome=True,
    ),
    Resource(
        name="Uber Data Explorer App",
        url="https://dataexplorerlit.herokuapp.com/",
        tags=[CODE],
        is_awesome=True,
    ),
]

TAGS = []
for resource in RESOURCES:
    for tag in resource.tags:
        TAGS.append(tag)
TAGS = sorted(list(set(TAGS)))
