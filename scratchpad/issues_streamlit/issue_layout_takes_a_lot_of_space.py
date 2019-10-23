import pandas as pd
import plotly.express as px
import streamlit as st

data = {"x": [1, 2, 3, 4], "y": [2, 4, 6, 8]}

st.selectbox("Select x", options=["A", "B"])
st.selectbox("Select y", options=["A", "B"])
dataframe = pd.DataFrame(data)
fig = px.scatter(dataframe, x="x", y="x", title="Plot 1", height=400)
st.plotly_chart(fig, height=400)
st.slider("Select min and max", min_value=1, max_value=10, value=[1, 4])
