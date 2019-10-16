# We test that the api can be imported as expected
import awesome_streamlit as ast

# from awesome_streamlit import database
# import awesome_streamlit.database
# from awesome_streamlit.database import models
# from awesome_streamlit.database import authors
# from awesome_streamlit.database import tags
# from awesome_streamlit.database import resources
# from awesome_streamlit.app.pages import gallery
# from awesome_streamlit import app


# from awesome_streamlit.database.models import Tag
# from awesome_streamlit.database.models import Author
# from awesome_streamlit.database.models import Resource
# from awesome_streamlit.database.tags import TAGS
# from awesome_streamlit.database.authors import AUTHORS
# from awesome_streamlit.database.resources import RESOURCES
# from awesome_streamlit.database.authors import AUTHORS


def test_write_hello_world():
    """We test that the function exists and can run without error"""
    ast.experiments.write_hello_world()


# def write():
#     """Test that the main applications can run"""
#     ast.app.write()
#     ast.app.pages.gallery.write()
#     ast.app.pages.gallery.spreadsheet.write()
#     ast.testing.write()
#     ast.experiments.hello_world()
