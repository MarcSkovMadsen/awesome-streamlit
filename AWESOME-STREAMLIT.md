# Awesome Streamlit [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesome-streamlit)

## Disclaimer

THE BELOW IS VERY PRELIMINARY AND RAPIDLY DEVELOPING! IT'S A VISION and a HYPOTHESIS. NOT FACTS! MIGHT CHANGE A LOT.

I JUST DISCOVERED [JUPYTER VOILA](https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93) WHICH MIGHT BE AN ALTERNATIVE. I DO NOT KNOW HOW THAT COMPARES. I WILL DESCRIBE THAT BELOW ASAP.

## Introduction

This article will discuss if [Streamlit](https://streamlit.io/) is awesome and how awesome it can be.

Streamlit is announced as being **[The fastest way to build custom ML tool](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace)** but we believe it has the potential to become **much more awesome** than that.

[![Streamlit Video](https://miro.medium.com/max/700/1*p3XPm-x0TUIuMmQQa4mjHQ.gif)](https://miro.medium.com/max/700/1*p3XPm-x0TUIuMmQQa4mjHQ.gif)

The best way to think about the arrival of Streamlit is to think of the **arrival of the Iphone** being announced as **the smartest way to place calls and send text messages**. Well yes :-). But now we can see that it's a powerfull compute engine and an ecosystem of apps that has changed peoples lifes.

Streamlit has just arrived (Oct 2019). So it's too early tell if Streamlit will become truly awesome.

But we see the **potential to become the Iphone of Data Science, Technical Writing, Micro Apps, Code, Python and more**. It has the potential to change the way we share knowledge and create tools and applications because it's so plain simple to use.

This article was inspired by a reply in this [post on LinkedIn](https://www.linkedin.com/posts/marcskovmadsen_turn-python-scripts-into-beautiful-ml-tools-activity-6585883899514146816-OonG) and some replies to the announcement in the [Streamlit Community](https://discuss.streamlit.io/t/streamlit-has-launched/105/5).

You can find a curated list of Awesome Streamlit resources [here](https://github.com/MarcSkovMadsen/awesome-streamlit)

## Contribute

Feel free to contribute your comments or suggestions to to this article.

You can contribute through GitHub [Issues](https://github.com/MarcSkovMadsen/awesome-streamlit/issues) or [Pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls).

## Data Science

Data Science is a very broad category. It's used for to categorize work such as

- data transformations and visualisations in excel
- interactive data visualisations in BI Tools like Power BI and Tableau
- Building Fundamental, Statistical, Mathematical, Machine Learning or Deeplearning models in Python, R etc.
- Building applications on top of data science models and deploying them to production using web frameworks such as Bokeh/ Dash, Flask/ Django and React/Vue/Angular.

and much more

But actually every body extracting, transforming, loading and presenting data are actually doing work very similar to data scientists. If they are very structured about it and using methodologies from software development they are called Data Engineers, ML Engineers or Platform Engineers :-)

### Notebooks

#### Notebooks - Situation

One of the revolutionary tools of modern data science is the [Jupyter Notebook](https://jupyter.org/).

[![Awesome](https://jupyter.org/assets/jupyterpreview.png)](https://github.com/MarcSkovMadsen/awesome-streamlit)

The jupyter notebook provides an environment for working very exploratory and visually within data science

#### Notebooks - Problem

A jupyter notebook cannot really be deployed directly to production and the users.

So Notebooks do not facilitate rapid sharing, exploration, testing and improvement cycle you would like.

Bottom line. **Notebooks makes deployment of data science products costly**.

#### Notebooks - Complication

The pains of the Jupyter Notebook are

- The Notebook is not as productive a development environment as an Editor or IDE.
- The Notebook workflow tends to lead to code that is poorly written and/ or is difficult to reproduce.
- The Notebook cannot really be deployed to production and shared with users as an application. You can distribute it as pdf or html. But most often it will be refactored into a code library or an application by a team of developers.
- for more see [this](https://www.youtube.com/watch?v=7jiPeIFXb6U) video by Guss Allen.

Jupyter has tried to develop a more productive development environment called [Jupyter Labs](https://towardsdatascience.com/jupyter-lab-evolution-of-the-jupyter-notebook-5297cacde6b).

But this environment also has it's pains.

- It's still not as productive or extensible as a real editor like VS Code or Pycharm.
- It changes the Notebook from being a simple interactive document that you can read and distribute as pdf or html to an advanced but complicated development environment that you work in.

#### Notebooks even more complicated

Jupyter recently (Jun 2019) [announced](https://blog.jupyter.org/and-voil%C3%A0-f6a2c08a4a93) Voila which can transform Jupyter notebooks to standalone applications and dashboards.

The approach is different than that of Streamlit. I have not yet tried Voila.

But for now I believe that the code in your editor, use caching and only transfer incremental data of Streamlit is a very strong and unique approach. Also the magical api of Streamlit is different but very, very simple to use.

Whether Streamlit can compete with the massive popularity and library of widgets of Jupyter is yet to be seen. Or whether Voila will quickly learn from Streamlit.

See [Hacker News Discussion](https://news.ycombinator.com/item?id=21158487) for a little bit of technical discussion.

More to come

#### Notebooks - Solution

Streamlit aims to solve all of the problems described above as described in the  [Announcement](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace).

[![Streamlit Video](https://miro.medium.com/max/700/1*p3XPm-x0TUIuMmQQa4mjHQ.gif)](https://miro.medium.com/max/700/1*p3XPm-x0TUIuMmQQa4mjHQ.gif)

As you can see on the image above it simplifies everything by enabling data scientist to

- develop applications in just one python file (left side of image)
- using their editor of choice (VS Code on left side of image)
- producing a web application that can very easily be deployed to production. (right side of image)

And the application can provide the interactivity that you would normally be developing using a modern web framework as React, Vue or Angular. So **a single data scientist can develop a data science application in hours**. **No large project or team required**.

Streamlit provides **self service data science**.

And it's **very appealing to data scientists** as they can develop an application in the way they find simple, productive and fun

- Text as MarkDown
- Code in Python
- All of your data science modelling libraries at hand like Pandas, SciKitLearn, PyTorch, Keras, TensorFlow etc.
- All of your data science visualisation libraries at hand like  Matplotlib, Vega and Plotly.
- No HTML and No Javascript is required.

I believe that the **Jupyter Notebook is a cell phone** and **Streamlit is the Iphone** of Data Science

## Notebooks - Implications

For building data science applications

- business should start investigating Streamlit and Jupyter Voila
- There will be a lot less demand for front end developers and development in React, Vue an Angular in data science.
  - The remaining front end developers in data science should be developing specialized Web Components for Streamlit when needed.
- There will be less demand for back end developers to develop REST APIs etc. for data science products.
- Streamlit is so simple to use that business users across an enterprise can create apps them selves. It's the democratization of Data Science Apps.
  - Actually we believe the development cycle will be
    - Business users and data scientists develop data science apps independently or together and deploy to production.
    - The most valuable apps will be identified and the quality and governance of these apps will be improved and maintained. They will get an approval as Enterprise Ready apps. But probably as this is so simple and there is revision control and pull requests Business Users and Data Scientist will be able to continue the development of these apps.
- Business should start experimenting with this technology to find it's use cases and limits and evaluate how and when to start using Streamlit securely.
  - As **time to market** is so important you should **start moving!**.
- IT departments should
  - Describe their way of securely deploying these applications to on-premise or cloud and
  - join the [one-click deployment solution for Teams](https://streamlit.io/forteams/) beta.

For building larger, traditional applications with data science app components the data science app components can in a lot of cases be build in Streamlit and embedded in the larger application. REST API endpoints should still be developed when the need is there.

### Notebooks - Disclaimer

Streamlit is very new. There will be rough edges and things you cannot yet do. And maybe it turns out the product is not secure or something else. Who knows? But as the principles and api of Streamlit is so simple and productive we believe they will be developed and fixed very rapidly.

Things you cannot do yet

- Select from thousands of web components to make your application interactive.
  - The basic ones are there
- Deploy to production with one click.
  - It can be deployed as any other python web application. And it's only one file, the streamlit package and any data science packages needed. So it's very simple to deploy one you have done it once.

More to come

### Spreadsheets

As Streamlit apps are so simple, the quality so high and robust and it enjoys the power of Python a lot business users will transform from developing spreadsheets into developing Streamlit application.

#### Spreadsheets - Implications

- Train your business users in Python and Streamlit.
- Help your business users install Python and Python packages.
- Help your business users govern their projects and how to use revision control.

I believe a Spreadsheet wrapper for Streamlit removing these pain points will be provided soon as it will be so easy to setup on top of Streamlit.

### BI Visualization Tools

Another category of revolutionary tools for data science are data reporting and visualization tools like Power BI and Tableau.

### BI Visualization Tools - Problem

- Difficult or impossible to do model visualization.
- Hard to maintain using good software developing techniques because you do not develop code. - Does not enjoy the power of Python.

But it's still a very strong drag and drop 1-click deployment tool for data visualization.

### Bokeh


### Dash

Problem: You still need to master HTML and manage callbacks. Focus on Plotly charts mainly. The development cycle is slow. The api is not "magical".

Implications:

For some use case where you wan't a high degree of flexibility in layout and formatting, you might still need Dash.

### Flask and Django

Problem: So many layers of abstraction to master. The api is not "magical".

### React, Vue and Angular

Implications:

### Binder

Not needed?

## Technical Writing

Something like [this](https://insights.stackoverflow.com/survey/2019) and [this](https://streamlit.io/docs/api.html) will be so easy to develop in Streamlit.

## Code

Streamlit lowers the barrier to entry for young and new programmers. One file in an editor is all that is needed to develop a powerfull app. Somebody will abstract away the rest in a cloud solution.

## Micro Apps

When you can build something like this is a few hours you know something will change.

[Video](https://twitter.com/i/status/1179155259819806721)

You can find the code [here](https://gist.github.com/ines/b320cb8441b590eedf19137599ce6685).
See the original tweet [here](https://twitter.com/_inesmontani/status/1179155259819806721?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1179155259819806721&ref_url=https%3A%2F%2Fpublish.twitter.com%2F%3Fquery%3Dhttps%253A%252F%252Ftwitter.com%252F_inesmontani%252Fstatus%252F1179155259819806721%26widget%3DTweet)

## Python

Streamlit reduces the barrier to entry and enables even more people to enjoy the power of Python.

## More

To come
