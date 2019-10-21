import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from scipy.stats import norm


def write():
    plot_section()


def plot_section():
    st.markdown(
        """
## Interactive plot - Streamlit

"""
    )
    x = get_x()
    mu = st.slider(
        "mu", value=float(0), min_value=float(-5), max_value=float(5), step=float(0.1)
    )
    sigma = st.slider(
        "sigma",
        value=float(1),
        min_value=float(0.1),
        max_value=float(5),
        step=float(0.1),
    )
    plot_figure(x, mu, sigma)


@st.cache
def get_x():
    return np.linspace(-10, 10, 200)


def plot_figure(x, mu: float = 0, sigma: float = 1):
    y = norm.pdf(x, mu, sigma)
    title = f"Gaussian Density (mu = {mu} and sigma = {sigma})"
    plt.hist(y, bins=20)
    st.pyplot()


write()
