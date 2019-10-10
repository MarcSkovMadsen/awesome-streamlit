"""Home page shown when the user enters the application"""
import streamlit as st
import src.st_extensions
import src.st_awesome

# pylint: disable=line-too-long


def write():
    """Used to write the page in the app.py file"""
    src.st_awesome.title("")
    st.write(
        """
[Streamlit](https://streamlit.io/) is [announced](https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace) as being **The fastest way to build custom Machine Learning tools** but I believe it has the potential to become much more awesome than that.

I believe Streamlit has the **potential to become the Iphone of Data Science Apps**. And maybe it can even become the Iphone of Technical Writing, Code, Micro Apps and Python.

The purpose of this application is to

- Share a list of awesome Streamlit **resources**.
- Provide a **gallery** of awesome streamlit applications.
- Share a **vision** on how awesome Streamlit can be.

This an open source project and you are very welcome to **contribute** your awesome
comments, questions, resources and apps as
[issues](https://github.com/MarcSkovMadsen/awesome-streamlit/issues) or
[pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls).

This app is maintained by Marc Skov Madsen. I'm not an experienced open source maintainer,
so helpfull hints and suggestions are welcome.
You can learn more about me at [datamodelsanalytics.com](https://datamodelsanalytics.com)

## The Magic of Streamlit

The only way to truly understand how magical Streamlit is to play around with it
but if you need to be convinced first, then here is the **4 minute introduction** to Streamlit!

Afterwards you can go to the [Streamlit docs](https://streamlit.io/docs/) to get started.


"""
    )
    src.st_extensions.video_youtube(
        src="https://www.youtube.com/embed/B2iAodr0fOo"
    )
