import streamlit as st


class App:
    def run(self):
        st.title("Cannot st.cache classmethod issue")
        App.get_data1()
        st.info("data1 loaded")
        self.get_data2()
        st.info("data2 loaded")

    @classmethod
    @st.cache
    def get_data1(cls):
        pass

    @st.cache
    @classmethod
    def get_data2(cls):
        pass


App().run()
