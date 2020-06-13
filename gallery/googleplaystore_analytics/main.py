import streamlit as st

import dataset
import intro
import model
import references
import topic_modelling

PAGES = {
    "Intro": intro,
    "Dataset Exploration": dataset,
    "Topic Modelling": topic_modelling,
    "Star Rating Prediction Model": model,
    "References": references,
}


def main():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]

    with st.spinner(f"Loading Page ..."):
        page.write()  # each page has a write function


if __name__ == "__main__":
    main()
