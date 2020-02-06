import streamlit as st

# not used as originally intended to be render on the page itself, but not able to do so.
# with open("website/assets/overall_100_topics_enhanced.html", 'r') as f:
#     html_string = f.read()


def write():
    st.title("Google Playstore Analytics")
    st.write(
        "Trends in App Store Data, App Reviews and Prediction of Individual Star Ratings")
    st.write(
        """
        Team members:
        
        - Chua Wan Yun
        - Tey Siew Wen
        - Marooth Nath Chaowanastier
        """)
    st.image("website/assets/logo.png", use_column_width=True)
