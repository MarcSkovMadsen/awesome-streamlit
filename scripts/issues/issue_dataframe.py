import streamlit as st

from yahooquery import Ticker

data = Ticker("ORSTED.CO").balance_sheet(frequency="annual")

st.header("Raw Data")
st.dataframe(data)

def get_default_format(data):
    format_dict = {}
    for column in data.columns:
        if data[column].dtype == "int64":
            format_dict[column] = "{0:,.0f}"
        elif data[column].dtype == "float64":
            format_dict[column] = "{0:,.2f}"
        else:
            format_dict[column] = "{0:}"
    return format_dict

st.header("Dataframe Index dropped and decimal symbol format applied")
data_reset_index = data.reset_index()
format_dict = get_default_format(data_reset_index)
st.dataframe(data_reset_index.style.format(format_dict))

st.header("Dataframe Index NOT dropped and decimal symbol format applied")
format_dict = get_default_format(data)
st.dataframe(data.style.format(format_dict))
