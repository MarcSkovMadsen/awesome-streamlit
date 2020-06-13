import time

import streamlit as st

slider_ph = st.empty()
info_ph = st.empty()

value = slider_ph.slider("slider", 0, 100, 25, 1)
info_ph.info(value)

if st.button('animate'):
    for x in range(20):
        time.sleep(.5)

        value = slider_ph.slider("slider", 0, 100, value + 1, 1)
        info_ph.info(value)
