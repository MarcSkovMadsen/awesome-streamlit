"""This example is a Streamlit implementation of an interactive Country Indicators app.

The purpose of this example is to test what we can do and cannot (yet) do in Streamlit compared
to [Voila](https://github.com/voila-dashboards/voila) and
list how the development experience and the end result compares

The benchmark example from Voila is
[https://github.com/voila-gallery/voila-gallery-country-indicators]
(https://github.com/voila-gallery/voila-gallery-country-indicators)

Author: Marc Skov Madsen https://github.com/marcskovmadsen

"""
import pandas as pd
import streamlit as st
import plotly.express as px


DATA_PATH = "package/awesome_streamlit/app/pages/contributions/voila_country_indicators/country_indicators.csv"
DATA_URL = "https://gist.githubusercontent.com/chriddyp/cb5392c35661370d95f300086accea51/raw/8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/indicators.csv"

EXPLANATION = """\
<div class="app-sidebar">
<p><em>Compare different development indicators.</em><p>

<p>Select what indicators to plot in the dropdowns, and use the slider
to sub-select a fraction of years to include in the plot.</p>

<p>Data and idea copied from the <a href="https://dash.plot.ly/getting-started-part-2">
Plotly Dash documentation</a>.</p>

<p>This example demonstrates combining Plotly with Streamlit widgets.
</div>
"""


def write():
    intro_section()
    streamlit_section()
    voila_section()
    findings_section()


def streamlit_section():
    st.markdown(
        """
## Plot - Streamlit

"""
    )
    App.from_url(DATA_PATH)


def voila_section():
    st.markdown(
        """
## Plot - Voila

![Executing 3 of 6 spinner](voila_executing_3_of_6)

We compare to the Country Indicator app in the Voila Gallery.
Click [here](https://github.com/voila-gallery/voila-gallery-country-indicators) to see the source.

![Voila country indicators](voila_country_indicators.png)
"""
    )


def intro_section():
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


def findings_section():
    st.markdown(
        """
## Findings

### Pros of Voila

- The label and widget are independent. I.e. you don't have to have a label.
- There is a built in IntRangeSelector widget.

### Pros of Streamlit

- The label is a part of the widget. I.e. the developer will not forget to put on a label.
- You can use your **editor of choice**
  - Streamlit does not require knowing something like how to install and use a notebook editor.
  - You you can use integrated, automatic tests like pylint, mypy etc. to help  produce quality code.
- Very fast and **simple development cycle** of develop-test-refactor
because of very fast, automatic hot reload and ease of navigation in editor.
- End result is a **code file** that works very well with Git.
- End result comes with a **multiuser, production ready server** out of the box.

### Issues

- Streamlit:
  - [@st.cache @classmethod issue 481](https://github.com/streamlit/streamlit/issues/481)
  - [No Grid issues](https://github.com/streamlit/streamlit/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+grid)
  - Plotly_chart and slider overlap
"""
    )


class App:
    def __init__(self, df):
        self._df = df.copy(deep=True)
        st.sidebar.markdown(EXPLANATION, unsafe_allow_html=True)
        available_indicators = self._df["Indicator Name"].unique()
        x_indicator = st.selectbox("Select indicator x", available_indicators, 0)
        y_indicator = st.selectbox("Select indicator y", available_indicators, 1)
        plotly_chart = st.empty()
        st.markdown("<br><br>", unsafe_allow_html=True)
        min_value = min(df["Year"])
        max_value = max(df["Year"])
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
    def _get_dataframe(cls, url):
        return pd.read_csv(url)

    @classmethod
    def from_url(cls, url) -> "App":
        df = cls._get_dataframe(url)
        return cls(df)

    def _create_plot(self, x_indicator, y_indicator, year_range):
        df = self._df[self._df["Year"].between(*year_range)]
        xs = df[df["Indicator Name"] == x_indicator]
        ys = df[df["Indicator Name"] == y_indicator]

        dataframe = pd.merge(xs, ys, how="inner", on=["Country Name", "Year"])
        title = f"Country Indicators"
        fig = px.scatter(dataframe, x="Value_x", y="Value_y", title=title)
        fig.update_layout(dict(xaxis=dict(title=dict(text=x_indicator))))
        fig.update_layout(dict(yaxis=dict(title=dict(text=y_indicator))))
        return fig


def range_selectbox(label, min_value: int, max_value: int):
    selection_min = st.slider(f"Select min {label}", min_value, max_value)
    selection_max = st.slider(f"Select max year {label}", min_value, max_value)
    return range(selection_min, selection_max)


write()
