"""Fork of Sentiment-Analyzer-Tool by Paras Patidar

Source: https://github.com/patidarparas13/Sentiment-Analyzer-Tool
Credits: https://github.com/patidarparas13
"""

import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix
import numpy as np
import itertools
import matplotlib.pyplot as plt
import requests

st.title("Sentiment Analyzer Based On Text Analysis ")
st.subheader("Paras Patidar - MLAIT")
st.write("\n\n")


@st.cache
def get_all_data():
    root = "https://raw.githubusercontent.com/patidarparas13/Sentiment-Analyzer-Tool/master/Datasets/"
    data = requests.get(root + "imdb_labelled.txt").text.split("\n")
    data += requests.get(root + "amazon_cells_labelled.txt").text.split("\n")
    data += requests.get(root + "yelp_labelled.txt").text.split("\n")

    return data


with st.spinner("Data"):
    all_data = get_all_data()
if st.checkbox("Show Dataset"):
    st.write(all_data)


@st.cache
def preprocessing_data(data):
    processing_data = []
    for single_data in data:
        if len(single_data.split("\t")) == 2 and single_data.split("\t")[1] != "":
            processing_data.append(single_data.split("\t"))

    return processing_data


if st.checkbox("Show PreProcessed Dataset"):
    st.write(preprocessing_data(all_data))


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


training_data, evaluation_data = preprocessing_step()
vectorizer = CountVectorizer(binary="true")
classifier = training_step(training_data, vectorizer)


def analyse_text(classifier, vectorizer, text):
    return text, classifier.predict(vectorizer.transform([text]))


def print_result(result):
    text, analysis_result = result
    print_text = "Positive" if analysis_result[0] == "1" else "Negative"
    return text, print_text


review = st.text_input("Enter The Review", "Write Here...")
if st.button("Predict Sentiment"):
    result = print_result(analyse_text(classifier, vectorizer, review))
    st.success(result[1])
else:
    st.write("Press the above button..")
