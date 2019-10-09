import pandas as pd
import streamlit as st


def write():
    st.write("TEST ABCD")
    # Create Sidebar
    sheet = st.sidebar.selectbox("Select Sheet", ["Biostats", "Grades"])
    show_code = st.sidebar.checkbox("Show Code")
    show_source = st.sidebar.checkbox("Show Source")

    # Create Header
    st.write(f"""## Spreadsheet""")
    st.write(
        """
        Illustration of how easy it is to create a spreadsheet like application with

        - Sheets
        - Tables
        - Plots
        - Formulas

        using the power of Streamlit and Python
        """
    )
    st.write("**You can change the Sheet shown in the sidebar on the left**")
    st.write(f"""## {sheet}""")

    if sheet == "Biostats":
        # Extract Source
        biostats_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/biostats.csv"
        biostats = pd.read_csv(biostats_url)

        # Wash Data
        columns = {
            "Name": "Name",
            '     "Sex"': "Sex",
            ' "Age"': "Age",
            ' "Height (in)"': "Height (in)",
            ' "Weight (lbs)"': "Weight (lbs)",
        }
        biostats = biostats.rename(columns=columns)

        # Show
        measure = st.selectbox("Measure", ["Age", "Height (in)", "Weight (lbs)"])
        biostats_selected = pd.DataFrame(biostats[measure])
        st.bar_chart(biostats_selected)

        # Show Source
        if show_source:
            st.write(
                f"""Source

            {biostats_url}""",
                biostats,
            )

    elif sheet == "Grades":
        # Extract Source
        grades_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/grades.csv"
        grades_source = pd.read_csv(grades_url)

        # Wash Data
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

        # Add formulas
        grades_mean = grades_source.copy()
        grades_mean["Test Mean"] = (
            grades_mean[["Test1", "Test2", "Test3", "Test4"]].mean(axis=1).round()
        )
        grades_mean["Relative diff from 1 to 4 (%)"] = (
            (grades_mean["Test4"] - grades_mean["Test1"]) / grades_mean["Test1"] * 100
        ).round()

        # Show
        st.write(
            """I illustrate a calculation by calculating the Test Mean.
        After that we illustrate a calculation to show how much better the students did the 4th test compared to 1st one
        """,
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
            ],
        )
        # Show Soure
        if show_source:
            st.write(
                f"""Source

            {grades_url}""",
                grades_source,
            )

    if show_code:
        st.write(
            """
This is just some dummy code

```python
a = 1
b = 2
result = a + b
print(result)
```
"""
        )
