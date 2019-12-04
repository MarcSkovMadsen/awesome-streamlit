import streamlit as st
import pathlib
import pandas as pd
import numpy as np
import json


def main():
    specification_path = (
        pathlib.Path(__file__).parent
        / "specifications"
        / "connections_among_us_airports.json"
    )
    specification = specification_path.read_text()
    specification = specification.replace(
        '"url": "data/', '"url": "https://vega.github.io/vega-lite/examples/data/'
    )
    specification = json.loads(specification)
    st.vega_lite_chart(specification)


main()
