# pylint: disable=line-too-long
"""This is example shows how to **upload multiple files** via the
[File Uploader Widget](https://streamlit.io/docs/api.html?highlight=file%20upload#streamlit.file_uploader)

Once you upload multiple files it triggers multiple reruns of your script. One for each file.
You then need to process those files and maybe store them in a static List or Dictionary.
Here I store them in a Dictionary.

Please note that file uploader is a **bit problematic** because every time you interact with any
widget, the script is rerun and you risk processing or storing the file again! I've tried to handle
that in the code below.

This example was based on
[Discourse 1445](https://discuss.streamlit.io/t/uploading-multiple-files-with-file-uploader/1445)
"""
# pylint: enable=line-too-long
from typing import Dict

import streamlit as st


@st.cache(allow_output_mutation=True)
def get_static_store() -> Dict:
    """This dictionary is initialized once and can be used to store the files uploaded"""
    return {}


def main():
    """Run this function to run the app"""
    static_store = get_static_store()

    st.info(__doc__)
    result = st.file_uploader("Upload", type="py")
    if result:
        # Process you file here
        value = result.getvalue()

        # And add it to the static_store if not already in
        if not value in static_store.values():
            static_store[result] = value
    else:
        st.info("Upload one or more `.py` files.")

    if st.button("Clear file list"):
        static_store.clear()
    if st.checkbox("Show file list?"):
        st.write(list(static_store.keys()))
    if st.checkbox("Show content of files?"):
        for value in static_store.values():
            st.code(value)


main()
