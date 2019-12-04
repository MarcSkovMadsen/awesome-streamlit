import pandas as pd
import streamlit as st
import base64

st.header("File Download - A Workaround for small data")

text = """\
    There is currently (20191204) no official way of downloading data from Streamlit.

    But I discovered a workaround
    [here](https://github.com/holoviz/panel/issues/839#issuecomment-561538340).

    You can try it out below.
    """
st.markdown(text)

data = [(1, 2, 3)]
# When no file name is given, pandas returns the CSV as a string, nice.
df = pd.DataFrame(data, columns=["Col1", "Col2", "Col3"])
csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
href = f'<a href="data:file/csv;base64,{b64}">Download Table</a> (right-click and save as &lt;some_name&gt;.csv)'
st.markdown(href, unsafe_allow_html=True)
