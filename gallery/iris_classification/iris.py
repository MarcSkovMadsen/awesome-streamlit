"""
App: Iris Classifier

Author: Noah Saunders
Credits: Marc Skov Madsen (for refactoring)
Source Code: https://morioh.com/p/7066169a0314
Source Data: https://gist.github.com/netj/8836201
"""

import pathlib
import urllib.request
from typing import Tuple

import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

IRIS_CSV_FILE = "iris.csv"
GALLERY_FOLDER = "iris_classification"
LOCAL_ROOT = pathlib.Path(__file__).parent
GITHUB_ROOT = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/"
    "master/gallery/" + GALLERY_FOLDER + "/"
)


def main():
    st.title("Iris Classifier")
    st.header("Data Exploration")

    source_df = read_iris_csv()
    if st.checkbox("Show Source Data"):
        st.write(source_df)

    selected_species_df = select_species(source_df)

    show_scatter_plot(selected_species_df)

    show_histogram_plot(selected_species_df)

    show_machine_learning_model(source_df)


def show_machine_learning_model(source_df):
    st.header("Machine Learning models")
    features = source_df[
        ["sepal.length", "sepal.width", "petal.length", "petal.width"]
    ].values
    labels = source_df["variety"].values
    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, train_size=0.7, random_state=1
    )
    alg = ["Decision Tree", "Support Vector Machine"]
    classifier = st.selectbox("Which algorithm?", alg)

    if classifier == "Decision Tree":
        dtc = DecisionTreeClassifier()
        dtc.fit(X_train, y_train)
        acc = dtc.score(X_test, y_test)
        st.write("Accuracy: ", acc)
        pred_dtc = dtc.predict(X_test)
        cm_dtc = confusion_matrix(y_test, pred_dtc)
        st.write("Confusion matrix: ", cm_dtc)
    elif classifier == "Support Vector Machine":
        svm = SVC()
        svm.fit(X_train, y_train)
        acc = svm.score(X_test, y_test)
        st.write("Accuracy: ", acc)
        pred_svm = svm.predict(X_test)
        cm = confusion_matrix(y_test, pred_svm)
        st.write("Confusion matrix: ", cm)


def show_histogram_plot(selected_species_df):
    st.subheader("Histogram")
    feature = st.selectbox("Which feature?", selected_species_df.columns[0:4])
    fig2 = px.histogram(selected_species_df, x=feature, color="variety", marginal="rug")
    st.plotly_chart(fig2)


def select_species(source_df):
    selected_species = st.multiselect(
        "Select iris varieties for further exploration", source_df["variety"].unique()
    )
    selected_species_df = source_df[(source_df["variety"].isin(selected_species))]
    st.write(selected_species_df)
    return selected_species_df


def show_scatter_plot(selected_species_df: pd.DataFrame):
    st.subheader("Scatter plot")
    col1 = st.selectbox("Which feature on x?", selected_species_df.columns[0:4])
    col2 = st.selectbox("Which feature on y?", selected_species_df.columns[0:4])

    fig = px.scatter(selected_species_df, x=col1, y=col2, color="variety")
    st.plotly_chart(fig)


@st.cache
def read_iris_csv() -> pd.DataFrame:
    return pd.read_csv(LOCAL_ROOT / IRIS_CSV_FILE)
    # return pd.read_csv(GITHUB_ROOT + IRIS_CSV_FILE)


main()
