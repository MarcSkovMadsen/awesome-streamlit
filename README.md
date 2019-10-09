# Awesome Streamlit [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesome-streamlit)

The purpose of this project is to share knowledge on how Awesome [Streamlit](https://streamlit.io/) is and can become. [Pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls) are very welcome!

Streamlit has just been [announced](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace) (Oct 2019) but I see the potential of becoming the Iphone of Data Science Apps. And maybe it can even become the Iphone of Technical Writing, Code, Micro Apps and Python.

This project will consist of 3 things

- A unofficial and curated [list](https://github.com/MarcSkovMadsen/awesome-streamlit#awesome-resources) of Awesome Streamlit **resources**. See below.
- An [article](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/AWESOME-STREAMLIT.md) on the **vision** of how awesome Streamlit is and can become.
- An [**awesome Streamlit application**](https://awesome-streamlit.azurewebsites.net/) to accompany the article and to act as **inspiration for building and deploying awesome, multipage Streamlit apps**.

## Awesome Resources

A curated list of awesome streamlit resources. Inspired by [awesome-python](https://github.com/vinta/awesome-python) and [awesome-pandas](https://github.com/tommyod/awesome-pandas).

### Official Resources

- [Streamlit.io](https://streamlit.io/)
- [Streamlit Docs](https://streamlit.io/docs/)
- [Streamlit Community](https://discuss.streamlit.io/top/quarterly)

### What started this project

- [The announcing blog](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace)
- [The announcing community post](https://discuss.streamlit.io/t/streamlit-has-launched/105/3)
- [LinkedIn Discussion](https://www.linkedin.com/feed/update/urn:li:activity:6586497522896818176/?commentUrn=urn%3Ali%3Acomment%3A(activity%3A6585883899514146816%2C6586497466957385728))

### Follow the excitement

- [LinkedIn](https://www.linkedin.com/search/results/all/?keywords=%23streamlit)
- [Twitter](https://twitter.com/search?q=%23streamlit&src=typed_query)

### Awesome Applications

- [SpacyIO Application](https://gist.github.com/ines/b320cb8441b590eedf19137599ce6685)
- [Kaggle Mushrooms Dashboard](https://github.com/pierpaolo28/Data-Visualization/tree/master/Streamlit)

## Governance

This repo is maintained by me :-)

I'm Marc, Skov, Madsen, PhD, CFA®, Lead Data Scientist Developer at [Ørsted](https://orsted.com)

You can find my contact details at [datamodelsanalytics.com](https://datamodelsanalytics.com)

I try my best to govern and maintain this project in the spirit of the [Zen of Python](https://www.python.org/dev/peps/pep-0020/).

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
- add your code in a new `your_app_name.py` file in the `src/pages` folder.
  - If your code is large feel free to add a `your_app_name` folder of files instead.
- add the `your_app_name` to the
  - [src/pages/__init__.py](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/src/pages/__init__.py) file.
  - list of PAGES in the [src/app.py](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/src/app.py).
- update the [requirements.txt](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/requirements.txt) file.
    Please specify the required version.
- Manually test your contribution

Finally you need to make sure all automated tests pass by running

```bash
invoke test.all
```

Please note that your app should not require high compute power as we are running this on the cheapest pricing tier available on Azure.

Feel free to reach out if you have comments, questions or need help.

Thanks.

### How to sponsor this project

If you would like to sponsor my time or the infrastructure the platform is running on feel free to reach out via [datamodelsanalytics.com](https://datamodelsanalytics.com).

Thanks

## LICENSE

[MIT](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/LICENSE.md)

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
- [Git-sci](https://git-scm.com/downloads)

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

The final thing to do is to install the local requirements

```bash
pip install -r requirements_local.txt
```

### Run the Application

```bash
streamlit run src/pages/app.py
```

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

### Project Layout

The basic layout of a application is as simple as

```bash
.
└── src
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
└── src
    ├── app.py
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

We place our tests in a `test` folder in the root folder organized with folders similar to the `src` folder and file names with a `test_` prefix.

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
