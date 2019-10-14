# Awesome Streamlit [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesome-streamlit)

[<img src="https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/assets/streamlit-logo.png?raw=true" align="right" height="100">](https://streamlit.io)

> The fastest way to build **Awesome Tools and Apps**! Powered by **Python**!

The purpose of this project is to share knowledge on how Awesome [Streamlit](https://streamlit.io/) is and can become. [Pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls) are very welcome!

Streamlit has just been [announced](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace) (Oct 2019) but I see the potential of becoming the **Iphone of Data Science Apps**. And maybe it can even become the Iphone of Technical Writing, Code, Micro Apps and Python.

This project provides

- A curated [list](https://github.com/MarcSkovMadsen/awesome-streamlit#awesome-resources) of Awesome Streamlit **resources**. See below.
- An [**awesome Streamlit application**](https://awesome-streamlit.azurewebsites.net/) with a **gallery** of Awesome Streamlit Apps.
  - Feel free to add your awesome app to the gallery via a [Pull request](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls). It's easy (see below).
- A [**vision**](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/AWESOME-STREAMLIT.md) on how awesome Streamlit is and can become.
- A **best practices** example and **starter** template of a larger, multipage, high quality app.

## Awesome-streamlit.org is not yet performant

I'm working on getting it performant, but there is an issue. Cf.

- [https://discuss.streamlit.io/t/streamlit-app-deployed-as-azure-webapp-for-containers-becomes-unresponsive-over-time/330]
  - [https://github.com/streamlit/streamlit/issues/367](https://github.com/streamlit/streamlit/issues/367)
  - [https://github.com/MarcSkovMadsen/awesome-streamlit/issues/6](https://github.com/MarcSkovMadsen/awesome-streamlit/issues/6)

If you know how to solve this please let me know. Thanks

## The Magic of Streamlit

The only way to truly understand how magical Streamlit is to play around with it, but if you need to be convinced first, then here is the **4 minute introduction** to Streamlit!

Afterwards you can go to the [Streamlit docs](https://streamlit.io/docs/) to get started.

[![Introduction to Streamlit](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/assets/youtube-introduction-to-streamlit.png)](https://www.youtube.com/watch?v=B2iAodr0fOo&feature=youtu.be "Introduction to streamlit")

## Awesome Resources

A curated list of awesome streamlit resources. Inspired by [awesome-python](https://github.com/vinta/awesome-python) and [awesome-pandas](https://github.com/tommyod/awesome-pandas).

### Alternatives

- [Bokeh](https://bokeh.pydata.org/en/latest/index.html)
- [Jupyter Voila](https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93)
- [Plotly Dash](https://plot.ly/dash/)

### Apps

- [Kaggle Mushrooms Dashboard](https://github.com/pierpaolo28/Data-Visualization/tree/master/Streamlit)
- [Sentiment Analyzer Tool](https://www.linkedin.com/posts/patidarparas13_code-ml-machinelearning-ugcPost-6585745929062703104-ttkv)
- [SpacyIO Application](https://gist.github.com/ines/b320cb8441b590eedf19137599ce6685)
- [Streamlit-components-demo App](https://fullstackstation.com/streamlit-components-demo)

### Code

- [Streamlit-components-demo Code](https://github.com/virusvn/streamlit-components-demo)

### Social

- [LinkedIn #streamlit](https://www.linkedin.com/search/results/all/?keywords=%23streamlit)
- [Twitter #streamlit](https://twitter.com/search?q=%23streamlit&src=typed_query)

### Streamlit.io

- [Streamlit Community](https://discuss.streamlit.io/top/quarterly)
- [Streamlit Docs](https://streamlit.io/docs/)
- [Streamlit.io](https://streamlit.io/)
- [The announcing blog](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace)
- [The announcing community post](https://discuss.streamlit.io/t/streamlit-has-launched/105/3)

### Technical

- [Hacker News technical discussion of how Streamlit work](https://news.ycombinator.com/item?id=21158487)

### The beginning

- [LinkedIn post that started awesome-streamlit.org](https://www.linkedin.com/feed/update/urn:li:activity:6586497522896818176)

## Governance

This repo is maintained by me :-)

I'm Marc, Skov, Madsen, PhD, CFA®, Lead Data Scientist Developer at [Ørsted](https://orsted.com)

You can learn more about me at [datamodelsanalytics.com](https://datamodelsanalytics.com)

I try my best to govern and maintain this project in the spirit of the [Zen of Python](https://www.python.org/dev/peps/pep-0020/).

But **i'm not an experienced open source maintainer** so helpfull suggestions are appreciated.

Thanks

## Contribute

GitHub [Issues](https://github.com/MarcSkovMadsen/awesome-streamlit/issues) and [Pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls) are very welcome!

If you believe Streamlit is awesome and would like to join as a Core Maintainer feel free to reach out via [datamodelsanalytics.com](https://datamodelsanalytics.com)

### How to contribute awesome links

The best way to contribute an awesome link is via a [Pull request](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls).

In the pull request you should

- describe why your contribution is awesome and should be included.
- update the [README.md](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/README.md) file
- update the list of RESOURCES in the [src/db.py](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/src/db.py) file.

Thanks.

### How to contribute awesome apps

The best way to contribute an awesome app is via a [Pull request](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls).

In the pull request you should

- describe why your contribution is awesome and should be included.
- add your code in a new `your_app_name.py` file in the `src/pages/gallery` folder.
  - If your code is large feel free to add a `your_app_name` folder of files instead.
- your code should look like

```python
"""APP DESCRIPTION"""
import streamlit as st

def write():
    st.markdown(
        """
        ## APP NAME

        DESCRIPTION

        Author: [YOUR NAME](https://URL_TO_YOU))\n
        Source: [Github](https://github.com/URL_TO_CODE)
        """
    )
    # Your code goes below

if __name__ == "__main__":
    write()
```

- Please note magic in sub pages does not work. So **don't use magic**.
- add the `your_app_name` to the
  - list of APPS in the [src/gallery/index.py](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/src/gallery/index.py).
- import your page in the app.py to enable automatic reload. You need to use the full path `import src.pages.gallery.your_app_name as your_app_name` for automatic reload to work. Cf. this [issue](https://github.com/MarcSkovMadsen/awesome-streamlit/issues/2)
- update the [requirements.txt](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/requirements.txt) file.
    Please specify the required versions.
- Run the automated tests using `invoke test.all` and fix all errors from your app
- Run the full app via `streamlit run app.py` and manually test your contribution.

Please note that your app should not require high compute power as we are running on one of the cheapest tiers available on Azure.

Feel free to reach out if you have comments, questions or need help.

Thanks.

### How to contribute to the Streamlit Community

Please sign up to and participate in the community at [discuss.streamlit.io](https://discuss.streamlit.io/)

### How to contribute to the Streamlit Package

Please contribute to improving the Streamlit package at [GitHub/streamlit/streamlit](https://github.com/streamlit/streamlit)

### How to contribute to Streamlit.io

Streamlit.io is in the position of trying to balance building an awesome, succesfull business and providing an awesome product to the open source community.

If you are in a Team please consider signing up for the beta of

- [Streamlit for teams](https://streamlit.io/forteams/)

### How to sponsor the Awesome Streamlit project

If you would like to sponsor my time or the infrastructure the platform is running on feel free to reach out via [datamodelsanalytics.com](https://datamodelsanalytics.com).

You can also just appreciate the work that has alredy been done if you

[![Buy me a coffee](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/assets/buymeacoffee.png?raw=true)](https://www.buymeacoffee.com/4jlTzBJyQ)

Thanks

Marc

## LICENSE

[Attribution-ShareAlike 4.0 International](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/license.md)

## Getting Started with the Awesome Streamlit Application

### Prerequisites

- An Operating System like Windows, OsX or Linux
- A working [Python](https://www.python.org/) installation.
  - We recommend using 64bit Python 3.7.4.
- a Shell
  - We recommend [Git Bash](https://git-scm.com/downloads) for Windows 8.1
  - We recommend [wsl](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) for For Windows 10
- an Editor
  - We recommend [VS Code](https://code.visualstudio.com/) (Preferred) or [PyCharm](https://www.jetbrains.com/pycharm/).
- The [Git cli](https://git-scm.com/downloads)

### Installation

Clone the repo

```bash
git clone https://github.com/MarcSkovMadsen/awesome-streamlit.git
```

cd into the project root folder

```bash
cd awesome-streamlit
```

Then you should create a virtual environment named .venv

```bash
python -m venv .venv
```

and activate the environment.

On Linux, OsX or in a Windows Git Bash terminal it's

```bash
source .venv/Scripts/activate
```

In a Windows terminal it's

```bash
.venv/Scripts/activate.bat
```

The you should install the local requirements

```bash
pip install -r requirements_local.txt
```

Finally you need to install some [spacy](https://spacy.io/) dependencies

```bash
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
python -m spacy download de_core_news_sm
```

### Build and run the Application Locally

```bash
streamlit run app.py
```

or as a Docker container via

```bash
invoke docker.build --rebuild
invoke docker.run-server
```

### Run the Application using the image on Dockerhub

If you don't wan't to clone the repo and build the docker container you can just use `docker run` to run the image from [Dockerhub](https://cloud.docker.com/u/marcskovmadsen/repository/docker/marcskovmadsen/awesome-streamlit)

To run bash interactively

```bash
docker run -it -p 80:80 --entrypoint "/bin/bash" marcskovmadsen/awesome-streamlit:latest
```

To run the streamlit interactively on port 80

```bash
docker run -it -p 80:80 --entrypoint "streamlit" marcskovmadsen/awesome-streamlit:latest run app.py
```

### Code quality and Tests

We use

- [isort](https://pypi.org/project/isort/) for sorting import statements
- [autoflake](https://github.com/myint/autoflake) to remove unused imports and unused variables
- [black](https://pypi.org/project/black/) the opinionated code formatter
- [pylint](https://www.pylint.org/) for static analysis
- [mypy](https://github.com/python/mypy) for static type checking
- [pytest](https://github.com/pytest-dev/pytest) for unit to functional tests

to ensure a high quality of our code and application.

You can run all tests using

```bash
invoke test.all
```

### Streamlit Tests

I've created a first version of an awesome streamlit test runner. You run it via

```bash
streamlit run test_runner_app.py
```

or in Docker

```bash
docker run -it -p 80:80 --entrypoint "streamlit" marcskovmadsen/awesome-streamlit:latest run test_runner_app.py
```

![Awesome Streamlit Test Runner](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/assets/awesome-streamlit-test-runner.png)


### Workflow

We use the power of [Invoke](http://www.pyinvoke.org/) to semi-automate the local workflow. You can see the list of available commands using

```bash
$ invoke --list
Available tasks:

  docker.build                            Build Docker image
  docker.push                             Push the Docker container
  docker.run                              Run the Docker container interactively.
  docker.run-server                       Run the Docker container interactively
  docker.system-prune                     The docker system prune command will free up space
  test.all (test.pre-commit, test.test)   Runs isort, autoflake, black, pylint, mypy and pytest
  test.autoflake                          Runs autoflake to remove unused imports on all .py files recursively
  test.bandit                             Runs Bandit the security linter from PyCQA.
  test.black                              Runs black (autoformatter) on all .py files recursively
  test.isort                              Runs isort (import sorter) on all .py files recursively
  test.mypy                               Runs mypy (static type checker) on all .py files recursively
  test.pylint                             Runs pylint (linter) on all .py files recursively to identify coding errors
  test.pytest                             Runs pytest to identify failing tests
```

### Configuration

You can configure the app in the `config.py` file.

Please note that Streamlit has its own config files in the `~/.streamlit` folder.

### CI/ CD and Hosting

The application is

- build as a Docker image and tested via Azure Pipelines builds
  - You find the Dockerfiles [here](https://github.com/MarcSkovMadsen/awesome-streamlit/tree/master/devops/docker) and the Azure pipelines yml files [here](https://github.com/MarcSkovMadsen/awesome-streamlit/tree/master/devops/azure-pipelines)

![Azure Pipelines](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/assets/azure-pipeline.png)

- pushed to the Dockerhub repository [marcskovmadsen/awesome-streamlit](https://cloud.docker.com/u/marcskovmadsen/repository/docker/marcskovmadsen/awesome-streamlit).

![Dockerhub](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/assets/dockerhub.png)

- released via Azure Pipelines

![Azure Pipelines](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/assets/azure-pipeline-release.png)

- to a web app for containers service on Azure on the cheapest non-free pricing tier

![Azure Pipelines](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/assets/azure-pricing-tier.png)

### The Awesome-Streamlit Package

You can build the package using

```bash
cd package
python setup.py sdist bdist_wheel
```

If you wan't to publish the package to PyPi you should first

update the version number in the setup.py file. The format is `YYYYmmdd.version`. For example `20191014.2`

Then you run

```bash
twine upload dist/awesome-streamlit-YYYYmmdd.version.tar.gz -u <the-pypi-username> -p <the-pypi-password>
```

For more info see the package [README.md](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/package/README.md)

### Project Layout

The basic layout of a application is as simple as

```bash
.
└── app.py
```

As our application grows we would refactor our app.py file into multiple folders and files.

- *assets* here we keep our css and images assets.
- *models* - Defines the layout of our data in the form of
  - Classes: Name, attribute names, types
  - DataFrame Schemas: column and index names, dtypes
  - SQLAlchemy Tables: columns names, types
- *pages* - Defines the different pages of the Streamlit app
- *services* - Organizes and shares business logic, models, data and functions with different pages of the Streamlit App.
  - Database interactions: Select, Insert, Update, Delete
  - REST API interactions, get, post, put, delete
  - Pandas transformations

and end up with a project structure like

```bash
.
├── app.py
└── src
    └── assets
    |    └── css
    |    |   ├── app.css
    |    |   ├── component1.css
    |    |   ├── component2.css
    |    |   ├── page1.css
    |    |   └── page2.css
    |    └── images
    |    |   ├── image1.png
    |    |   └── image2.png
    ├── core
    |   └── services
    |       ├── service1.py
    |       └── service2.py
    └── pages
    |   └── pages
    |       ├── page1.py
    |       └── page2.py
    └── shared
        └── models
        |   ├── model1.py
        |   └── model2.py
        └── components
            ├── component1.py
            └── component2.py
```

Further refactoring is guided by by [this](https://itnext.io/choosing-a-highly-scalable-folder-structure-in-angular-d987de65ec7) blog post and the [Angular Style Guide](https://angular.io/guide/styleguide).

We place our tests in a `test` folder in the root folder organized with folders similar to the `app` folder and file names with a `test_` prefix.

```bash
.
└── test
    ├── test_app.py
    ├── core
    |   └── services
    |       ├── test_service1.py
    |       └── test_service2.py
    └── pages
    |   └── pages
    |       ├── page1
    |       |   └── test_page1.py
    |       └── page2
    └── shared
        └── models
        |   ├── test_model1.py
        |   └── test_model2.py
        └── components
            ├── test_component1.py
            └── test_component2.py
```
