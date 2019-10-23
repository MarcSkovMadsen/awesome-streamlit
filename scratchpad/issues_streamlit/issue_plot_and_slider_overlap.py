import pandas as pd
import plotly.express as px
import streamlit as st

data = {"x": [1, 2, 3, 4], "y": [2, 4, 6, 8]}

dataframe = pd.DataFrame(data)
fig = px.scatter(dataframe, x="x", y="x", title="Plot 1")
st.plotly_chart(fig)
st.slider("Select min and max", min_value=1, max_value=10, value=[1, 4])

fig = px.scatter(dataframe, x="x", y="x", title="Plot 2")
st.plotly_chart(fig, height=400)
st.slider("Select min and max 2", min_value=1, max_value=10, value=[1, 4])

fig = px.scatter(dataframe, x="x", y="x", height=400, title="Plot 3")
st.plotly_chart(fig)
st.slider("Select min and max 2", min_value=1, max_value=10, value=[1, 4])
