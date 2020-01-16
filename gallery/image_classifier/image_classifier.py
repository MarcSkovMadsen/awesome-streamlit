"""This is an image classifier app that enables a user to

- select a classifier model (in the sidebar),
- upload an image (in the main area)

and get a predicted classification in return.

This app is inspired by the awesome [imageNet](https://github.com/iamatulsingh/imageNet-streamlit)
application developed by [Atul Kumar Singh](https://github.com/iamatulsingh)."""
import os
from typing import Callable, List, NamedTuple, Tuple

import altair as alt
import keras.backend.tensorflow_backend as tb
import numpy as np
import pandas as pd
import streamlit as st
from keras.applications import (densenet, imagenet_utils, inception_v3,
                                mobilenet_v2, nasnet, resnet, vgg19, xception)
from keras.preprocessing.image import img_to_array, load_img
from PIL import Image

# Hack
# I get a '_thread._local' object has no attribute 'value' error without this
# See https://github.com/keras-team/keras/issues/13353#issuecomment-545459472
tb._SYMBOLIC_SCOPE.value = True  # pylint: disable=protected-access


class KerasApplication(NamedTuple):
    """We wrap a Keras Application into this class for ease of use"""

    name: str
    keras_application: Callable
    input_shape: Tuple[int, int] = (224, 224)
    preprocess_input_func: Callable = imagenet_utils.preprocess_input
    decode_predictions_func: Callable = imagenet_utils.decode_predictions
    url: str = "https://keras.io/applications/"

    def load_image(self, image_path: str) -> Image:
        """Loads the image from file

        Arguments:
            image_path {str} -- The absolute path to the image

        Returns:
            Image -- The image loaded
        """
        return load_img(image_path, target_size=self.input_shape)

    def to_input_shape(self, image: Image) -> Image:
        """Resizes the image to the input_shape

        Arguments:
            image {Image} -- The image to reshape

        Returns:
            Image -- The reshaped image
        """
        return image.resize(self.input_shape)

    @st.cache()
    def get_model(self) -> object:
        """The Keras model with weights="imagenet"

        Returns:
            [object] -- An instance of the keras_application with weights="imagenet"
        """
        return self.keras_application(weights="imagenet")

    def preprocess_input(self, image: Image) -> Image:
        """Prepares the image for classification by the classifier

        Arguments:
            image {Image} -- The image to preprocess

        Returns:
            Image -- The preprocessed image
        """
        # For an explanation see
        # https://stackoverflow.com/questions/47555829/preprocess-input-method-in-keras
        image = self.to_input_shape(image)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = self.preprocess_input_func(image)
        return image

    def get_top_predictions(
        self, image: Image = None, report_progress_func=print
    ) -> List[Tuple[str, str, float]]:
        """[summary]

        Keyword Arguments:
            image {Image} -- An image (default: {None})
            report_progress_func {Callable} -- A function like 'print', 'st.write' or similar
            (default: {print})

        Returns:
            [type] -- The top predictions as a list of 3-tuples on the form
            (id, prediction, probability)
        """
        report_progress_func(
            f"Loading {self.name} model ... (The first time this is done it may take several "
            "minutes)",
            10,
        )
        model = self.get_model()

        report_progress_func(f"Processing image ... ", 67)
        image = self.preprocess_input(image)

        report_progress_func(f"Classifying image with '{self.name}'... ", 85)
        predictions = model.predict(image)
        top_predictions = self.decode_predictions_func(predictions)

        report_progress_func("", 0)

        return top_predictions[0]

    @staticmethod
    def to_main_prediction_string(predictions) -> str:
        """A pretty string of the main prediction to output to the user"""
        _, prediction, _ = predictions[0]
        prediction_text = prediction.replace("_", " ").capitalize()
        prediction_query = prediction.replace("_", "+")
        prediction_url = f"http://www.image-net.org/search?q={prediction_query}"
        return f"It's a **[{prediction_text}]({prediction_url})**"

    @staticmethod
    def to_predictions_chart(predictions) -> alt.Chart:
        """A pretty chart of the (prediction, probability) to output to the user"""
        dataframe = pd.DataFrame(predictions, columns=["id", "prediction", "probability"])
        dataframe["probability"] = dataframe["probability"].round(2) * 100
        chart = (
            alt.Chart(dataframe)
            .mark_bar()
            .encode(
                x=alt.X("probability:Q", scale=alt.Scale(domain=(0, 100))),
                y=alt.Y(
                    "prediction:N",
                    sort=alt.EncodingSortField(field="probability", order="descending"),
                ),
            )
        )
        return chart


# pylint: enable=line-too-long

