"""Simple 'database' of models

Here you maintain the list of awesome resources
"""
from awesome_streamlit.database import authors, tags
from awesome_streamlit.database.apps_in_gallery import APPS_IN_GALLERY
from awesome_streamlit.database.tags import (ALTERNATIVE, APP, APP_IN_GALLERY,
                                             CODE, SOCIAL, STREAMLIT_TAG,
                                             TECHNICAL)
# pylint: disable=line-too-long
from awesome_streamlit.shared.models import Resource

# STREAMLIT FILE ROOTS

STREAMLIT_EXAMPLE_APPS_ROOT = (
    "https://raw.githubusercontent.com/streamlit/streamlit/develop/examples/"
)
STREAMLIT_COMPONENTS_APPS_ROOT = (
    "https://github.com/streamlit/streamlit/tree/develop/docs/api-examples-source"
)
STREAMLIT_EXAMPLE_APPS_FAILED_TEST_FILES = [
    "apocrypha.py",
    "bart_vs_bikes.py",
    "images.py",
    "matplotlib_kwargs.py",
    "mnist-cnn",
    "reference.py",
    "run_on_save.py",
    "syntax_hilite.py",
    #  "disable_client.py", RUNS TOO LONG DURING TESTS
]
STREAMLIT_EXAMPLE_APPS_FAILED_TEST = [
    Resource(
        name=file,
        url=STREAMLIT_EXAMPLE_APPS_ROOT + file,
        is_awesome=False,
        tags=[CODE, APP, APP_IN_GALLERY],
        author=authors.STREAMLIT_AUTHOR,
    )
    for file in STREAMLIT_EXAMPLE_APPS_FAILED_TEST_FILES
]

STREAMLIT_EXAMPLE_APPS_FILES = [
    "altair_example.py",
    "animation.py",
    "audio.py",
    "bokeh_example.py",
    "caching.py",
    "checkboxes.py",
    "dataframe_styling.py",
    "empty_charts.py",
    "graphviz_example.py",
    "interactive_widgets.py",
    "keras_example.py",
    "lists.py",
    "plotly_example.py",
    "syntax_error.py",
    "table_styling.py",
    "video.py",
]
STREAMLIT_EXAMPLE_APPS = [
    Resource(
        name=file,
        url=STREAMLIT_EXAMPLE_APPS_ROOT + file,
        is_awesome=False,
        tags=[CODE, APP, APP_IN_GALLERY, tags.STREAMLIT_EXAMPLE],
        author=authors.STREAMLIT_AUTHOR,
    )
    for file in STREAMLIT_EXAMPLE_APPS_FILES
]
RESOURCES_STREAMLIT_COMPONENT_APPS = [
    Resource(
        name="pcharts.area_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.area_chart.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.audio",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.audio.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.bar_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.bar_chart.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.bokeh_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.bokeh_chart.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.deck_gl_charts1",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.deck_gl_charts1.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.deck_gl_charts2",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.deck_gl_charts2.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.graphviz_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.graphviz_chart.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.image",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.image.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.line_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.line_chart.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.map",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.map.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.plotly_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.plotly_chart.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.pyplot",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.pyplot.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.vega_lite_chart",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.vega_lite_chart.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="charts.video",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/charts.video.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="data.dataframe",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/data.dataframe.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="data.json",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/data.json.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="data.table",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/data.table.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="text.code",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.code.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="text.header",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.header.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="text.markdown",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.markdown.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="text.subheader",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.subheader.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="text.text",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.text.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="text.title",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.title.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="text.write1",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.write1.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="text.write2",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.write2.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="text.write3",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/text.write3.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="widget.button",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.button.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="widget.checkbox",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.checkbox.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="widget.date_input",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.date_input.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="widget.radio",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.radio.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="widget.selectbox",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.selectbox.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="widget.slider",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.slider.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="widget.text_area",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.text_area.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="widget.text_input",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.text_input.py",
        is_awesome=False,
        tags=[CODE, APP_IN_GALLERY, tags.STREAMLIT_COMPONENT],
        author=authors.STREAMLIT_AUTHOR,
    ),
    Resource(
        name="widget.time_input",
        url="https://raw.githubusercontent.com/streamlit/streamlit/master/docs/api-examples-source/widget.time_input.py",
        is_awesome=False,
        tags=[CODE, APP, APP_IN_GALLERY],
        author=authors.STREAMLIT_AUTHOR,
    ),
]

