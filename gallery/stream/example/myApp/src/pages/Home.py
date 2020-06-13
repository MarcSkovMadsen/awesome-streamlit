import streamlit as st

PAGE_NAME = "Home"

def write():
	with st.spinner(f"Loading {PAGE_NAME}..."):
		st.write(f"This is {PAGE_NAME}")

		elt_0 = st.empty()
