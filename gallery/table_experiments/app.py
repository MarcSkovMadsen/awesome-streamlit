"""This app explores the tables of streamlit and if we could provide better tables"""
import pathlib
import zipfile

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

LOCAL_ROOT = pathlib.Path.cwd() / "gallery" / "table_experiments"
GITHUB_ROOT = "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-analytics-apps/master/gallery/table_experiments/"
ZIP_FILE_2019 = "developer_survey_2019.zip"
RESULTS_2019 = "survey_results_public.csv"
SCHEMA_2019 = "survey_results_schema.csv"

DEFAULT_NUMBER_OF_ROWS = 5
DEFAULT_NUMBER_OF_COLUMNS = 5


def main():
    st.title("Table Experiments")
    st.markdown(
        """
The purpose of this app is to explore the possibilities for showing and working
with tables in Streamlit

NOTE. THIS IS WORK IN PROGRESS. FEEL FREE TO CONTRIBUTE.
"""
    )

    results = read_results()

    st.header("Possibilities for showing and working with dataframe")
    table_type = st.radio(
        "Select table type",
        options=[
            "Streamlit dataframe",
            "Streamlit table",
            "Plotly table",
            "Slick Grid",
        ],
    )
    if table_type == "Streamlit dataframe":
        streamlit_dataframe(results)
    elif table_type == "Streamlit table":
        streamlit_table(results)
    elif table_type == "Plotly table":
        plotly_table(results)
    else:
        slick_grid(results)


def streamlit_dataframe(results):
    st.subheader("Streamlit Dataframe (st.dataframe)")
    number_of_rows, number_of_columns, style = select_number_of_rows_and_columns(
        results, key="st.dataframe"
    )
    filter_table = filter_results(results, number_of_rows, number_of_columns, style)
    st.dataframe(filter_table)

    st.markdown(
        """
Pros

- Can sort
- Can maximize
- Can transfer and display 10.000 rows and 5 columns in 3 seconds.
- Can style cells using
[dataframe.style.set_properties](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html)

Cons

- Cannot filter
- Cannot style table (including header) using [dataframe.style.set_table_styles]
(https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html)
  - Cannot change column width, aligment or similar.
- The scrollbar is *thin* and can be difficult to select/ drag.

"""
    )


def streamlit_table(results):
    st.subheader("Streamlit Table (st.table)")
    number_of_rows, number_of_columns, style = select_number_of_rows_and_columns(
        results, key="st.table"
    )
    filter_table = filter_results(results, number_of_rows, number_of_columns, style)
    st.table(filter_table)

    st.markdown(
        """
Pros

- Can transfer and display 5.000 rows and 5 columns in 5 seconds.
- Can style cells using
[dataframe.style.set_properties](https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html)

Cons

- Cannot sort or filter
- Cannot maximize
- No scrollbar
- Cannot style table (including header) using [dataframe.style.set_table_styles]
(https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html)
  - Cannot change column width, aligment or similar.


"""
    )


def plotly_table(results):
    st.header("Plotly Table (go.Table)")
    number_of_rows, number_of_columns, style = select_number_of_rows_and_columns(
        results, key="go.Table"
    )
    filter_table = _filter_results(results, number_of_rows, number_of_columns)

    header_values = list(filter_table.columns)
    cell_values = []
    for index in range(0, len(filter_table.columns)):
        cell_values.append(filter_table.iloc[:, index : index + 1])

    if not style:
        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(values=header_values), cells=dict(values=cell_values)
                )
            ]
        )
    else:
        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(
                        values=header_values, fill_color="paleturquoise", align="left"
                    ),
                    cells=dict(values=cell_values, fill_color="lavender", align="left"),
                )
            ]
        )

    st.plotly_chart(fig)
    st.markdown(
        """
Pros

- Can maximize
- Can transfer and display 10.000 rows and 5 columns in 10000 seconds.
- Can do advanced styling and layout.

Cons

- Cannot sort or filter
- The scrollbar is *thin* and can be difficult to select/ drag.

References:

- [Plotly Table Introduction](https://plot.ly/python/table/)
- [Plotly Table Reference](https://plot.ly/python/reference/#table)
"""
    )


