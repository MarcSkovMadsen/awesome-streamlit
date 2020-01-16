"""This example is a Streamlit implementation of an interactive Country Indicators app.

The purpose of this example is to test what we can do and cannot (yet) do in Streamlit compared
to [Voila](https://github.com/voila-dashboards/voila) and
list how the development experience and the end result compares

The benchmark example from Voila is
[https://github.com/voila-gallery/voila-gallery-country-indicators]
(https://github.com/voila-gallery/voila-gallery-country-indicators)

Author: Marc Skov Madsen https://github.com/marcskovmadsen

"""
import pathlib
from typing import Tuple

import pandas as pd
import plotly.express as px
import streamlit as st

DATA_LOCAL = pathlib.Path(__file__).parent / "country_indicators.csv"

DATA_URL = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/package/"
    "awesome_streamlit/app/pages/contributions/country_indicators/country_indicators.csv"
)
DATA_ORIGINAL = (
    "https://gist.githubusercontent.com/chriddyp/cb5392c35661370d95f300086accea51/"
    "raw/8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/indicators.csv"
)

EXPLANATION = """
## Compare different development indicators.

Select what indicators to plot in the dropdowns, and use the slider
to sub-select a fraction of years to include in the plot.

Data and idea copied from the
[Plotly Dash documentation](https://dash.plot.ly/getting-started-part-2)

This example demonstrates combining Plotly with Streamlit widgets.
"""


def main():
    """This is the main component. Run this to start the app."""
    intro_section()
    streamlit_section()
    voila_section()
    findings_section()


def intro_section():
    """This section introduces the app"""
    st.markdown(
        """
# Country Indicators

## Introduction

This example is a Streamlit implementation of an interactive Country Indicator plot.

The purpose of this example is to test what we can do and cannot (yet) do in Streamlit compared
to the combination of [Jupyter Notebook](https://jupyter.org/) and [Voila](https://github.com/voila-dashboards/voila).


As of today (2019-10-20) both Voila and Streamlit are released for Beta Testing only.
"""
    )


def streamlit_section():
    """This section controls the Streamlit Country Indicators App"""
    st.markdown(
        """
## Country Indicators - Streamlit version

"""
    )
    App.create_from_url(DATA_URL, DATA_LOCAL)


def voila_section():
    """This section controls the Voila Reference Country Indicators App"""
    st.markdown(
        """
## Country Indicators - Voila Version

We compare to the Country Indicator app in the Voila Gallery.
**Click the image**  to see the **source**.

[![Voila country indicators](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/gallery/country_indicators/voila_country_indicators.png?raw=true)](https://github.com/voila-gallery/voila-gallery-country-indicators)

Voila also shows a nice spinner by it self while running some of the cells

![Executing 3 of 6 spinner](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/gallery/country_indicators/voila_executing_3_of_6.png?raw=true)
"""
    )


def findings_section():
    st.markdown(
        """
## Findings

### Pros of Voila

- The **image updates very, very fast** when changing a selection
- The **label and widget are independent**.
I.e. you don't have to have a label if you need a more compact layout.
- How to get a **range slider is very explicit**, i.e. IntRangeSlider.
- You can have columnar and row layout with **HBox and VBox**
- It's ok to **style** via HTML and <style> tags

### Pros of Streamlit

- There is an easy to use **sidebar**
- The **label is a part of the widget**. I.e. the developer will not forget to put on a label.
- You can use your **editor of choice**
  - Streamlit does not require knowing something like how to install and use a notebook editor.
  - You you can use integrated, automatic tests like pylint, mypy etc. to help  produce quality code.
- Very fast and **simple development cycle** of develop-test-refactor
because of very fast, automatic hot reload and ease of navigation in editor.
- End result is a **code file** that works very well with Git.
- End result comes with a **multiuser, production ready server** out of the box.

### Issues

- Streamlit:
  - [Performance issue 494](https://github.com/streamlit/streamlit/issues/494)
  - [Streamlit crashes when using MatPlotLib issue 469](https://github.com/streamlit/streamlit/issues/469)
  - [Compact and Dashboard layout needed issue 486](https://github.com/streamlit/streamlit/issues/486)
  - [No Grid issues](https://github.com/streamlit/streamlit/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+grid)
  - [@st.cache @classmethod issue 481](https://github.com/streamlit/streamlit/issues/481)
  - [slider range method is not 'obvious' issue 482](https://github.com/streamlit/streamlit/issues/482)
  - [Plotly_chart and slider overlap issue 379](https://github.com/streamlit/streamlit/issues/379)
"""
    )


class App:
    """The Voila reference example is implemented as an App. Thus we do the same for Streamlit"""

    def __init__(self, df):
        self._df = df.copy(deep=True)  # Deep copy to avoid st.cache problems
        available_indicators = self._df["Indicator Name"].unique()
        min_value = min(df["Year"])
        max_value = max(df["Year"])

        st.sidebar.markdown(EXPLANATION, unsafe_allow_html=True)
        x_indicator = st.selectbox("Select indicator x", available_indicators, 0)
        y_indicator = st.selectbox("Select indicator y", available_indicators, 1)
        plotly_chart = st.empty()

        # Hack to seperate plot and slider
        st.markdown("<br><br>", unsafe_allow_html=True)
        year_range = st.slider(
            "Select min and max Year",
            min_value=min_value,
            max_value=max_value,
            value=[min_value, max_value],
        )

        fig = self._create_plot(x_indicator, y_indicator, year_range)
        plotly_chart.plotly_chart(fig)

    @classmethod
    @st.cache
    def _get_dataframe(cls, url) -> pd.DataFrame:
        """Return the dataframe of country indicators"""
        return pd.read_csv(url)

    @classmethod
    def create_from_url(cls, url: str, local: pathlib.Path) -> "App":
        """Creates an instance of the App with data from the url"""
        if local.exists():
            df = cls._get_dataframe(local)
        else:
            df = cls._get_dataframe(url)
            df.to_csv(local, index=False)  # We save it to speed up load times next time
        return cls(df)

    def _create_plot(
        self, x_indicator: str, y_indicator: str, year_range: Tuple[int, int]
    ) -> "plotly.Fig":
        """Creates a Plotly plot for the specified selections"""
        df = self._df[self._df["Year"].between(*year_range)]
        xs = df[df["Indicator Name"] == x_indicator]
        ys = df[df["Indicator Name"] == y_indicator]

        dataframe = pd.merge(xs, ys, how="inner", on=["Country Name", "Year"])
        title = f"Country Indicators"
        fig = px.scatter(dataframe, x="Value_x", y="Value_y", title=title, height=400)
        fig.update_layout(dict(xaxis=dict(title=dict(text=x_indicator))))
        fig.update_layout(dict(yaxis=dict(title=dict(text=y_indicator))))
        return fig


main()
