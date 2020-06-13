import pandas as pd
import streamlit as st


def write():

    st.write("""
           Initially, we trained a BERT-base-uncased Named Entity Recognition (NER) model on a Kaggle dataset [Annotated Corpus for Named Entity Recognition](https://www.kaggle.com/abhinavwalia95/entity-annotated-corpus)
            """)
    st.image("website/assets/ner_dataset.png", use_column_width=True)
    st.write(
        "And this are our results from training and testing")
    st.image("website/assets/bert_training_results.png", use_column_width=True)
    st.write(
        "However, it did not manage to perform well on the reviews from the Google Playstore Dataset... So the alternative is to do some topic modelling to derive more useful features instead.")

    st.write("""# Topic Modelling""")
    st.write("""
             Refer [here](website/assets/overall_100_topics_enhanced.html) for pyLDAvis visualization.
             Topic modelling is based on the Latent Dirichlet Allocation Algorithm.
             """)

    st.write("#### Latent Dirichlet Algorithm (LDA)")
    st.image("website/assets/LDA-concept.png", use_column_width=True)
    st.write(r"""
        To begin, LDA is based on the Dirichlet Distribution, normally known as $Dir(\alpha)$.
        Dirichlet distributions are commonly used as prior distributions in Bayesian statistics,
        and in fact the Dirichlet distribution is the conjugate prior of the categorical distribution and multinomial distribution.
        A great article about this distribution can be found [here](https://towardsdatascience.com/dirichlet-distribution-a82ab942a879).
        """)
    st.image("website/assets/Dirichlet.png", use_column_width=True)
    st.write(r"""
    Given:
    - A document is a sequence of $N$ words denoted by $\textbf{w} = (w_1,w_2,... ,w_N)$, where $w_n$ is the nth word b in the sequence.
    - A corpus is a collection of $M$ documents denoted by $D = \textbf{w}_1, \textbf{w}_2,...\textbf{w}_m$
    - $\alpha$ is the Dirichlet prior on the per-document topic distributions
    - $\beta$ is the Dirichlet prior on the per-topic  word distributions
    - $\Theta$ is the topic distribution for document $m$
    - $z_{mn}$ is the topic for $n^{\text{th}}$  word in document $m$
    """)
    st.image("website/assets/LDA-concept2.png", use_column_width=True)
