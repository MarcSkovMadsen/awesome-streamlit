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
INGALLERY = Tag(name="In Gallery")

# Authors
STREAMLIT = Author(name="Streamlit", url="https://streamlit.io/")
MARC_SKOV_MADSEN = Author(
    name="Marc Skov Madsen", url="https://datamodelsanalytics.com"
)
INES = Author(name="Ines Montani", url="https://gist.github.com/ines")

RESOURCES_OTHER_APPS = [
    Resource(
        name="SpacyIO",
        url="https://gist.githubusercontent.com/ines/b320cb8441b590eedf19137599ce6685/raw/6e0ead5a442fd9c5e3f621a76fba94241cc847ce/streamlit_spacy.py",
        tags=[CODE, INGALLERY],
        is_awesome=True,
        author=INES,
    ),
    Resource(
        name="Spreadsheet",
        url="https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/src/pages/gallery/contributions/marc_skov_madsen/spreadsheet.py",
        tags=[CODE, INGALLERY],
        is_awesome=True,
        author=MARC_SKOV_MADSEN,
    )
]

RESOURCES_STREAMLIT_APPS = [
    Resource(
        name="charts.area_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.area_chart.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.audio",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.audio.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.bar_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.bar_chart.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.bokeh_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.bokeh_chart.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.deck_gl_charts1",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.deck_gl_charts1.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.deck_gl_charts2",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.deck_gl_charts2.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.graphviz_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.graphviz_chart.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.image",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.image.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.line_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.line_chart.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.map",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.map.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.plotly_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.plotly_chart.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.pyplot",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.pyplot.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.vega_lite_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.vega_lite_chart.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.video",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.video.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="data.dataframe",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/data.dataframe.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="data.json",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/data.json.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="data.table",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/data.table.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.code",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.code.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.header",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.header.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.markdown",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.markdown.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.subheader",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.subheader.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.text",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.text.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.title",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.title.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.write1",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.write1.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.write2",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.write2.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.write3",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.write3.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.button",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.button.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.checkbox",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.checkbox.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.date_input",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.date_input.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.radio",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.radio.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.selectbox",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.selectbox.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.slider",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.slider.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.text_area",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.text_area.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.text_input",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.text_input.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.time_input",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.time_input.py",
        is_awesome=False,
        tags=[CODE, INGALLERY],
        author=STREAMLIT,
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
] + RESOURCES_STREAMLIT_APPS + RESOURCES_OTHER_APPS

TAGS = []
for resource in RESOURCES:
    for tag in resource.tags:
        TAGS.append(tag)
TAGS = sorted(list(set(TAGS)))
