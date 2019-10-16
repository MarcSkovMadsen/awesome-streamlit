"""This module provides a reference test example for
https://github.com/MarcSkovMadsen/awesome-streamlit/issues/2"""
import streamlit as st

import bf4.b4 as b4_new_name  # Hot reload works in b4.py file
import bf.b  # Hot reloading works in b.py file
import st_extensions  # Hot reloading works in st_extensions.py file
from bf2 import b2  # Hot reload does not work in b2.py file
from bf3 import b3 as b3_new_name  # Hot reload does not work in b3.py file

# c hot reloading does not work in bf/cf/c.py file through file bf/b.py
# d hot reloading does not work in bf/cf/df/d.py file through file bf/cf/c.py

st.write("this is a")

bf.b.write()
b2.write()
b3_new_name.write()
b4_new_name.write()
st_extensions.write("awesome")
