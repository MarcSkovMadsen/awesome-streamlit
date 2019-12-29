# pylint: disable=line-too-long
"""This is example shows how to **upload multiple files** via the
[File Uploader Widget](https://streamlit.io/docs/api.html?highlight=file%20upload#streamlit.file_uploader)

As far as I can see you can only upload one file at a time. So if you need multiple files in your
app, you need to store them in a static List or Dictionary. Alternatively they should be uploaded
as one .zip file.

Please note that file uploader is a **bit problematic** because
- You can only upload one file at the time.
- You get no additional information on the file like name, size, upload time, type etc. So you
cannot distinguish the files without reading the content.
- every time you interact with any widget, the script is rerun and you risk processing or storing
the file again!
- The file uploader widget is not cleared when you clear the cache and there is no way to clear the
file uploader widget programmatically.

Based on the above list I created [Issue 897](https://github.com/streamlit/streamlit/issues/897)

This example was based on
[Discuss 1445](https://discuss.streamlit.io/t/uploading-multiple-files-with-file-uploader/1445)
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
        static_store.clear()  # Hack to clear list if the user clears the cache and reloads the page
        st.info("Upload one or more `.py` files.")

    if st.button("Clear file list"):
        static_store.clear()
    if st.checkbox("Show file list?", True):
        st.write(list(static_store.keys()))
    if st.checkbox("Show content of files?"):
        for value in static_store.values():
            st.code(value)


main()