def slick_grid(results):
    st.header("Slickgrid")
    st.markdown(
        """
The SlickGrid example does not work because I cannot inject javascript <script>...</script> tags.

References:

- [SlickGrid](https://slickgrid.net/)
- [SlickGrid examples](https://github.com/mleibman/SlickGrid/tree/gh-pages/examples)
"""
    )

    st.markdown(
        """
<link rel="stylesheet" href="https://mleibman.github.io/SlickGrid/slick.grid.css" type="text/css"/>
<link rel="stylesheet" href="https://mleibman.github.io/SlickGrid/css/smoothness/jquery-ui-1.8.16.custom.css" type="text/css"/>
<table width="100%">
  <tr>
    <td valign="top" width="50%">
      <div id="myGrid" style="width:600px;height:500px;"></div>
    </td>
    <td valign="top">
      <h2>Demonstrates:</h2>
      <ul>
        <li>basic grid with minimal configuration</li>
      </ul>
        <h2>View Source:</h2>
        <ul>
            <li><A href="https://github.com/mleibman/SlickGrid/blob/gh-pages/examples/example1-simple.html" target="_sourcewindow"> View the source for this example on Github</a></li>
        </ul>
    </td>
  </tr>
</table>
<script src="https://mleibman.github.io/SlickGrid/lib/jquery-1.7.min.js"></script>
<script src="https://mleibman.github.io/SlickGrid/lib/jquery.event.drag-2.2.js"></script>
<script src="https://mleibman.github.io/SlickGrid/slick.core.js"></script>
<script src="https://mleibman.github.io/SlickGrid/slick.grid.js"></script>
<script>
  var grid;
  var columns = [
    {id: "title", name: "Title", field: "title"},
    {id: "duration", name: "Duration", field: "duration"},
    {id: "%", name: "% Complete", field: "percentComplete"},
    {id: "start", name: "Start", field: "start"},
    {id: "finish", name: "Finish", field: "finish"},
    {id: "effort-driven", name: "Effort Driven", field: "effortDriven"}
  ];
  var options = {
    enableCellNavigation: true,
    enableColumnReorder: false
  };
  $(function () {
    var data = [];
    for (var i = 0; i < 500; i++) {
      data[i] = {
        title: "Task " + i,
        duration: "5 days",
        percentComplete: Math.round(Math.random() * 100),
        start: "01/01/2009",
        finish: "01/05/2009",
        effortDriven: (i % 5 == 0)
      };
    }
    grid = new Slick.Grid("#myGrid", data, columns, options);
  })
</script>
""",
        unsafe_allow_html=True,
    )


def select_number_of_rows_and_columns(results: pd.DataFrame, key: str):
    rows = st.selectbox(
        "Select number of table rows to display",
        options=[5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, len(results)],
        key=key,
    )
    columns = st.slider(
        "Select number of table columns to display",
        0,
        len(results.columns) - 1,
        DEFAULT_NUMBER_OF_COLUMNS,
        key=key,
    )
    style = st.checkbox("Style dataframe?", False, key=key)
    return rows, columns, style


@st.cache
def _filter_results(results, number_of_rows, number_of_columns) -> pd.DataFrame:
    return results.iloc[0:number_of_rows, 0:number_of_columns]


def filter_results(results, number_of_rows, number_of_columns, style) -> pd.DataFrame:
    filter_table = _filter_results(results, number_of_rows, number_of_columns)
    if style:
        filter_table = set_styles(filter_table)
    return filter_table


def set_styles(results):
    table_styles = [
        dict(
            selector="table",
            props=[("font-size", "150%"), ("text-align", "center"), ("color", "red")],
        ),
        dict(selector="caption", props=[("caption-side", "bottom")]),
    ]
    return (
        results.style.set_table_styles(table_styles)
        .set_properties(**{"background-color": "blue", "color": "white"})
        .set_caption("This is a caption")
    )


def _get_zip_file() -> zipfile.ZipFile:
    return zipfile.ZipFile(LOCAL_ROOT / ZIP_FILE_2019)


@st.cache
def read_results() -> pd.DataFrame:
    """The Stack Overflow Developer Survey Results

    Returns:
        pd.DataFrame -- A DataFrame containing the Stack Overflow Developer Survey Results
    """
    with _get_zip_file().open(RESULTS_2019) as file:
        return pd.read_csv(file)


@st.cache
def read_schema() -> pd.DataFrame:
    """The Stack Overflow Developer Survey Questions

    Returns:
        pd.DataFrame -- A DataFrame containing the Stack Overflow Developer Survey Questions
    """
    with _get_zip_file().open(SCHEMA_2019) as file:
        return pd.read_csv(file)


main()
