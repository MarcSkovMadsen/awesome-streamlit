# Awesome Streamlit [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesomestreamlit)

The purpose of this project is to share knowledge on how Awesome Streamlit is.

We believe that [Streamlit](https://streamlit.io/) is truly awesome.

But Streamlit is so new that it's to early to tell how awesome. Maybe it's the Iphone of Code, Web Apps or Python. The future will determine.

This project will consist of 3 things

- A list of Awesome Streamlit resources. See below.
- An article on the potential of Streamlit: [Awesome Streamlit](https://github.com/MarcSkovMadsen/awesomestreamlit/blob/master/AWESOMESTREAMLIT.md)
- An Awesome Streamlit application to illustrate and share the knowledge of how Awesome Streamlit is.

## Awesome Resources

A curated list of awesome streamlit resources.

Inspired by [awesome-python](https://github.com/vinta/awesome-python).

- [The announcing blog](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace)
- [The announcing community post](https://discuss.streamlit.io/t/streamlit-has-launched/105/3)
- [streamlit.io](https://streamlit.io/)
- [Streamlit docs](https://streamlit.io/docs/)
- [Streamlit Community](https://discuss.streamlit.io/top/quarterly)

## Governance

This repo is governed by a team of *Core Developers*.

The Core Developers are guided by the [Zen of Python](https://www.python.org/dev/peps/pep-0020/).

The team of Core Developers currently consists of

- Marc Skov Madsen, [datamodelsanalytics.com](https://datamodelsanalytics.com)

## Contribute

Feel free to contribute to this project. You can contribute your thoughts or code through the GitHub [Issues](https://github.com/MarcSkovMadsen/awesomeStreamlit/issues) or [Pull requests](https://github.com/MarcSkovMadsen/awesomeStreamlit/pulls) functionality.

## LICENSE

[MIT](https://github.com/MarcSkovMadsen/awesomeStreamlit/blob/master/LICENSE.md)

## Getting Started with the Awesome Streamlit Application

THE APPLICATION IS NOT YET IMPLEMENTED

### Prerequisites

- An Operating System like Windows, OsX or Linux
- A working [Python](https://www.python.org/) installation.
  - We recommend using 64bit Python 3.7.4.
- a Shell
  - We recommend [Git Bash](https://git-scm.com/downloads) for Windows 8.1
  - We recommend [wsl](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) for For Windows 10
- an Editor
  - We recommend [VS Code](https://code.visualstudio.com/) (Preferred) or [PyCharm](https://www.jetbrains.com/pycharm/).
- a version of the project cloned from [https://github.com/MarcSkovMadsen/awesomeStreamlit.git](https://github.com/MarcSkovMadsen/awesomeStreamlit.git)

### Installation

```bash
git clone https://github.com/MarcSkovMadsen/awesomeStreamlit.git
```

```bash
cd awesomeStreamlit
```

Then you should create a virtual environment named .venv

```bash
python -m venv .venv
```

and activate the environment

```bash
source .venv/Scripts/activate
```

The final thing to do is to install the local requirements

```bash
pip install -r requirements_local.txt
```

### Project Layout

The basic layout of a application is as simple as

```bash
.
└── src
    └── app.py
```

As our application grows we need to think about the layout of our project, i.e. how we structure our files and folders. We would probably end up with something inspired by [this](https://itnext.io/choosing-a-highly-scalable-folder-structure-in-angular-d987de65ec7) blog post and the [Angular Style Guide](https://angular.io/guide/styleguide)

```bash
.
├── src
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
