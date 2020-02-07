import itertools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from nltk.probability import FreqDist


@st.cache(persist=True)
def load_data():
    reviews_data = pd.read_csv("data/reviews_naive_polarity.csv")
    app_data = pd.read_csv("data/googleplaystore_cleaned.csv")
    return reviews_data, app_data

def preview(selection, reviews_df, app_df):
    if selection == view_modes[0]:
        preview_general(app_df)
    elif selection == view_modes[1]:
        preview_reviews(reviews_df)

def preview_general(df):
    st.write("## General App Data")
    st.write(df)
    fig = plt.figure(figsize=(10, 4))
    sns.countplot(df['Type'], orient="h")
    plt.title('Frequency of Free and Paid Apps')
    st.pyplot()

    st.write("""
             ### Observation of Trends
             """)
    fig = plt.figure(figsize=(10, 4))
    plt.title('Frequency Distribution of Categories')
    plt.xlabel('Category')
    plt.ylabel('Frequency')
    sns.countplot(df['Category'])
    plt.xticks(rotation=90)
    plt.tight_layout()
    st.pyplot()

    st.image("gallery/googleplaystore_analytics/assets/category_rating_violin.jpg", use_column_width=True)

    fig = plt.figure(figsize=(10, 4))
    value_counts = df["Genres"].value_counts()
    genre_labels = list(value_counts.index)

    # manually overriding so that they don't appear on the circle
    for i in range(10, len(genre_labels)):
        genre_labels[i] = " "

    def my_autopct(pct):
        return ('%.2f%%' % pct) if pct > 3.5 else ''

    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    fig1, ax1 = plt.subplots()
    ax1.pie(value_counts, colors=colors, labels=genre_labels,
            autopct=my_autopct, startangle=90)

    # wanted to add in an explode param, but streamlit did not allow this
    # https://medium.com/@kvnamipara/a-better-visualisation-of-pie-charts-by-matplotlib-935b7667d77f

    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    ax1.axis('equal')
    st.pyplot()

    fig = plt.figure(figsize=(10, 4))
    plt.xlabel('Rating')
    plt.ylabel('Frequency')
    sns.countplot(df['Rating'])
    plt.title('Frequency of Average Star Ratings')
    st.pyplot()


def preview_reviews(df):
    st.write(
        "## Reviews Data\n The preprocessing steps taken to produce the tokens can refered [here](https://github.com/lyqht/googleplaystore-analytics/blob/master/Notebooks/prelim_nlp_model.ipynb) ")
    st.write(df)

    st.image("gallery/googleplaystore_analytics/assets/1_word_count_reviews.jpg", use_column_width=True)
    st.write("Word Count Frequency")
    st.image("gallery/googleplaystore_analytics/assets/review_length_by_sentiment.jpg",
             use_column_width=True)
    st.image("gallery/googleplaystore_analytics/assets/freqDist.png", use_column_width=True)


def writeDataset():
    reviews_df, app_df = load_data()
    st.write(
        """
        ### Skimming Through The Dataset
        Toggle below to view the different datasets! (already been preprocessed by us) 
        """)
    selection = st.radio("Explore: ", view_modes)
    preview(selection, reviews_df, app_df)

