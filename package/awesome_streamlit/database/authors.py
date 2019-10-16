"""This module contains the list of Authors"""
from awesome_streamlit.database import models

Author = models.Author
# Authors
STREAMLIT_AUTHOR = Author(name="Streamlit", url="https://streamlit.io/")
STREAMLIT_EXAMPLE_AUTHOR = Author(
    name="Streamlit/.../examples/", url="https://streamlit.io/"
)
STREAMLIT_COMPONENT_AUTHOR = Author(
    name="Streamlit/.../api-examples-source", url="https://streamlit.io/"
)
MARC_SKOV_MADSEN = Author(
    name="Marc Skov Madsen", url="https://datamodelsanalytics.com"
)
INES = Author(name="Ines Montani", url="https://gist.github.com/ines")
PARAS_PATIDAR = Author(name="Paras Patidar", url="https://github.com/patidarparas13")

AUTHORS = [
    STREAMLIT_AUTHOR,
    STREAMLIT_EXAMPLE_AUTHOR,
    STREAMLIT_COMPONENT_AUTHOR,
    MARC_SKOV_MADSEN,
    INES,
    PARAS_PATIDAR,
]
