"""This module contains the list of Authors"""
from awesome_streamlit.shared import models

Author = models.Author
# Authors
STREAMLIT_AUTHOR = Author(name="Streamlit", url="https://streamlit.io/")
KEVIN_ARVAI = Author(name="Kevin Arvai", url="https://github.com/arvkevi")
MARC_SKOV_MADSEN = Author(
    name="Marc Skov Madsen", url="https://datamodelsanalytics.com"
)
INES = Author(name="Ines Montani", url="https://gist.github.com/ines")
PARAS_PATIDAR = Author(name="Paras Patidar", url="https://github.com/patidarparas13")
AWESOME_STREAMLIT_ORG = Author(
    name="Awesome-Streamlit.org",
    url="https://github.com/marcskovmadsen/awesome-streamlit",
)
ALEXANDER_GARCIA = Author(name="Alexander Garcia", url="https://github.com/djauxel")
JCHARIS = Author(name="Jesse E. Agbe (JCharis)", url="https://github.com/Jcharis")
POSEY = Author(name="Luke Posey", url="https://github.com/Poseyy")
PADUEL = Author(name="Paduel", url="https://github.com/paduel")
AUTHORS = [
    ALEXANDER_GARCIA,
    INES,
    JCHARIS,
    KEVIN_ARVAI,
    MARC_SKOV_MADSEN,
    PARAS_PATIDAR,
    POSEY,
    STREAMLIT_AUTHOR,
]
