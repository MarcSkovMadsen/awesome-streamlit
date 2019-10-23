"""Page to show that its really easy to create a Spreadsheet like application"""
import pandas as pd
import streamlit as st


@st.cache
def get_biostats_data(url) -> pd.DataFrame:
    """A DataFrame of data from https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv

    Returns:
        pd.DataFrame -- [description]
    """
    data = pd.read_csv(url)
    columns = {
        "Name": "Name",
        '     "Sex"': "Sex",
        ' "Age"': "Age",
        ' "Height (in)"': "Height (in)",
        ' "Weight (lbs)"': "Weight (lbs)",
    }
    data = data.rename(columns=columns)
    return data


@st.cache
def transform_biostats_data(source_data: pd.DataFrame) -> pd.DataFrame:
    return source_data


@st.cache
def get_grades_data(url: str) -> pd.DataFrame:
    source_data = pd.read_csv(source_url)
    columns = {
        "Last name": "Last name",
        ' "First name"': "First name",
        ' "SSN"': "SSN",
        '        "Test1"': "Test1",
        ' "Test2"': "Test2",
        ' "Test3"': "Test3",
        ' "Test4"': "Test4",
        ' "Final"': "Final",
        ' "Grade"': "Grade",
    }
    source_data = source_data.rename(columns=columns)
    source_data["Test1"] = pd.to_numeric(source_data["Test1"], errors="coerce")
    source_data["First name"] = source_data["First name"].str.replace('"', "")
    return source_data


@st.cache
def transform_grades_data(source_data: pd.DataFrame) -> pd.DataFrame:
    # Add formulas
    transform_data = source_data.copy()
    transform_data["Test Mean"] = (
        transform_data[["Test1", "Test2", "Test3", "Test4"]].mean(axis=1).round()
    )
    transform_data["Relative diff from 1 to 4 (%)"] = (
        (transform_data["Test4"] - transform_data["Test1"])
        / transform_data["Test1"]
        * 100
    ).round()
    return transform_data


st.markdown(
    """
This app illustrates that it's so easy to create high quality spreadsheet like apps
 with [Streamlit](https://streamlit.io). You can **change the sheet** or **hide/show**
 the source data via the sidebar!"""
)

st.sidebar.title("Spreadsheet")
sheet = st.sidebar.selectbox("Select Sheet", ["Biostats", "Grades"])
show_source_data = st.sidebar.checkbox("Show Source Data", value=True)

st.write(f"""## {sheet}""")

if sheet == "Biostats":
    with st.spinner("Loading source data ..."):
        source_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv"
        source_data = get_biostats_data(source_url)
        transform_data = transform_biostats_data(source_data)
        measures = ["Age", "Height (in)", "Weight (lbs)"]

    # Show
    measure = st.selectbox("Measure", ["Age", "Height (in)", "Weight (lbs)"])
    with st.spinner("Updating plot ..."):
        selected = pd.DataFrame(transform_data[measure])
        st.bar_chart(selected)


elif sheet == "Grades":
    with st.spinner("Loading source data ..."):
        source_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/grades.csv"
        source_data = get_grades_data(source_url)
        transform_data = transform_grades_data(source_data)

    # Show
    st.write(  # pylint-disable=line-too-long
        "I illustrate a calculation by calculating the Test Mean."
        " After that we illustrate a calculation to show how much better the students did"
        " the 4th test compared to 1st one.",
        transform_data[
            [
                "First name",
                "Last name",
                "Test1",
                "Test2",
                "Test3",
                "Test4",
                "Test Mean",
                "Relative diff from 1 to 4 (%)",
            ]
        ],
    )
# Show Soure
if show_source_data:
    st.subheader("Source Data")
    st.markdown(f"[{source_url}]({source_url})")
    st.dataframe(source_data)
