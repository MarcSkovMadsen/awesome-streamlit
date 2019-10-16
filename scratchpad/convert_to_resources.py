import json
import urllib.request
from typing import Dict

from awesome_streamlit.shared.models import Author, Resource, Tag
from db import APP_INGALLERY, CODE, STREAMLIT

JSON_URL = "https://raw.githubusercontent.com/virusvn/streamlit-components-demo/master/streamlit_apps.json"


def fetch_json(url: str):
    data = urllib.request.urlopen(url).read()
    output = json.loads(data)
    return output


def get_apps(url: str) -> Dict[str, str]:
    json_obj = fetch_json(url)
    apps = {}
    for item in json_obj:
        if item["url"] is not None and item["url"].endswith(".py"):
            # can overwrite if same name
            apps[item["name"]] = item["url"]

    return apps


def get_resources(apps):
    resources = []
    for name, url in apps.items():
        resource = Resource(
            name=name,
            url=url,
            is_awesome=False,
            tags=[CODE, APP_INGALLERY],
            author=STREAMLIT,
        )
        resources.append(resource)
    return resources


apps = get_apps(JSON_URL)
resources = get_resources(apps)
representation = repr(resources)
# print(representation)
representation = representation.replace("author=Streamlit", "author=STREAMLIT")
representation = representation.replace("Code", "CODE")
representation = representation.replace(
    "Included in Awesome Streamlit Gallery", "APP_INGALLERY"
)
print(representation)

STREAMLIT_COMPONENTS = [
    Resource(
        name="charts.area_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.area_chart.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.audio",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.audio.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.bar_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.bar_chart.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.bokeh_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.bokeh_chart.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.deck_gl_charts1",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.deck_gl_charts1.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.deck_gl_charts2",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.deck_gl_charts2.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.graphviz_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.graphviz_chart.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.image",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.image.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.line_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.line_chart.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.map",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.map.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.plotly_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.plotly_chart.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.pyplot",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.pyplot.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.vega_lite_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.vega_lite_chart.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="charts.video",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.video.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="data.dataframe",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/data.dataframe.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="data.json",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/data.json.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="data.table",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/data.table.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.code",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.code.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.header",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.header.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.markdown",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.markdown.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.subheader",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.subheader.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.text",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.text.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.title",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.title.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.write1",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.write1.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.write2",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.write2.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="text.write3",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.write3.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.button",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.button.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.checkbox",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.checkbox.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.date_input",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.date_input.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.radio",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.radio.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.selectbox",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.selectbox.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.slider",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.slider.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.text_area",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.text_area.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.text_input",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.text_input.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
    Resource(
        name="widget.time_input",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.time_input.py",
        is_awesome=False,
        tags=[CODE, APP_INGALLERY],
        author=STREAMLIT,
    ),
]
