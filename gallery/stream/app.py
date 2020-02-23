# Look here for documenting Python code: https://realpython.com/documenting-python-code/

import streamlit as st
import src.content as content
import src.structure as struct
import uuid
import os

def main():
    # Set up temporary directory.
    wd_dir = os.getcwd()
    if os.path.lexists(os.path.join(wd_dir, "tmp")) == False:
        os.mkdir(path = os.path.join(wd_dir, "tmp"))

    # App
    st.title("Stream")
    st.header("A streamlit application template generator")

    message = st.empty()
    
    st.write('<hr>', unsafe_allow_html=True)
    
    st.subheader("App location and name") # Directory section
    dir_ = st.text_input(label="Directory where to create the app.\nUse '\\\\' instead of '\\'.")
    st.write(dir_)

    app_name = st.text_input(label="Name of your application.")

    if app_name != "" and os.path.lexists(os.path.join(dir_, app_name)):
        message.error("Directory already exists.")


    # create temp directory for app - could be used for a future preview functionality
    if os.path.lexists(os.path.join(wd_dir, "tmp")):
        if os.path.lexists(os.path.join(wd_dir, "tmp", app_name))== False:
            os.mkdir(path = os.path.join(wd_dir, "tmp", app_name))

    st.write(app_name)
    st.info(f'Current working directory: {wd_dir}')

    st.subheader("App pages") # Pages section
    page_num = st.number_input(label="Number of pages in your app", min_value=1)

    st.write('<hr>', unsafe_allow_html=True)

    page_name=list()
    page_elt=list()

    for p in range(page_num):
        page_name_holder=st.text_input(label=f'Name of page #{p}', key=f'pn{p}')
        page_elt_holder=st.number_input(label=f'Number of elements on page #{p}', key='pe{p}', value=1)
        if page_name_holder != '':
            page_name.append(page_name_holder)
        if page_elt_holder != 0:
            page_elt.append(page_elt_holder)

    if st.button("Create"):
        if os.environ.get('AWESOME_STREAMLIT_ORG') != None:
            message.info("AWESOME_STREAMLIT_ORG environment variable exists, application not created.")
        else:
            if app_name != "" and os.path.lexists(os.path.join(dir_, app_name)):
                message = st.error("Directory already exists.")
            else:
                struct.create_dir_structure(top_dir=dir_, name=app_name)

                content.create_app_file(top_dir=dir_, name=app_name, pages=page_name)
                content.create_default_pages(top_dir=dir_, name=app_name)

                content.write_default_utils_functions(top_dir=dir_, name=app_name)
                content.write_main_sidebar(top_dir=dir_, name=app_name, maintainer="Fred")

                content.create_pages(top_dir=dir_, name=app_name, pages=page_name, elts=page_elt)
                
                content.create_batch_file(top_dir=dir_, name=app_name)
                
                message = st.info("Created application!")
        





if __name__ == "__main__":
    main()

# --- CODE TO DO DYNAMIC ASSIGNMENT OF WIDGETS ---
# to_be_deleted = set()
# for i in range(10):
#     delete = st.checkbox(f'delete {i}?', False, key=f'delete_{i}')
#     if delete:
#         to_be_deleted.add(i)
# st.write(to_be_deleted)