"""
App: Iris Classifier

Author: Noah Saunders
Credits: Marc Skov Madsen (for refactoring)
Source Code/ Article: https://morioh.com/p/7066169a0314
Source Data: https://gist.github.com/netj/8836201
"""

import pathlib

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
    """## Main function of Iris Classifier App

    Run this to run the app.
    """
    st.title("Iris Classifier")
    st.header("Data Exploration")

    source_df = read_iris_csv()
    st.subheader("Source Data")
    if st.checkbox("Show Source Data"):
        st.write(source_df)

    selected_species_df = select_species(source_df)
    if not selected_species_df.empty:
        show_scatter_plot(selected_species_df)
        show_histogram_plot(selected_species_df)
    else:
        st.info("Please select one of more varieties above for further exploration.")

    show_machine_learning_model(source_df)


def select_species(source_df: pd.DataFrame) -> pd.DataFrame:
    """## Component for selecting one of more species for exploration

    Arguments:
        source_df {pd.DataFrame} -- The source iris dataframe

    Returns:
        pd.DataFrame -- A sub dataframe having data for the selected species
    """
    selected_species = st.multiselect(
        "Select iris varieties for further exploration below",
        source_df["variety"].unique(),
    )
    selected_species_df = source_df[(source_df["variety"].isin(selected_species))]
    if selected_species:
        st.write(selected_species_df)
    return selected_species_df


def show_scatter_plot(selected_species_df: pd.DataFrame):
    """## Component to show a scatter plot of two features for the selected species

    Arguments:
        selected_species_df {pd.DataFrame} -- A DataFrame with the same columns as the
            source_df iris dataframe
    """
    st.subheader("Scatter plot")
    feature_x = st.selectbox("Which feature on x?", selected_species_df.columns[0:4])
    feature_y = st.selectbox("Which feature on y?", selected_species_df.columns[0:4])

    fig = px.scatter(selected_species_df, x=feature_x, y=feature_y, color="variety")
    st.plotly_chart(fig)


def show_histogram_plot(selected_species_df: pd.DataFrame):
    """## Component to show a histogram of the selected species and a selected feature

    Arguments:
        selected_species_df {pd.DataFrame} -- A DataFrame with the same columns as the
            source_df iris dataframe
    """
    st.subheader("Histogram")
    feature = st.selectbox("Which feature?", selected_species_df.columns[0:4])
    fig2 = px.histogram(selected_species_df, x=feature, color="variety", marginal="rug")
    st.plotly_chart(fig2)


def show_machine_learning_model(source_df: pd.DataFrame):
    """Component to show the performance of an ML Algo trained on the iris data set

    Arguments:
        source_df {pd.DataFrame} -- The source iris data set

    Raises:
        NotImplementedError: Raised if a not supported model is selected
    """
    st.header("Machine Learning models")
    features = source_df[
        ["sepal.length", "sepal.width", "petal.length", "petal.width"]
    ].values
    labels = source_df["variety"].values
    x_train, x_test, y_train, y_test = train_test_split(
        features, labels, train_size=0.7, random_state=1
    )
    alg = ["Decision Tree", "Support Vector Machine"]
    classifier = st.selectbox("Which algorithm?", alg)

    if classifier == "Decision Tree":
        model = DecisionTreeClassifier()
    elif classifier == "Support Vector Machine":
        model = SVC()
    else:
        raise NotImplementedError()

    model.fit(x_train, y_train)
    acc = model.score(x_test, y_test)
    st.write("Accuracy: ", acc.round(2))
    pred_model = model.predict(x_test)
    cm_model = confusion_matrix(y_test, pred_model)
    st.write("Confusion matrix: ", cm_model)


@st.cache
def read_iris_csv() -> pd.DataFrame:
    """## Iris DataFrame

    Returns:
        pd.DataFrame -- A dataframe with the source iris data
    """
    # return pd.read_csv(LOCAL_ROOT / IRIS_CSV_FILE)
    return pd.read_csv(GITHUB_ROOT + IRIS_CSV_FILE)


main()
