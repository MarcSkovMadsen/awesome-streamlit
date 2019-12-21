"""# Kickstarter Dashboard

The purpose of the Kickstarter Dashboard is to test if the claims regarding Bokeh as of Jan 2018 in
the [bokeh-dash-best-dashboard-framework]
(https://www.sicara.ai/blog/2018-01-30-bokeh-dash-best-dashboard-framework-python)
article holds for [Panel](https://panel.pyviz.org/) and the [HoloViews](http://holoviews.org/)
suite of tools as of Dec 2019.

Panel is an alternative frawework to Streamlit for building awesome analytics apps in Python.
It uses the [Bokeh](https://docs.bokeh.org/en/latest/) server as a backend server.

You can find the alternative version of this Dashboard in Panel at
[awesome-panel.org](https://awesome-panel.org)

Here you find an implementation in Streamlit so that you can compare and contrast the frameworks.
"""
import pathlib
from typing import List, Optional

import holoviews as hv
import hvplot.pandas  # pylint: disable=unused-import
import pandas as pd
import panel as pn
import param
import streamlit as st

COLUMNS = ["created_at", "usd_pledged", "state", "category_slug"]
DATE_COLUMNS = ["created_at"]
N_SAMPLES = 10000
CMAP = {"canceled": "blue", "failed": "red", "successful": "green", "suspended": "orange"}

INFO = """\
Please note that zooming on the parent, scatter chart and having the child, bar chart update
accordingly is not currently not possible in Streamlit. Instead you can use the Sliders in the
sidebar to zoom.
"""

SEARCH_PATHS = [
    pathlib.Path(__file__).parent / "kickstarter-cleaned.csv",
    pathlib.Path(__file__).parent / "kickstarter_dashboard" / "kickstarter-cleaned.csv"
]
if SEARCH_PATHS[0].exists():
    KICKSTARTER_PATH = str(SEARCH_PATHS[0])
elif SEARCH_PATHS[1].exists():
    KICKSTARTER_PATH = str(SEARCH_PATHS[1])
else:
    KICKSTARTER_PATH = (
        "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/"
        "gallery/kickstarter_dashboard/kickstarter-cleaned.csv"
    )


@st.cache()
def get_kickstarter_df() -> pd.DataFrame:
    """The Source DataFrame of Kickstarter Data

    Returns:
        pd.DataFrame -- The Source DataFrame of Kickstarter Data
    """
    return KickstarterDashboard.get_kickstarter_df()


@st.cache()
def get_categories() -> List[str]:
    """The list of all broader categories

    Returns:
        List[str] -- A list of all broader categories
    """
    return KickstarterDashboard.get_categories(get_kickstarter_df())


def main():
    """A Reactive View of the KickstarterDashboard"""
    kickstarter_df = get_kickstarter_df()
    kickstarter_dashboard = KickstarterDashboard(kickstarter_df=kickstarter_df)
    st.markdown(__doc__)
    st.info(INFO)

    options = get_categories()
    categories_selected = st.multiselect("Select Categories", options=options)
    if not categories_selected and kickstarter_dashboard.categories:
        kickstarter_dashboard.categories = []
    else:
        kickstarter_dashboard.categories = categories_selected

    st.sidebar.title("Selections")
    x_range = st.sidebar.slider("Select create_at range", 2009, 2018, (2009, 2018))
    y_range = st.sidebar.slider("Select usd_pledged", 0.0, 5.0, (0.0, 5.0))
    filter_df = KickstarterDashboard.filter_on_categories(kickstarter_df, categories_selected)
    filter_df = kickstarter_dashboard.filter_on_ranges(
        filter_df, (pd.Timestamp(x_range[0], 1, 1), pd.Timestamp(x_range[1], 12, 31)), y_range
    )
    kickstarter_dashboard.scatter_df = filter_df

    st.bokeh_chart(hv.render(kickstarter_dashboard.scatter_plot_view()))
    st.bokeh_chart(hv.render(kickstarter_dashboard.bar_chart_view()))


