"""This is a example shows how to upload multiple files via the File Uploader Widget

Once you upload multiple files it triggers multiple reruns of your script. One for each file.
You then need to process those files and maybe store them in a static List or Dictionary.
Here I store them in a List.

This example was based on
[Discourse 1445](https://discuss.streamlit.io/t/uploading-multiple-files-with-file-uploader/1445)
"""
from typing import List

import streamlit as st


@st.cache(allow_output_mutation=True)
def get_static_store():
    """This List is initialized once and can be used to store the files uploaded"""
    return []


def main():
    """Run this function to run the app"""
    static_store = get_static_store()

    st.info(__doc__)
    result = st.file_uploader("Upload", type="py")
    if result:
        # Process you file here

        # And add it to the static_store
        static_store.append(result)

    if st.button("Clear file list"):
        static_store.clear()
    for file in static_store:
        if file:
            st.code(file.getvalue())


main()
