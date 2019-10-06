import streamlit as st
import pandas as pd

"""# Streamlit Spreadsheet"""

sheet = st.sidebar.selectbox("Select Sheet", ["Biostats", "Other"])

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

    f"""Source

    {biostats_url}"""
    biostats

elif sheet == "Other":
    pass