# The KickStarterDashboard is a copy paste from
# https://github.com/MarcSkovMadsen/awesome-panel/tree/master/src/pages/gallery/kickstarter_dashboard
# which is deployed at https://awesome-panel.org
class KickstarterDashboard(param.Parameterized):
    # pylint: disable=line-too-long
    """The purpose of the Kickstarter Dashboard is to test if the claims regarding Bokeh as of Jan 2018 in the
[bokeh-dash-best-dashboard-framework](https://www.sicara.ai/blog/2018-01-30-bokeh-dash-best-dashboard-framework-python)
article holds for Panel and the HoloViews suite of tools as of Dec 2019.

The claims where

- Data in Bokeh becomes inconsistent
- Cannot link charts to dataframe
- Bokeh is slow for big datasets
- Interactions take a long time to develop

You can evaluate this dashboard and the code to make your personal evaluation of the above
statements.

My evaluation is

- the **first two statements does no longer hold**.
- The third is up for discussion. I would also like the Dashboard updates to be a bit faster. Maybe it's because I don't yet know how to implement this efficiently.
- The fourth I've also experienced
see this [discussion](https://discourse.holoviz.org/t/how-to-create-a-parameterized-dashboard-with-seperation-between-data-transforms-and-data-views/53/13).

I can see that I made a lot of mistakes because it takes time for me to understand how the api works.
There is a lot to I need to learn across the HoloViz suite of tools.
"""
    # pylint: enable=line-too-long
    kickstarter_df = param.DataFrame()
    categories = param.ListSelector()
    scatter_df = param.DataFrame()
    bar_df = param.DataFrame()
    rangexy = param.ClassSelector(class_=hv.streams.RangeXY, default=hv.streams.RangeXY())

    def __init__(self, kickstarter_df: Optional[pd.DataFrame], *args, **kwargs):
        if not isinstance(kickstarter_df, pd.DataFrame):
            kickstarter_df = self.get_kickstarter_df()

        categories = self.get_categories(kickstarter_df)

        self.param.kickstarter_df.default = kickstarter_df
        self.param.categories.default = categories
        self.param.categories.objects = categories
        self.param.scatter_df.default = kickstarter_df
        self.param.bar_df.default = kickstarter_df

        super().__init__(*args, **kwargs)

    @param.depends("kickstarter_df", "categories", watch=True)
    def _set_scatter_df(self):
        self.scatter_df = self.filter_on_categories(self.kickstarter_df, self.categories)

    @param.depends("scatter_df")
    def scatter_plot_view(self):
        """A Reactive View of the scatter plot"""
        # Potential Improvements
        # Rename columns to Capitalized without under score
        # Add name of movie to hover tooltip
        scatter_plot = self.get_scatter_plot(self.scatter_df)
        # Please note that depending on how the scatter_plot is generated it might be a Scatter
        # or Ndoverlay objects
        # In the first case use scatter_plot. In the second case use scatter_plot.last
        self.rangexy.source = scatter_plot.last
        return scatter_plot

    @param.depends("scatter_df", "rangexy.x_range", "rangexy.y_range", watch=True)
    def _set_bar_df(self):
        """Update the bar_df dataframe"""
        self.bar_df = self.filter_on_ranges(
            self.scatter_df, self.rangexy.x_range, self.rangexy.y_range  # pylint: disable=no-member
        )

    @param.depends("bar_df")
    def bar_chart_view(self):
        """A Reactive View of the Bar Chart"""
        return self.get_bar_chart(self.bar_df)

    def view(self):
        """A Reactive View of the KickstarterDashboard"""
        return pn.Column(
            pn.pane.Markdown(__doc__),
            # InfoAlert(INFO), pn.layout.HSpacer(height=25),
            self.param.categories,
            self.scatter_plot_view,
            self.bar_chart_view,
            sizing_mode="stretch_width",
        )

    @staticmethod
    def _extract() -> pd.DataFrame:
        """Extracts the kickstarter data into a DataFrame

        Returns:
            pd.DataFrame -- A Dataframe of kickstarter data with
            columns=["created_at", "usd_pledged", "state", "category_slug"]
        """
        return pd.read_csv(KICKSTARTER_PATH, parse_dates=DATE_COLUMNS)

    @staticmethod
    def _transform(source_data: pd.DataFrame, n_samples: int = N_SAMPLES) -> pd.DataFrame:
        """Transform the data by

        - adding broader_category,
        - converting usd_pledged to millions
        - sampling to n_samples

        Arguments:
            source_data {pd.DataFrame} -- The source kickstarter data

        Returns:
            pd.DataFrame -- The transformed DataFrame with
            columns=["created_at", "usd_pledged", "state", "category_slug", "broader_category"]
        """
        source_data["broader_category"] = source_data["category_slug"].str.split("/").str.get(0)
        source_data["usd_pledged"] = source_data["usd_pledged"] / 10 ** 6
        return source_data.sample(n_samples)

    @classmethod
    def get_kickstarter_df(cls) -> pd.DataFrame:
        """The Dataframe of Kickstarter Data

        Returns:
            [pd.DataFrame] -- The Dataframe of Kickstarter Data
        """
        source_data = cls._extract()
        kickstarter_df = cls._transform(source_data)
        return kickstarter_df

    @staticmethod
    def get_categories(kickstarter_df) -> List[str]:
        """The list of kickstarter broader categories

        Arguments:
            kickstarter_df {[type]} -- [description]

        Returns:
            List[str] -- [description]
        """
        return list(kickstarter_df["broader_category"].unique())

    @classmethod
    def filter_on_categories(
        cls, kickstarter_df: pd.DataFrame, categories: List[str]
    ) -> pd.DataFrame:
        """Filters the kickstarter_df by the specified categories

        Arguments:
            kickstarter_df {pd.DataFrame} -- A Kickstarter Dataframe
            categories {List[str]} -- The list of broader_category in the DataFrame

        Returns:
            pd.DataFrame -- The filtered DataFrame
        """
        if categories is None or categories == []:
            categories = cls.get_categories(kickstarter_df)
        categories_filter = kickstarter_df["broader_category"].isin(categories)
        return kickstarter_df[categories_filter]

    @staticmethod
    def filter_on_ranges(kickstarter_df: pd.DataFrame, x_range, y_range) -> pd.DataFrame:
        """Filter the kickstarter_df by x_range and y_range

        Arguments:
            kickstarter_df {pd.DataFrame} -- [description]
            x_range {[type]} -- The usd_pledged range
            y_range {[type]} -- The created_at range

        Returns:
            pd.DataFrame -- The filtered DataFrame
        """
        sub_df = kickstarter_df
        if y_range:
            y_filter = (kickstarter_df["usd_pledged"] >= y_range[0]) & (
                kickstarter_df["usd_pledged"] <= y_range[1]
            )
            sub_df = sub_df[y_filter]
        if x_range:
            x_filter = (kickstarter_df["created_at"] >= x_range[0]) & (
                kickstarter_df["created_at"] <= x_range[1]
            )
            sub_df = sub_df[x_filter]
        return sub_df

    @staticmethod
    def get_scatter_plot(kickstarter_df: pd.DataFrame):  # pylint: disable=missing-return-type-doc
        """A Scatter plot of the kickstarter_df

        Arguments:
            kickstarter_df {pd.DataFrame} -- The DataFrame of kickstarter data

        Returns:
            [type] -- A Scatter plot
        """
        # Potential Improvements
        # Rename columns to Capitalized without under score
        # Add name of movie to hover tooltip
        kickstarter_df["color"] = kickstarter_df["state"]
        return kickstarter_df.hvplot.scatter(
            x="created_at",
            y="usd_pledged",
            # color="color",
            by="state",
            cmap=list(CMAP.values()),
            height=400,
            responsive=True,
            yformatter="%.1fM",
        )

    @staticmethod
    def get_bar_chart(kickstarter_df: pd.DataFrame):  # pylint: disable=missing-return-type-doc
        """A bar chart of the kickstarter_df

        Arguments:
            kickstarter_df {pd.DatacFrame} -- A DataFrame of Kickstarter data

        Returns:
            [type] -- A bar chart of the kickstarter_df
        """
        # Potential improvements
        # Sort by Number of Projects Desc to make it easier to see what large and small

        # Filter
        stacked_barchart_df = (
            kickstarter_df[["broader_category", "state", "created_at"]]
            .groupby(["broader_category", "state"])
            .count()
            .rename(columns={"created_at": "Number of projects"})
        )

        # Plot
        bar_chart = stacked_barchart_df.hvplot.bar(
            stacked=True, height=400, responsive=True, xlabel="Number of projects", cmap=CMAP
        )
        return bar_chart


main()