RESOURCES = (
    [
        Resource(
            "Streamlit Roadmap",
            url="https://github.com/streamlit/streamlit/wiki/Roadmap",
            is_awesome=True,
            tags=[tags.STREAMLIT_TAG, tags.ARTICLE],
            author=authors.STREAMLIT_AUTHOR,
        ),
        Resource(
            "The Streamlit Roadmap: Big Plans for 2020!",
            url="https://discuss.streamlit.io/t/the-streamlit-roadmap-big-plans-for-2020/2054",
            is_awesome=True,
            tags=[tags.STREAMLIT_TAG, tags.ARTICLE],
            author=authors.STREAMLIT_AUTHOR,
        ),
        Resource(
            "Object Detection in a few lines of code",
            url="https://medium.com/@boadziedaniel/object-detection-in-a-few-lines-of-code-40640fdb2c46",
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.ARTICLE],
            author=authors.BOADZIE_DANIEL,
        ),
        Resource(
            "Creating A Stock Dashboard",
            url="https://www.linkedin.com/pulse/creating-stock-dashboard-curt-beck/?trackingId=AityTMjb3NukPM%2FZIrEoxA%3D%3D",
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.ARTICLE],
            author=authors.CURT_BECK,
        ),
        Resource(
            "Turn Python Scripts into Beautiful ML Tools | PyData LA 2019",
            url="https://www.youtube.com/watch?v=0It8phQ1gkQ",
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.VIDEO],
            author=authors.ADRIAN_TREUILLE,
        ),
        Resource(
            "Host Streamlit on Heroku with Nginx basic authentication",
            url="https://github.com/Taxuspt/heroku_streamlit_nginx",
            is_awesome=True,
            tags=[tags.GUIDE, tags.CODE],
            author=authors.ALEXANDRE_DOMINGUES,
        ),
        Resource(
            "Intermediate Streamlit - Tips and Tricks for an evolving app",
            url="https://towardsdatascience.com/intermediate-streamlit-d5a1381daa65",
            is_awesome=True,
            tags=[tags.ARTICLE],
            author=authors.PETER_BAUMGARTNER,
        ),
        Resource(
            "Awesome-Panel.Org",
            url="https://awesome-panel.org",
            is_awesome=True,
            tags=[tags.SISTER_SITES],
            author=authors.MARC_SKOV_MADSEN,
        ),
        Resource(
            name="Quickly Build and Deploy a Dashboard with Streamlit",
            url="https://towardsdatascience.com/quickly-build-and-deploy-an-application-with-streamlit-988ca08c7e83",
            is_awesome=True,
            tags=[tags.APP, tags.CODE, tags.DEPLOYMENT],
            author=authors.MAARTEN_GROOTENDORST,
        ),
        Resource(
            name="Powering up Apache JMeter with Streamlit",
            url="https://qainsights.com/apache-jmeter-with-streamlit-for-machine-learning/",
            is_awesome=True,
            tags=[tags.APP, tags.CODE],
            author=authors.NAVEEN_KUMAR,
        ),
        Resource(
            name="Machine Learning App Registry",
            url="https://ml-app-rig.herokuapp.com/",
            is_awesome=False,
            tags=[tags.APP],
            author=authors.BOADZIE_DANIEL,
        ),
        Resource(
            name="Machine Learning App Registry",
            url="https://github.com/Boadzie/ML-App-Registry",
            is_awesome=False,
            tags=[tags.CODE, tags.APP],
            author=authors.BOADZIE_DANIEL,
        ),
        Resource(
            name="Mining and Classifying Medical Text Documents",
            url="https://github.com/gtancev/MLML/blob/master/nlp_app.py",
            is_awesome=True,
            tags=[tags.CODE, tags.APP],
            author=authors.GEORGI_TANCEV,
        ),
        Resource(
            name="Mining and Classifying Medical Text Documents",
            url="https://towardsdatascience.com/mining-and-classifying-medical-text-documents-1876462f73bc",
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.ARTICLE, tags.NLP, tags.DEPLOYMENT],
            author=authors.GEORGI_TANCEV,
        ),
        Resource(
            name="Full-Stack AI: Building a UI for Your Latest AI Project in No Time at All",
            url="https://towardsdatascience.com/full-stack-ai-building-a-ui-for-your-latest-ai-project-in-no-time-at-all-7e5c8fd4eafd",
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.ARTICLE, tags.IMAGE_RECOGNITION],
        ),
        Resource(
            name="How To Deploy Streamlit Apps (Using Heroku)",
            url="https://www.youtube.com/watch?v=skpiLtEN3yk&feature=youtu.be",
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.VIDEO, tags.DEPLOYMENT],
        ),
        Resource(
            name="How to create and deploy data exploration web app easily using python",
            url="https://github.com/robmarkcole/mqtt-camera-streamer",
            is_awesome=True,
            tags=[tags.APP, tags.CODE, tags.DEPLOYMENT],
        ),
        Resource(
            name="How to create and deploy data exploration web app easily using python",
            url="https://medium.com/@ansjin/how-to-create-and-deploy-data-exploration-web-app-easily-using-python-a03c4b8a1f3e",
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.ARTICLE, tags.DEPLOYMENT],
        ),
        Resource(
            name="How to write web apps using simple python for data scientists",
            url="https://towardsdatascience.com/how-to-write-web-apps-using-simple-python-for-data-scientists-a227a1a01582",
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.ARTICLE],
        ),
        Resource(
            name="A step by step guide to running streamlit pytorch and bert on a cheap aws instance",
            url="https://fuzzyblog.io/blog/python/2019/10/17/a-step-by-step-guide-to-running-streamlit-pytorch-and-bert-on-a-cheap-aws-instance.html",
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.ARTICLE, tags.DEPLOYMENT],
        ),
        Resource(
            name="How to build your machine learning app in 3 simple steps",
            url="https://towardsdatascience.com/how-to-build-your-machine-learning-app-in-3-simple-steps-d56ed910355c",
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.ARTICLE, tags.DEPLOYMENT],
        ),
        Resource(name="Panel", url="http://panel.pyviz.org/", is_awesome=True, tags=[ALTERNATIVE]),
        Resource(
            name="Streamlit Demo",
            url="https://github.com/Poseyy/StreamlitDemo",
            is_awesome=True,
            tags=[tags.APP, tags.CODE],
            author=authors.POSEY,
        ),
        Resource(
            name="NLP Based App with Streamlit",
            url=(
                "https://github.com/Jcharis/Streamlit_DataScience_Apps/tree/"
                "master/NLP_App_with_Streamlit_Python"
            ),
            is_awesome=True,
            tags=[tags.APP, tags.CODE],
            author=authors.JCHARIS,
        ),
        Resource(
            name="Building an Iris EDA App with Streamlit and Python",
            url="https://www.youtube.com/watch?v=L_mZcEMFUIc",
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.VIDEO],
            author=authors.JCHARIS,
        ),
        Resource(
            name="Streamlit Python Tutorial (Crash Course)",
            url="https://www.youtube.com/watch?v=_9WiB2PDO7k",
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.VIDEO],
            author=authors.JCHARIS,
        ),
        Resource(
            name="Building a ui for your latest ai",
            url=(
                "https://towardsdatascience.com/full-stack-ai-building-a-ui-for-your-latest-ai"
                "-project-in-no-time-at-all-7e5c8fd4eafd  "
            ),
            is_awesome=True,
            tags=[tags.TUTORIAL, tags.ARTICLE],
            author=authors.POSEY,
        ),
        Resource(
            name="Hello-streamlit deployed on Glitch",
            url="https://glitch.com/~hello-streamlit",
            is_awesome=True,
            tags=[tags.APP, tags.DEPLOYMENT],
            author=authors.ALEXANDER_GARCIA,
        ),
        Resource(
            name="Resources List",
            url="https://github.com/marcskovmadsen/awesome-streamlit",
            is_awesome=True,
            tags=[tags.AWESOME_STREAMLIT_ORG],
            author=authors.AWESOME_STREAMLIT_ORG,
        ),
        Resource(
            name="Repo",
            url="https://github.com/marcskovmadsen/awesome-streamlit",
            is_awesome=True,
            tags=[tags.AWESOME_STREAMLIT_ORG],
            author=authors.AWESOME_STREAMLIT_ORG,
        ),
        Resource(
            name="App",
            url="https://awesome-streamlit.org",
            is_awesome=True,
            tags=[tags.AWESOME_STREAMLIT_ORG],
            author=authors.AWESOME_STREAMLIT_ORG,
        ),
        Resource(
            name="Docs",
            url="https://awesome-streamlit.readthedocs.io/en/latest/",
            is_awesome=True,
            tags=[tags.AWESOME_STREAMLIT_ORG],
            author=authors.AWESOME_STREAMLIT_ORG,
        ),
        Resource(
            name="Python Package",
            url="https://pypi.org/project/awesome-streamlit/",
            is_awesome=True,
            tags=[tags.AWESOME_STREAMLIT_ORG],
            author=authors.AWESOME_STREAMLIT_ORG,
        ),
        Resource(
            name="Docker Image",
            url="https://cloud.docker.com/u/marcskovmadsen/repository/docker/marcskovmadsen/awesome-streamlit",
            is_awesome=True,
            tags=[tags.AWESOME_STREAMLIT_ORG],
            author=authors.AWESOME_STREAMLIT_ORG,
        ),
        Resource(
            name="Streamlit launches article in TechCrunch",
            url="https://techcrunch.com/2019/10/01/streamlit-launches-open-source-machine-learning-application-development-framework/",
            tags=[STREAMLIT_TAG],
            is_awesome=True,
        ),
        Resource(
            name="Streamlit.io", url="https://streamlit.io/", tags=[STREAMLIT_TAG], is_awesome=True
        ),
        Resource(
            name="Streamlit Docs",
            url="https://streamlit.io/docs/",
            tags=[STREAMLIT_TAG],
            is_awesome=True,
        ),
        Resource(
            name="Streamlit Community",
            url="https://discuss.streamlit.io/top/quarterly",
            tags=[STREAMLIT_TAG],
            is_awesome=True,
        ),
        Resource(
            "The announcing blog",
            url="https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace",
            tags=[STREAMLIT_TAG],
            is_awesome=True,
        ),
        Resource(
            "The announcing community post",
            url="https://discuss.streamlit.io/t/streamlit-has-launched/105/3",
            tags=[STREAMLIT_TAG],
            is_awesome=True,
        ),
        Resource(
            "LinkedIn post that started awesome-streamlit.org",
            url="https://www.linkedin.com/feed/update/urn:li:activity:6586497522896818176",
            tags=[tags.AWESOME_STREAMLIT_ORG, SOCIAL],
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
            name="Plotly Dash", url="https://plot.ly/dash/", tags=[ALTERNATIVE], is_awesome=True
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
        Resource(
            name="Deploying wed apps with Streamlit, Docker, and AWS",
            url="https://github.com/collinprather/streamlit-docker/tree/docker-compose+postgres",
            is_awesome=True,
            tags=[tags.APP, tags.CODE],
            author=authors.COLLIN_PRATHER,
        ),
    ]
    + STREAMLIT_EXAMPLE_APPS
    + STREAMLIT_EXAMPLE_APPS_FAILED_TEST
    + RESOURCES_STREAMLIT_COMPONENT_APPS
    + APPS_IN_GALLERY
)

TAGS = []
for resource in RESOURCES:
    for tag in resource.tags:
        TAGS.append(tag)
TAGS = sorted(list(set(TAGS)))
