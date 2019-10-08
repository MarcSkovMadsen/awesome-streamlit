# Awesome Streamlit [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesome-streamlit)

The purpose of this project is to share knowledge on how Awesome Streamlit can become.

I believe that [Streamlit](https://streamlit.io/) is truly awesome.

Streamlit is very new (Oct 2019) but we see the potential of being the Iphone of Data Science, Technical Writing, Code, Micro Apps, Python and more.

This project will consist of 3 things

- A [list](https://github.com/MarcSkovMadsen/awesome-streamlit#awesome-resources) of Awesome Streamlit resources. See below.
- An [article](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/AWESOME-STREAMLIT.md) on the vision of how awesome Streamlit is.
- An **Awesome Streamlit Application** to accompany the article and to illustrate and share the knowledge of how Awesome Streamlit is.
  - Of course it will be built in Streamlit.

## Awesome Resources

A curated list of awesome streamlit resources.

Inspired by [awesome-python](https://github.com/vinta/awesome-python).

### Official Resources

- [Streamlit.io](https://streamlit.io/)
- [Streamlit Docs](https://streamlit.io/docs/)
- [Streamlit Community](https://discuss.streamlit.io/top/quarterly)

### What started this project

- [The announcing blog](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace)
- [The announcing community post](https://discuss.streamlit.io/t/streamlit-has-launched/105/3)
- [LinkedIn Discussion](https://www.linkedin.com/feed/update/urn:li:activity:6586497522896818176/?commentUrn=urn%3Ali%3Acomment%3A(activity%3A6585883899514146816%2C6586497466957385728))

### Follow the excitement

- [LinkedIn](https://www.linkedin.com/search/results/all/?authorCompany=%5B%5D&authorIndustry=%5B%5D&contactInterest=%5B%5D&facetCity=%5B%5D&facetCompany=%5B%5D&facetConnectionOf=%5B%5D&facetCurrentCompany=%5B%5D&facetCurrentFunction=%5B%5D&facetGeoRegion=%5B%5D&facetGroup=%5B%5D&facetGuides=%5B%5D&facetIndustry=%5B%5D&facetNetwork=%5B%5D&facetNonprofitInterest=%5B%5D&facetPastCompany=%5B%5D&facetProfessionalEvent=%5B%5D&facetProfileLanguage=%5B%5D&facetRegion=%5B%5D&facetSchool=%5B%5D&facetSeniority=%5B%5D&facetServiceCategory=%5B%5D&facetState=%5B%5D&groups=%5B%5D&keywords=%23streamlit&origin=GLOBAL_SEARCH_HEADER&page=1&refresh=false&skillExplicit=%5B%5D&topic=%5B%5D)
- [Twitter](https://twitter.com/search?q=%23streamlit&src=typed_query)

### Awesome Applications

- [SpacyIO Application](https://gist.github.com/ines/b320cb8441b590eedf19137599ce6685)
- [Kaggle Mushrooms Dashboard](https://github.com/pierpaolo28/Data-Visualization/tree/master/Streamlit)

## Governance

This repo is maintained by me :-)

I'm Marc, Skov, Madsen, PhD, CFA, Lead Data Scientist Developer at [Ørsted](https://orsted.com)

You can find my contact details at [datamodelsanalytics.com](https://datamodelsanalytics.com)

I find guidance in the [Zen of Python](https://www.python.org/dev/peps/pep-0020/).

## Contribute

Feel free to contribute to this project.

You can contribute your thoughts or code through the GitHub [Issues](https://github.com/MarcSkovMadsen/awesome-streamlit/issues) or [Pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls) functionality.

If you are passionate about Streamlit and would like to join as a Core Maintainer feel free to reach out via [datamodelsanalytics.com](https://datamodelsanalytics.com)

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
