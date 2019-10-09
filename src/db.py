from shared.models import Resource, Tag

APP = Tag("App")
PAGE = Tag(name="App included here")
STREAMLITIO = Tag(name="Streamlit.io")
THEBEGINNING = Tag(name="The beginning")
SOCIAL = Tag(name="Social")
TECHNICAL = Tag(name="Technical")

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
        "LinkedIn Post that started this project",
        url="https://www.linkedin.com/feed/update/urn:li:activity:6586497522896818176",
        tags=[THEBEGINNING, SOCIAL],
    ),
    Resource(
        name="Twitter",
        url="https://twitter.com/search?q=%23streamlit&src=typed_query",
        tags=[SOCIAL],
    ),
    ### Awesome Applications
    Resource(
        name="SpacyIO Application",
        url="https://gist.github.com/ines/b320cb8441b590eedf19137599ce6685",
        tags=[PAGE, APP],
    ),
    Resource(
        name="Kaggle Mushrooms Dashboard",
        url="https://github.com/pierpaolo28/Data-Visualization/tree/master/Streamlit",
        tags=[APP],
    ),
    Resource(
        name="abcd",
        url="https://news.ycombinator.com/item?id=21158487",
        tags=[TECHNICAL],
    ),
]

TAGS = []
for resource in RESOURCES:
    for tag in resource.tags:
        TAGS.append(tag)
TAGS = sorted(list(set(TAGS)))
