import streamlit as st
import pandas as pd

"""# Awesome Streamlit Spreadsheet [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesome-streamlit)"""

"""Illustration of how easy it is to create a spreadsheet like application with

- Sheets
- Tables
- Plots
- Formulas

using the power of Streamlit and Python"""
sheet = st.sidebar.selectbox("Select Sheet", ["Biostats", "Grades"])
show_source = st.sidebar.checkbox("Show Source")
show_code = st.sidebar.checkbox("Show Code")

st.write(f"## {sheet}")

if sheet == "Biostats":
    biostats_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv"

    biostats = pd.read_csv(biostats_url)

    columns = {
        "Name": "Name",
        '     "Sex"': "Sex",
        ' "Age"': "Age",
        ' "Height (in)"': "Height (in)",
        ' "Weight (lbs)"': "Weight (lbs)",
    }
    biostats = biostats.rename(columns=columns)

    # category = st.selectbox("Category", ["Name", "Sex"])
    measure = st.selectbox("Measure", ["Age", "Height (in)", "Weight (lbs)"])

    # biostats_selected = biostats.set_index(category)
    biostats_selected = pd.DataFrame(biostats[measure])
    # biostats_selected.set_index(biostats[category], inplace=True)
    st.bar_chart(biostats_selected)

    if show_source:
        f"""Source

        {biostats_url}"""
        biostats

elif sheet == "Grades":
    """We illustrate a calculation by calculating the Test Mean.
    After that we illustrate a calculation to show how much better the students did the 4th test compared to 1st one
    """

    grades_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/grades.csv"

    grades_source = pd.read_csv(grades_url)
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
    grades_source = grades_source.rename(columns=columns)
    grades_source["Test1"] = pd.to_numeric(grades_source["Test1"], errors="coerce")
    grades_source["First name"] = grades_source["First name"].str.replace('"', "")
    grades_mean = grades_source.copy()
    grades_mean["Test Mean"] = (
        grades_mean[["Test1", "Test2", "Test3", "Test4"]].mean(axis=1).round()
    )
    grades_mean["Relative diff from 1 to 4 (%)"] = (
        (grades_mean["Test4"] - grades_mean["Test1"]) / grades_mean["Test1"] * 100
    ).round()
    grades_mean[
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
    ]
    if show_source:
        f"""Source

        {grades_url}"""
        grades_source

if show_code:
    """## Code"""
    with st.echo():
        """This is just some dummy code"""
        a = 1
        b = 2
        result = a + b
        result