def writeModel():
    st.title("Prediction of Individual Star Rating")
    st.write("""
             ## Feature Engineering: Sentiment Polarity

            Since we **do not have individual star ratings for each review**,
            we generated labels using VADER SentimentIntensityAnalyzer and used NaiveBayesClassifier to classify the reviews based on the sentiment polarity.
            [(link to previous presentation slides on this)](https://docs.google.com/presentation/d/e/2PACX-1vSopfa2P6Pq1XkO0fVyysrAUlShHuYO1YM0bXarXPL4majGsw1EUvd0gxvwepYRxl89yiJfglcmTmdH/pub?start=true&loop=false&delayms=3000)

            ## Classification Model
            After we labelled the reviews with their corresponding sentiment, we proceeded to build a classification model for classifying the reviews into their corresponding sentiment.
            For the input of the classifier, we explored two different feature extraction method for the reviews:

            1. TF-IDF
            2. Doc2Vec
                - For Doc2Vec, there are distributed bag of words (DBOW) and distributed memory (DM).
                - DBOW was selected.
            In DBOW, the paragraph vectors are obtained by training a neural network on the task of predicting a probability distribution of words in a paragraph given a randomly-sampled word from the paragraph.

            After which, we have also performed cross-validation of different models to classify the sentiment of each review.

            ### Cross Validation
            The following are the models that we used:

            1. Decision Tree
                - often perform well on imbalanced datasets due to their hierarchical structure
                - our dataset is biased to positive sentiment
            """)

    st.image("gallery/googleplaystore_analytics/assets/DecisionTree.PNG")

    st.write("""

            2. Support vector machine
                - This is because we can penalize mistakes on the minority class by an amount proportional to how under-represented it is.
             """)

    st.image("gallery/googleplaystore_analytics/assets/SVM.PNG", width=300)

    st.write("""

            To counter the imbalanced dataset, we also applied SMOTE (Synthetic Minority Over-sampling Technique).
            It is an over-sampling method which creates synthetic samples of the minority class.SMOTE uses a nearest neighbors algorithm to generate new and synthetic data we can use for training our model.

            """)
    st.write('**10-fold Cross Validation Table**')
    st.image("gallery/googleplaystore_analytics/assets/Best_Model.PNG")
    st.write("""
             Using TF-IDF generally results in higher F1 score.
             """)

    st.write("""
            The measure of performance is micro-average F1-score as the dataset is unbalanced.

            The following is our best model on classification.

            **TF-IDF** + **Random Forest** + **OverSampling**

             """)
    st.image("gallery/googleplaystore_analytics/assets/model.PNG")
    st.write("""
             ## Individual Star Rating Prediction Model
             After finalizing the classifier model for predicting the sentiment polarity, we designed a Neural Network with `Pytorch` as such.
             """)

    st.write(
        """
        Across the apps, there is a differing number of reviews, and the 15th percentile is 28.
        Thus for train-ing and testing our model, we only selected apps that minimally have 28 reviews.
        """
    )
    st.write(
        """
        Hence, we chose to randomly pick 28 reviews from each of these apps and use their sentiment values as the input for the model $x_i$,
        and the average rating for the corresponding apps as the labels $y_i$.
        """
    )
    st.image("gallery/googleplaystore_analytics/assets/Predict_explaination.jpg", use_column_width=True)
    st.write(
        r"""
        We trained our model for 100, 300 and 1000 epochs using the following parameters: 
        
        InputSize $= 28$, OutputSize $= 1$, HiddenSize $= 30$ and learning rate $= 0.0002$.
        """
    )
    st.image("gallery/googleplaystore_analytics/assets/ReLUgraph.png")
    


def writeTopicModelling():
    st.write("""# Topic Modelling""")
    st.write("""
             Download the file [here](gallery/googleplaystore_analytics/assets/overall_100_topics_enhanced.html) for pyLDAvis visualization.
             Topic modelling is based on the Latent Dirichlet Allocation Algorithm.
             """)

    st.write("#### Latent Dirichlet Algorithm (LDA)")
    st.image("gallery/googleplaystore_analytics/assets/LDA-concept.png", use_column_width=True)
    st.write(r"""
        To begin, LDA is based on the Dirichlet Distribution, normally known as $Dir(\alpha)$.
        Dirichlet distributions are commonly used as prior distributions in Bayesian statistics,
        and in fact the Dirichlet distribution is the conjugate prior of the categorical distribution and multinomial distribution.
        A great article about this distribution can be found [here](https://towardsdatascience.com/dirichlet-distribution-a82ab942a879).
        """)
    st.image("gallery/googleplaystore_analytics/assets/Dirichlet.png", use_column_width=True)
    st.write(r"""
    Given:
    - A document is a sequence of $N$ words denoted by $\textbf{w} = (w_1,w_2,... ,w_N)$, where $w_n$ is the nth word b in the sequence.
    - A corpus is a collection of $M$ documents denoted by $D = \textbf{w}_1, \textbf{w}_2,...\textbf{w}_m$
    - $\alpha$ is the Dirichlet prior on the per-document topic distributions
    - $\beta$ is the Dirichlet prior on the per-topic  word distributions
    - $\Theta$ is the topic distribution for document $m$
    - $z_{mn}$ is the topic for $n^{\text{th}}$  word in document $m$
    """)
    st.image("gallery/googleplaystore_analytics/assets/LDA-concept2.png", use_column_width=True)


view_modes = ["General App Data", "Reviews Data"]

st.write("For the presentation slide version of this project, view it [here](https://playstore-analytics.herokuapp.com/).")
writeDataset()
writeTopicModelling()
writeModel()
