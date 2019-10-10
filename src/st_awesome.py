"""Extensions of the streamlit api relevant for the awesome stremlit project"""
import streamlit as st


def title(body: str):
    """uses st.write to write the title as f'Awesome Streamlit {title} ' plus the awesome badge

    Arguments:
        body {str} -- [description]
    """
    st.write(
        f"# Awesome Streamlit {body} "
        "[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/"
        "d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)]"
        "(https://github.com/MarcSkovMadsen/awesome-streamlit)"
    )
