"""Medical Language Model Learner (MLML)

Author: Georgi Tancev. https://github.com/gtancev
Source: https://github.com/gtancev/MLML/blob/master/nlp_app.py
Article: https://towardsdatascience.com/mining-and-classifying-medical-text-documents-1876462f73bc
Data: https://www.kaggle.com/tboyle10/medicaltranscriptions/
Credits: Marc Skov Madsen (for refactoring)
"""
# Todo:
# 1. Do something about charts. They don't have the right size and the text characters do not
# look well.
# 2. Refactor into smaller functions. Some with @st.cache to speed up the application.

from __future__ import division, unicode_literals

import itertools
import pathlib

import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from matplotlib import rc
from sklearn.decomposition import NMF, LatentDirichletAllocation, TruncatedSVD
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
from streamlit.logger import get_logger

MT_SAMPLES_PATH = pathlib.Path(__file__).parent / "medical_language_learner/mtsamples.csv"

MT_SAMPLES_URL = (
    "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/gallery/"
    "medical_language_learner/mtsamples.csv"
)

enc = LabelEncoder()

plt.rcParams['lines.linewidth'] = 1.0
plt.rcParams['font.size'] = 6.0

LOGGER = get_logger(__name__)

def main():
    st.title("Medical Language Model Learner")
    st.sidebar.markdown("""
Author: [Georgi Tancev](https://github.com/gtancev)

[Original Code](https://github.com/gtancev/MLML/blob/master/nlp_app.py),
[Article](https://towardsdatascience.com/mining-and-classifying-medical-text-documents-1876462f73bc),
[Data](https://www.kaggle.com/tboyle10/medicaltranscriptions/)
""")
    st.sidebar.header("Sample Selection.")
    filename = st.sidebar.selectbox("Choose a file.",("None", "mtsamples"))

    st.header("Introduction")
    st.markdown("""
This application guides you through the development of **a language model
that classifies clinical documents** according to their medical speciality.

It is based on a **term frequency-inverse document frequency (tf-idf)** approach. Tf-idf is a
numerical statistic that is intended to reflect how important a word is to a document
in a collection or corpus. It is often used as a weighting factor in searches of information
retrieval, text mining, and user modeling.

The tf-idf value increases proportionally to the number of times a word appears in the document
and is offset by the number of documents in the corpus that contain the word, which helps to
adjust for the fact that some words appear more frequently in general.

Tf-idf is one of the most popular term-weighting schemes today; 83% of text-based recommender
systems in digital libraries use tf-idf.

**Note that tf-idf ignores the sequential aspect of a language**.

The actual model itself is based on a **random forest** classifier.

Random forests are an ensemble learning method for classification, regression and other tasks
that operates by constructing a multitude of decision trees at training time and outputting the
class that is the mode of the classes (classification) or mean prediction (regression) of the
individual trees. In particular, trees that are grown very deep tend to learn highly irregular
patterns: they overfit their training sets, i.e. have low bias, but very high variance.

Random forests are a way of averaging multiple deep decision trees, trained on different parts
of the same training set, with the goal of reducing the variance.

Random forests can be used to rank the importance of variables in a regression or classification
problem in a natural way.

The model is developed with scikit-learn. **Some possible degrees of freedom are shown in the
sidebar**. By adjusting them, the model is retrained and its performance re-evaluated.

**Start by choosing a file in the sidebar**.
""")

    if filename != "mtsamples":
        return

    try:
        data = get_mt_samples()
    except:
        st.error("The MT Samples could not be loaded!")
        return

    # DEFINE DATA.
    st.header("Preprocessing")
    st.write("First, data has to be preprocessed by adjusting the number of classes and transforming the data into tf-idf representation.",
    "As you can imagine, not every class might be represented enough in a data set to be able to classify it properly.",
    "It is advisable to remove classes which are underrepresented or whose abundance is below some treshhold to achieve a better performance.",
    "Alternatively, try to collect more data.")
    st.write("In addition, there are several degrees of freedom for the construction of tf-idf the dictionary. Adjusting them changes the amount and kind of words (**features**) which are included in the model.")
    st.subheader("Load data.")
    st.write("Display sample data by ticking the checkbox in the sidebar.")
    #filename = st.sidebar.text_input('Enter the filename of a csv-file.')

    agree = st.sidebar.checkbox('Display raw data.')
    if agree:
        st.dataframe(data)
    samples = data.transcription
    text_labels  = [label_name.lower() for label_name in data.medical_specialty]
    labels = enc.fit_transform(np.array(text_labels))
    labels = np.ravel(labels)
    unique_values, counts = np.unique(labels, return_counts=True)
    relative_counts = counts/np.sum(counts)
    st.write("The initial data set contains",np.shape(unique_values)[0],"classes and",data.shape[0],"samples.")

    # EXTRACT SAMPLES AND LABELS.
    st.sidebar.header("Preprocessing class distributions.")
    treshhold_to_consider = st.sidebar.slider("Minimum fraction of class in data set in order to be considered.", min_value=0.01, max_value=0.1, value=0.02, step=0.01)
    classes_to_consider = unique_values[relative_counts>=treshhold_to_consider]

    index_to_consider = np.empty((labels.shape[0]),dtype="bool")
    for i,label in enumerate(labels):
        if label in classes_to_consider:
            index_to_consider[i] = True
        else:
            index_to_consider[i] = False

    # EXTRACT CLASSES
    labels = labels[index_to_consider]
    samples = samples[index_to_consider]
    unique_values, counts = np.unique(labels, return_counts=True)
    relative_counts = counts/np.sum(counts)
    label_names = enc.inverse_transform(unique_values)

    # INSTRUCTION
    st.info("Some classes might be **underrepresented** in the data set and should be dropped. Choose a treshhold for minimum abundance in the original data set.")
    st.write("The final number of classes is",np.size(unique_values)," and the residual number of samples is",np.sum(index_to_consider),".")
    rel_counts = pd.DataFrame(data=relative_counts,columns=["fraction of class in data set"]).set_index(label_names)
    st.table(rel_counts)

    # DATA TRANSFORMATION
    st.subheader("Transform data.")
    st.sidebar.header("Constructing dictonary of words.")
    if st.sidebar.checkbox("Use word counts instead."):
        st.write("Transform the text data into **word count** representation.")
        max_df = st.sidebar.slider("Maximum fraction for a word to be considered.", min_value=0.05, max_value=0.4, value=0.3, step=0.01)
        min_df = st.sidebar.slider("Minimum fraction for a word to be considered.", min_value=0.001, max_value=0.05, value=0.01, step=0.001)
        max_features = st.sidebar.slider("Size of vocabulary.", min_value=100, max_value=2000, value=1000, step=100)
        ngram_range = (1,1)
        tfidf_vectorizer = CountVectorizer(max_df=max_df, min_df=min_df,max_features=max_features,stop_words='english',ngram_range=ngram_range)
    else:
        st.write("Transform the text data into **tf-idf representation**. Customize the dictionary in the sidebar. Alternatively, you can also work with pure word counts.")
        max_df = st.sidebar.slider("Maximum tf-idf for a word to be considered.", min_value=0.05, max_value=0.4, value=0.3, step=0.01)
        min_df = st.sidebar.slider("Minimum tf-idf for a word to be considered.", min_value=0.001, max_value=0.05, value=0.01, step=0.001)
        max_features = st.sidebar.slider("Size of vocabulary.", min_value=100, max_value=2000, value=1000, step=100)
        ngram_range = (1,1)
        tfidf_vectorizer = TfidfVectorizer(max_df=max_df, min_df=min_df,max_features=max_features,stop_words='english',ngram_range=ngram_range)

    #dimred =  NMF(n_components=2, random_state=1,beta_loss='kullback-leibler', solver='mu', max_iter=1000, alpha=.4,l1_ratio=.5)
    #dimred = LatentDirichletAllocation(n_components=2, max_iter=5,learning_method='online',learning_offset=50,random_state=1)
    dimred = TruncatedSVD(n_components=2)

    #@st.cache(show_spinner=False)
    def transform():
        tfidf = tfidf_vectorizer.fit_transform(samples)
        feature_names = tfidf_vectorizer.get_feature_names()
        return tfidf,feature_names

    # TF-IDF
    with st.spinner('Data is being transformed.'):
        tfidf,feature_names = transform()
        st.success("Transformation finished.")
        st.subheader("Visualize data.")
        st.write("Examine the distribution of classes by dimensionality reduction based on **singular value decomposition (SVD)**.")
        data_ = dimred.fit_transform(tfidf)
        data__ = pd.DataFrame(data=data_,columns=["principal component 1","principal component 2"])
        labels_ = pd.DataFrame(data=enc.inverse_transform(labels),columns=["class"])
        data___ = pd.concat((data__,labels_),axis=1)
        c = alt.Chart(data___,title="dimensionality reduction",height=600).mark_circle(size=20).encode(x='principal component 1', y='principal component 2',color=alt.Color('class', scale=alt.Scale(scheme='blues')),tooltip=["class"]).interactive()
        st.altair_chart(c)
        st.write("The explained variance is",np.round(np.sum(dimred.explained_variance_ratio_)*100,2),"%.")

    # MODEL BUILDING.
    st.header("Model Building")
    st.write("The model is based on a **random forest**. Customize the model in the sidebar.")
    st.sidebar.header("Customizing the model.")
    n_estimators = st.sidebar.text_input('Number of trees in random forest.', '1000')
    max_leaf_nodes = st.sidebar.text_input('Maximum number of lead nodes.', '25')
    max_depth = st.sidebar.text_input('Maximum depth.', '5')
    class_weight = st.sidebar.selectbox("Class weights for the model.",('balanced','balanced_subsample'))
    forest_clf = RandomForestClassifier(n_estimators=int(n_estimators),max_depth=int(max_depth),max_leaf_nodes=int(max_leaf_nodes),class_weight=class_weight,oob_score=True,n_jobs=-1,random_state=0) # Define classifier to optimize.
    #parameters = {'max_leaf_nodes':np.linspace(20,35,14,dtype='int')} # Define grid.
    #clf = RandomizedSearchCV(forest_clf, parameters, n_iter=10, cv=3,iid=False, scoring='accuracy',n_jobs=-1) # Balanced accuracy as performance measure.

    #@st.cache(show_spinner=False)
    def train():
        classifier = forest_clf.fit(tfidf, labels) # Train/optimize classifier.
        #forest = classifier.best_estimator_
        feature_importances = classifier.feature_importances_
        indices = np.argsort(feature_importances)[::-1]

        # Analyze Feature Importance.
        n_f = 30 # Amount of Desired Features.
        sorted_feature_names = []
        for f in range(n_f):
            sorted_feature_names.append(feature_names[indices[f]])
        #feature_importance = pd.DataFrame(data=feature_importances[indices[0:n_f]], index=sorted_feature_names,columns=["feature importance"])
        feature_importance = pd.DataFrame(data=np.transpose(np.array((np.round(feature_importances[indices[0:n_f]],5),sorted_feature_names))),columns=["feature importance","features"])
        return classifier,feature_importance

    with st.spinner('Model is being trained.'):
        classifier,feature_importance = train() # Train/optimize classifier.
        st.success("Training finished.")
        st.write("Examine the importance of the most meaningful words for the overall classification performance.")
        bars = alt.Chart(feature_importance,height=600, title="discriminative power of features").mark_bar(color='steelblue',opacity=0.7).encode(
        y='features:N',
        x='feature importance:Q',tooltip="feature importance")
        st.altair_chart(bars)
        st.write('The test set accuracy (from out-of-bag samples) is',np.round(classifier.oob_score_,2),".")

    # MODEL EVALUATION
    st.header("Model Evaluation")
    y_true = labels
    y_pred = classifier.predict(tfidf)
    f1_score_ = f1_score(y_true,y_pred,average="weighted")
    st.write("The F1-score is",np.round(f1_score_,2),".")
    st.write("Below, the confusion matrix for the classification problem is provided.")
    cm = confusion_matrix(y_true,y_pred)
    labels_repeated = []
    for _ in range(np.unique(labels_).shape[0]):
        labels_repeated.append(np.unique(labels_))
    source = pd.DataFrame({'predicted class': np.transpose(np.array(labels_repeated)).ravel(),
                        'true class': np.array(labels_repeated).ravel(),
                        'count': np.round(cm.ravel(),2)})
    heat = alt.Chart(source,height=1000, title="confusion matrix").mark_rect(opacity=0.7).encode(
    x='predicted class:N',
    y='true class:N',
    color=alt.Color('count:Q', scale=alt.Scale(scheme='blues')),
    tooltip="count")
    st.altair_chart(heat)


@st.cache
def get_mt_samples() -> pd.DataFrame:
    """A dataframe of mt samples

    Returns:
        pd.DataFrame -- A dataframe
    """
    if MT_SAMPLES_PATH.exists():
        location = MT_SAMPLES_PATH
    else:
        location = MT_SAMPLES_URL
    return pd.read_csv(location, index_col=0,usecols=[0,1,2,4]).dropna()


main()
