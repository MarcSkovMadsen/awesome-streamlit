
import os

PAGES_SRC = {'src/sidebar': 'main_sidebar.py', 'src/utils': 'utils.py'}

def create_app_file(top_dir, name, pages):
    path = os.path.join(top_dir, name, "app.py")
    with open(file=path, mode="w") as f:
        ### IMPORT LIBRARIES AND MODULES ###
        f.write('import streamlit as st\n')
        f.write('import src.utils.utils as utils\n')
        f.write('\n\n')

        ### IMPORT PAGES ###
        f.write('import src.sidebar.main_sidebar as msb\n')
        for p in pages:
            f.write(f'import src.pages.{p} as {p}\n')

        ### DEFINE PAGES AS DICTIONARY ###
        f.write('\n')
        f.write('PAGES = {\n')
        i = 1
        for p in pages:
            if i != len(pages):
                f.write(f'\t"{p}": {p},\n')
            else:
                f.write(f'\t"{p}": {p}\n')
            i+=1
        f.write('}')

        ### DEFINE APP STRUCTURE ###
        f.write(f'\n\n')
        f.write(f'def main():\n')
        f.write(f'\t"""Main function of the App"""\n')
        f.write(f'\tst.sidebar.title("Navigation")\n')
        f.write(f'\tselection = st.sidebar.radio("", list(PAGES.keys()))\n')
        f.write(f'\tutils.write_page(msb)\n')
        f.write(f'\n\n')
        f.write(f'\tpage = PAGES[selection]\n')
        f.write(f'\n')
        f.write(f'\twith st.spinner(f"Loading page ..."):\n')
        f.write(f'\t\tutils.write_page(page)\n')
        f.write(f'\n\n')
        f.write(f'if __name__ == "__main__":\n')
        f.write(f'\tmain()\n')
        f.write(f'\n')

    return True

def create_default_pages(top_dir, name, pages=PAGES_SRC):
    for i in range(len(pages)):
        path = os.path.join(top_dir, name, list(pages.keys())[i], list(pages.values())[i])
        with open(file=path, mode="w") as f:
            f.write('')
    
    return True

def create_pages(top_dir, name, pages, elts):
    for p,e in zip(pages,elts):
        pp = p + ".py"
        path = os.path.join(top_dir, name, "src/pages", pp)
        with open(file=path, mode="w") as f:
            f.write('import streamlit as st\n')
            f.write('\n')
            f.write(f'PAGE_NAME = "{p}"\n')
            f.write('\n')
            f.write('def write():\n')
            f.write('\twith st.spinner(f"Loading {PAGE_NAME}..."):\n')
            f.write('\t\tst.write(f"This is {PAGE_NAME}")\n')
            #f.write(f'return True')
            f.write(f'\n')
            for i in range(int(e)):
                i = str(i)
                strg = f'\t\telt_{i} = st.empty()\n'
                f.write(strg)
                f.write('\n')
    
    return True

def write_default_utils_functions(top_dir, name, utils="src/utils/utils.py"):
    path = os.path.join(top_dir, name, utils)
    with open(file=path, mode="a+") as f:
        f.write('def write_page(page):\n')
        f.write('\t"""Writes the specified page/module\n')
        f.write('\tTo take advantage of this function, a multipage app should be structured into sub-files with a `def write()` function\n')
        f.write('\tArguments:\n')
        f.write('\t\tpage {module} -- A module with a "def write():" function\n')
        f.write('\t"""\n')
        f.write('\tpage.write()\n')
        f.write('\n')

def write_main_sidebar(top_dir, name, main_sidebar="src/sidebar/main_sidebar.py", maintainer=""):
    path = os.path.join(top_dir, name, main_sidebar)

    with open(file=path, mode="a+") as f:
        f.write('import streamlit as st\n')
        f.write('def write():\n')
        f.write('\tst.sidebar.title("About")\n')
        f.write('\tst.sidebar.info(\n')
        f.write('\t"""\n')
        f.write(f'\tThis app is maintained by {maintainer}.\n')
        f.write('\t"""\n')
        f.write('\t)\n')
        f.write('\n')

def create_batch_file(top_dir, name):
    path = os.path.join(top_dir, name, "run.bat")

    with open(file=path, mode="w") as f:
        f.write("streamlit run app.py")