# See https://keras.io/applications/
DEFAULT_KERAS_APPLICATION_INDEX = 2
KERAS_APPLICATIONS: List[KerasApplication] = [
    KerasApplication(
        "DenseNet121",
        keras_application=densenet.DenseNet121,
        url="https://keras.io/applications/#densenet",
        preprocess_input_func=densenet.preprocess_input,
        decode_predictions_func=densenet.decode_predictions,
    ),
    KerasApplication(
        "InceptionV3",
        keras_application=inception_v3.InceptionV3,
        input_shape=(299, 299),
        url="https://keras.io/applications/#inceptionv3",
        preprocess_input_func=inception_v3.preprocess_input,
        decode_predictions_func=inception_v3.decode_predictions,
    ),
    KerasApplication(
        "MobileNetV2",
        keras_application=mobilenet_v2.MobileNetV2,
        url="https://keras.io/applications/#mobilenet",
        preprocess_input_func=mobilenet_v2.preprocess_input,
        decode_predictions_func=mobilenet_v2.decode_predictions,
    ),
    KerasApplication(
        "NASNetMobile",
        keras_application=nasnet.NASNetMobile,
        url="https://keras.io/applications/#nasnet",
        preprocess_input_func=nasnet.preprocess_input,
        decode_predictions_func=nasnet.decode_predictions,
    ),
    KerasApplication(
        "NASNetLarge",
        keras_application=nasnet.NASNetLarge,
        input_shape=(331, 331),
        url="https://keras.io/applications/#nasnet",
        preprocess_input_func=nasnet.preprocess_input,
        decode_predictions_func=nasnet.decode_predictions,
    ),
    KerasApplication(
        "ResNet50",
        keras_application=resnet.ResNet50,
        url="https://keras.io/applications/#resnet",
        preprocess_input_func=resnet.preprocess_input,
        decode_predictions_func=resnet.decode_predictions,
    ),
    KerasApplication(
        "VGG19",
        keras_application=vgg19.VGG19,
        url="https://keras.io/applications/#vgg19",
        preprocess_input_func=vgg19.preprocess_input,
        decode_predictions_func=vgg19.decode_predictions,
    ),
    KerasApplication(
        "Xception",
        keras_application=xception.Xception,
        input_shape=(299, 299),
        url="https://keras.io/applications/#inceptionv3",
        preprocess_input_func=xception.preprocess_input,
        decode_predictions_func=xception.decode_predictions,
    ),
]

IMAGE_TYPES = ["png", "jpg"]

# pylint: disable=line-too-long
def get_resources_markdown(model: KerasApplication) -> str:
    """Some info regarding Resources

    Arguments:
        model {KerasApplication} -- The KerasApplication employed

    Returns:
        str -- A Markdown string with links to relevant resources
    """

    return f"""### Resources

- [Keras](https://keras.io/)
  - [Keras Apps](https://keras.io/applications)
    - [{model.name} Docs]({model.url})
- Images
  - [ImageNet](http://www.image-net.org/)
  - [Awesome Images](https://github.com/heyalexej/awesome-images)
  - [Awesome-Streamlit Images](https://github.com/MarcSkovMadsen/awesome-streamlit/tree/master/gallery/image_classifier/images)
"""


# pylint: enable=line-too-long


def set_environ():
    """Sets environment variables for logging etc."""
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"


def main():
    """Run this to run the application"""
    set_environ()

    st.title("Image Classification with Keras and Tensorflow.")
    st.info(__doc__)
    st.sidebar.subheader("Classifier")
    selected_model = st.sidebar.selectbox(
        "Pick an image classifier model",
        options=KERAS_APPLICATIONS,
        index=DEFAULT_KERAS_APPLICATION_INDEX,
        format_func=lambda x: x.name,
    )
    st.sidebar.markdown(get_resources_markdown(selected_model))
    image = st.file_uploader("Upload a file for classification", IMAGE_TYPES)

    if image:
        st.image(image, use_column_width=True)
        image = Image.open(image)
        progress_bar = st.empty()
        progress = st.empty()

        def report_progress(message, value, progress=progress, progress_bar=progress_bar):
            if value == 0:
                progress_bar.empty()
                progress.empty()
            else:
                progress_bar.progress(value)
                progress.markdown(message)

        predictions = selected_model.get_top_predictions(
            image=image, report_progress_func=report_progress
        )

        st.subheader("Main Prediction")
        main_prediction = selected_model.to_main_prediction_string(predictions)
        st.write(main_prediction)

        st.subheader("Alternative Predictions")
        predictions_chart = selected_model.to_predictions_chart(predictions)
        st.altair_chart(predictions_chart)


main()
