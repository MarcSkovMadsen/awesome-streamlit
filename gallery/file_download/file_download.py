import base64

import pandas as pd
import streamlit as st

st.header("File Download - A Workaround for small data")

text = """\
    There is currently (20191204) no official way of downloading data from Streamlit. See for
    example [Issue 400](https://github.com/streamlit/streamlit/issues/400)

    But I discovered a workaround
    [here](https://github.com/holoviz/panel/issues/839#issuecomment-561538340).

    It's based on the concept of
    [HTML Data URLs](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs)

    You can try it out below for a dataframe csv file download.

    The methodology can be extended to other file types. For inspiration see
    [base64.guru](https://base64.guru/converter/encode/file)
    """
st.markdown(text)

data = [(1, 2, 3)]
# When no file name is given, pandas returns the CSV as a string, nice.
df = pd.DataFrame(data, columns=["Col1", "Col2", "Col3"])
csv = df.to_csv(index=False)
b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
st.markdown(href, unsafe_allow_html=True)
