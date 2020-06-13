import streamlit as st

import src.pages.Dashboard as Dashboard
import src.pages.Home as Home
import src.sidebar.main_sidebar as msb
import src.utils.utils as utils

PAGES = {
	"Home": Home,
	"Dashboard": Dashboard
}

def main():
	"""Main function of the App"""
	st.sidebar.title("Navigation")
	selection = st.sidebar.radio("", list(PAGES.keys()))
	utils.write_page(msb)


	page = PAGES[selection]

	with st.spinner(f"Loading page ..."):
		utils.write_page(page)


if __name__ == "__main__":
	main()
