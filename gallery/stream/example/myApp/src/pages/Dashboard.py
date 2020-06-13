import streamlit as st

PAGE_NAME = "Dashboard"

def write():
	with st.spinner(f"Loading {PAGE_NAME}..."):
		st.write(f"This is {PAGE_NAME}")

		elt_0 = st.empty()
