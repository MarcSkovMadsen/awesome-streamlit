"""Fork of Sentiment-Analyzer-Tool by Paras Patidar. Improvements by Marc Skov Madsen

Original Source: https://github.com/patidarparas13/Sentiment-Analyzer-Tool
Original Author: https://github.com/patidarparas13,
"""

import itertools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import BernoulliNB

ROOT_URL = "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/gallery/sentiment_analyzer/data/"
FILES = ["imdb_labelled.txt", "amazon_cells_labelled.txt", "yelp_labelled.txt"]


@st.cache
def get_all_data():
    """Loads the source data"""
    data = []
    for file in FILES:
        data += requests.get(ROOT_URL + file).text.split("\n")

    return data


@st.cache
def preprocessing_data(data):
    processing_data = []
    for single_data in data:
        if len(single_data.split("\t")) == 2 and single_data.split("\t")[1] != "":
            processing_data.append(single_data.split("\t"))
    return processing_data


@st.cache
def split_data(data):
    total = len(data)
    training_ratio = 0.75
    training_data = []
    evaluation_data = []

    for indice in range(0, total):
        if indice < total * training_ratio:
            training_data.append(data[indice])
        else:
            evaluation_data.append(data[indice])

    return training_data, evaluation_data


@st.cache
def preprocessing_step():
    data = get_all_data()
    processing_data = preprocessing_data(data)
    return split_data(processing_data)


def training_step(data, vectorizer):
    training_text = [data[0] for data in data]
    training_result = [data[1] for data in data]
    training_text = vectorizer.fit_transform(training_text)

    return BernoulliNB().fit(training_text, training_result)


def analyse_text(classifier, vectorizer, text):
    return text, classifier.predict(vectorizer.transform([text]))


def print_result(result):
    text, analysis_result = result
    print_text = "Positive" if analysis_result[0] == "1" else "Negative"
    return text, print_text


st.title("Sentiment Algorithm")
st.info(
    "This is an **improved version** of the "
    "awesome [**original**](https://github.com/patidarparas13/Sentiment-Analyzer-Tool) "
    "developed by awesome [**Paras Patidar**](https://github.com/patidarparas13). Kudos!\n\n"
)
st.write(
    "The algorithm is trained on a collection of movie reviews and you can test it below."
)
st.subheader("Extract the data")
file_markdown = "Source: \n"
file_markdown += ", ".join([f"[{file}]({ROOT_URL+file})" for file in FILES])
st.markdown(file_markdown)

with st.spinner("Extracting source data..."):
    all_data = get_all_data()

    source_data = pd.DataFrame(
        preprocessing_data(all_data), columns=["review", "sentiment"]
    )
    source_data["sentiment"] = source_data["sentiment"].map(
        {"0": "Negative", "1": "Positive"}
    )
    st.info(f"{len(source_data)} rows where extract with **succes**!")

top = st.selectbox(
    "Select number of rows to show", [5, 10, 25, 50, 100, len(source_data)]
)
st.table(source_data.head(top))

st.subheader("Train the algorithm")
with st.spinner("Training algorithm..."):
    training_data, evaluation_data = preprocessing_step()
    vectorizer = CountVectorizer(binary="true")
    classifier = training_step(training_data, vectorizer)
    st.info("The algorithm was trained with **success**!")


st.title("Try the algorithm here!")
write_here = "Write Here..."
review = st.text_input("Enter a review for classification by the algorithm", write_here)
if st.button("Predict Sentiment"):
    result = print_result(analyse_text(classifier, vectorizer, review))
    if review != write_here:
        st.success(result[1])
        st.error("For illustrative purposes only! :-)")
    else:
        st.error("You need to input a review for classification!")
else:
    st.info(
        "**Enter a review** above and **press the button** to predict the sentiment."
    )
