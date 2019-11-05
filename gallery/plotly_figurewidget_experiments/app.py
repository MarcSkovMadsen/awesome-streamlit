"""Experiments with the new Plotly FigureWidget"""
import datetime

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from ipywidgets import widgets


def main():
    example = st.selectbox("Select a FigureWidget example", [1, 2, 3])
    if example == 1:
        example_1()
    elif example == 2:
        example_2()
    elif example == 3:
        example_3()


def example_1():
    fig = go.FigureWidget()
    fig.add_scatter(y=[2, 1, 4, 3])
    fig.add_bar(y=[1, 4, 3, 2])
    fig.layout.title = "Hello FigureWidget"

    # update scatter data
    scatter = fig.data[0]
    scatter.y = [3, 1, 4, 3]

    # update bar data
    bar = fig.data[1]
    bar.y = [5, 3, 2, 8]

    fig.layout.title.text = "This is a new title"
    st.markdown("[Reference](https://plot.ly/python/figurewidget/)")
    st.plotly_chart(fig)


def example_2():
    trace = go.Heatmap(
        z=[[1, 20, 30, 50, 1], [20, 1, 60, 80, 30], [30, 60, 1, -10, 20]],
        x=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
        y=["Morning", "Afternoon", "Evening"],
    )
    data = [trace]
    layout = go.Layout(title="Activity Heatmap")

    figure = go.Figure(data=data, layout=layout)
    f2 = go.FigureWidget(figure)
    st.plotly_chart(f2)
    st.markdown("[Reference](https://plot.ly/python/figurewidget/)")


def example_3():
    df = get_flights()
    month = widgets.IntSlider(
        value=1.0,
        min=1.0,
        max=12.0,
        step=1.0,
        description="Month:",
        continuous_update=False,
    )

    use_date = widgets.Checkbox(description="Date: ", value=True)

    container = widgets.HBox(children=[use_date, month])

    textbox = widgets.Dropdown(
        description="Airline:   ", value="DL", options=df["carrier"].unique().tolist()
    )

    origin = widgets.Dropdown(
        options=list(df["origin"].unique()), value="LGA", description="Origin Airport:"
    )

    # Assign an empty figure widget with two traces
    trace1 = go.Histogram(x=df["arr_delay"], opacity=0.75, name="Arrival Delays")
    trace2 = go.Histogram(x=df["dep_delay"], opacity=0.75, name="Departure Delays")
    g = go.FigureWidget(
        data=[trace1, trace2],
        layout=go.Layout(title=dict(text="NYC FlightDatabase"), barmode="overlay"),
    )
    st.plotly_chart(g)

    def validate():
        if (
            origin.value in df["origin"].unique()
            and textbox.value in df["carrier"].unique()
        ):
            return True
        else:
            return False

    def response(change):
        if validate():
            if use_date.value:
                filter_list = [
                    i and j and k
                    for i, j, k in zip(
                        df["month"] == month.value,
                        df["carrier"] == textbox.value,
                        df["origin"] == origin.value,
                    )
                ]
                temp_df = df[filter_list]

            else:
                filter_list = [
                    i and j
                    for i, j in zip(df["carrier"] == "DL", df["origin"] == origin.value)
                ]
                temp_df = df[filter_list]
            x1 = temp_df["arr_delay"]
            x2 = temp_df["dep_delay"]
            with g.batch_update():
                g.data[0].x = x1
                g.data[1].x = x2
                g.layout.barmode = "overlay"
                g.layout.xaxis.title = "Delay in Minutes"
                g.layout.yaxis.title = "Number of Delays"

    origin.observe(response, names="value")
    textbox.observe(response, names="value")
    month.observe(response, names="value")
    use_date.observe(response, names="value")

    container2 = widgets.HBox([origin, textbox])
    fig = widgets.VBox()
    st.plotly_chart(fig)
    st.markdown("[Reference](https://plot.ly/python/figurewidget-app/)")
    go.FigureWidget.


def get_flights():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/yankev/testing/master/datasets/nycflights.csv"
    )
    df = df.drop(df.columns[[0]], axis=1)
    return df


main()
