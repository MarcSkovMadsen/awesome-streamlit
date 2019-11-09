"""
## App: Iris EDA App
Author: [Jesse E.Agbe(JCharis)](https://github.com/Jcharis))\n
Source: [Github](https://github.com/Jcharis/Machine-Learning-Web-Apps/tree/master/Iris_EDA_Web_App)
Credits: Streamlit Team,Marc Skov Madsen(For Awesome-streamlit gallery)

Description
This is a simple Exploratory Data Analysis of the Iris Dataset depicting the various
species built with Streamlit.
We can preview the dataset,column names as well as show some basic plot with matplotlib and
seaborn.
There is also an image manipulation of a specie with changeable contrast and width using st.slider()

Purpose
To show a simple EDA of Iris using Streamlit framework.

"""
from io import BytesIO

# Plotting Pkgs
import matplotlib
import matplotlib.pyplot as plt
# EDA Pkgs
import numpy as np
import pandas as pd
import requests
# Plotting Pkgs
import seaborn as sns
import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter

matplotlib.use("Agg")  # Prevent runtime error due to tk
GITHUB_ROOT = "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/gallery/iris_eda_app/"


def main():
    st.title("Iris EDA App")
    st.subheader("EDA Web App with Streamlit ")
    st.markdown(
        """
		#### Description
		+ This is a simple Exploratory Data Analysis  of the Iris Dataset depicting the various species built with Streamlit.

		#### Purpose
		+ To show a simple EDA of Iris using Streamlit framework.
		"""
    )

    # Your code goes below
    # Our Dataset
    my_dataset = "iris.csv"

    # Load Our Dataset
    data = explore_data(my_dataset)

    # Show Dataset
    if st.checkbox("Preview DataFrame"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
        else:
            st.write(data.head(2))

    # Show Entire Dataframe
    if st.checkbox("Show All DataFrame"):
        st.dataframe(data)

    # Show All Column Names
    if st.checkbox("Show All Column Name"):
        st.text("Columns:")
        st.write(data.columns)

    # Show Dimensions and Shape of Dataset
    data_dim = st.radio("What Dimension Do You Want to Show", ("Rows", "Columns"))
    if data_dim == "Rows":
        st.text("Showing Length of Rows")
        st.write(len(data))
    if data_dim == "Columns":
        st.text("Showing Length of Columns")
        st.write(data.shape[1])

    # Show Summary of Dataset
    if st.checkbox("Show Summary of Dataset"):
        st.write(data.describe())

    # Selection of Columns
    species_option = st.selectbox(
        "Select Columns",
        ("sepal_length", "sepal_width", "petal_length", "petal_width", "species"),
    )
    if species_option == "sepal_length":
        st.write(data["sepal_length"])
    elif species_option == "sepal_width":
        st.write(data["sepal_width"])
    elif species_option == "petal_length":
        st.write(data["petal_length"])
    elif species_option == "petal_width":
        st.write(data["petal_width"])
    elif species_option == "species":
        st.write(data["species"])
    else:
        st.write("Select A Column")

    # Show Plots
    if st.checkbox("Simple Bar Plot with Matplotlib "):
        data.plot(kind="bar")
        st.pyplot()

    # Show Correlation Plots
    if st.checkbox("Simple Correlation Plot with Matplotlib "):
        plt.matshow(data.corr())
        st.pyplot()

    # Show Correlation Plots with Sns
    if st.checkbox("Simple Correlation Plot with Seaborn "):
        st.write(sns.heatmap(data.corr(), annot=True))
        # Use Matplotlib to render seaborn
        st.pyplot()

    # Show Plots
    if st.checkbox("Bar Plot of Groups or Counts"):
        v_counts = data.groupby("species")
        st.bar_chart(v_counts)

    # Iris Image Manipulation
    # @st.cache
    # def load_image(img):
    #     im = Image.open(os.path.join(img))
    #     return im

    # Select Image Type using Radio Button
    species_type = st.radio(
        "What is the Iris Species do you want to see?",
        ("Setosa", "Versicolor", "Virginica"),
    )

    if species_type == "Setosa":
        st.text("Showing Setosa Species")
        st.image(load_image("imgs/iris_setosa.jpg"), width=400)
    elif species_type == "Versicolor":
        st.text("Showing Versicolor Species")
        st.image(load_image("imgs/iris_versicolor.jpg"), width=400)
    elif species_type == "Virginica":
        st.text("Showing Virginica Species")
        st.image(load_image("imgs/iris_virginica.jpg"), width=400)

    # Show Image or Hide Image with Checkbox
    if st.checkbox("Show Image/Hide Image"):
        my_image = load_image("iris_setosa.jpg")
        enh = ImageEnhance.Contrast(my_image)
        num = st.slider("Set Your Contrast Number", 1.0, 3.0)
        img_width = st.slider("Set Image Width", 300, 500)
        st.image(enh.enhance(num), width=img_width)

    # About
    if st.button("About App"):
        st.subheader("Iris Dataset EDA App")
        st.text("Built with Streamlit")
        st.text("Thanks to the Streamlit Team Amazing Work")

    if st.checkbox("By"):
        st.text("Jesse E.Agbe(JCharis)")
        st.text("Jesus Saves@JCharisTech")


@st.cache(persist=True)
def explore_data(dataset):
    df = pd.read_csv(GITHUB_ROOT + dataset)
    return df


@st.cache
def load_image(img):
    response = requests.get(GITHUB_ROOT + img)
    return Image.open(BytesIO(response.content))


main()
