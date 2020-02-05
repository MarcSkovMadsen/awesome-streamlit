import streamlit as st
import src.utils.utils as utils


import src.sidebar.main_sidebar as msb
import src.pages.Home as Home
import src.pages.Dashboard as Dashboard

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

