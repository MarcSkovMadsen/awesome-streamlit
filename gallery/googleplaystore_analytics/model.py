import streamlit as st


def write():
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

    st.image("website/assets/DecisionTree.PNG")

    st.write("""

            2. Support vector machine
                - This is because we can penalize mistakes on the minority class by an amount proportional to how under-represented it is.
             """)

    st.image("website/assets/SVM.PNG", width=300)

    st.write("""

            To counter the imbalanced dataset, we also applied SMOTE (Synthetic Minority Over-sampling Technique).
            It is an over-sampling method which creates synthetic samples of the minority class.SMOTE uses a nearest neighbors algorithm to generate new and synthetic data we can use for training our model.

            """)
    # st.image("website/assets/sentiment_freq.jpeg")
    #st.write(""" Figure 3 : Sentiment Distribution""")
    st.write('**10-fold Cross Validation Table**')
    st.image("website/assets/Best_Model.PNG")
    ##st.write("Figure 4 : Cross Validation")
    st.write("""
             Using TF-IDF generally results in higher F1 score.
             """)

    st.write("""
            The measure of performance is micro-average F1-score as the dataset is unbalanced.

            The following is our best model on classification.

            **TF-IDF** + **Random Forest** + **OverSampling**

             """)
    st.image("website/assets/model.PNG")
    st.write("""
             ## Individual Star Rating Prediction Model
             After finalizing the classifier model for predicting the sentiment polarity, we designed a Neural Network with `Pytorch` as such.
             """)

    # TODO: insert image on general idea of the model
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
    st.image("website/assets/Predict_explaination.jpg", use_column_width=True)
    st.write(
        r"""
        We trained our model for 100, 300 and 1000 epochs using the following parameters: 
        
        InputSize $= 28$, OutputSize $= 1$, HiddenSize $= 30$ and learning rate $= 0.0002$.
        """
    )
    st.image("website/assets/ReLUgraph.png")
