import altair as alt
import holoviews as hv
import holoviews.plotting.bokeh
import hvplot.pandas
import pandas as pd
import panel as pn
import plotly
import plotly.express as px
import streamlit as st
from bokeh.plotting import figure

pn.config.sizing_mode = "stretch_width"
pn.extension()
pn.extension("vega")
pn.extension("plotly")

data = {"x": [1, 2, 3], "y": [1, 2, 3]}
dataframe = pd.DataFrame(data)

intro = """
[Panel](https://panel.holoviz.org/index.html#) is a framework for creating awesome analytics apps
in Python. It provides a strong integration to the [HoloViz](http://holoviz.org/) ecosystem and many
other python packages.

Panel is a competing framework to Streamlit, but **Panel can also make Streamlit more
awesome**.

Panel is build on top of [Bokeh](https://docs.bokeh.org/en/latest/) and some of it's powers can
actually be used in Streamlit via `st.bokeh_chart`.

The key to use `st.bokeh_chart` is to convert the *Panel component* to a *Bokeh model* using
the method `.get_root()`.

You can use Panel in Streamlit to

- **layout objects** like plots into Columns, Rows, Tabs and Grids.
- **style objects**
    - You can better control the size and color of the components
    - You can specify css classes and use css to style
- get access to **additional cool python libraries** like
[VTK](https://panel.holoviz.org/reference/panes/VTK.html#panes-gallery-vtk).
    - Soon you will even be able to get access to all ipython widgets.
- use **Javascript** in your application.
- and so much more

What you cannot do in Streamlit (without a lot of hacks) is to react to events in the browser like
clicking a table or chart or changing the value of a Panel widget.

Visit the sister site [awesome-panel.org](https://awesome-panel.org) or some of the official
resources like the [Reference Gallery](https://panel.holoviz.org/reference/index.html) and the
[App Gallery](https://panel.holoviz.org/gallery/index.html) for more inspiration.

![Awesome-panel.org](https://github.com/MarcSkovMadsen/awesome-panel/blob/master/assets/images/awesome-panel-full-branded.gif?raw=true)
![Reference Gallery](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/gallery/panel_experiments/panel_reference_gallery.png?raw=true)
"""

intro_pane = pn.pane.Markdown(intro, name="Introduction")

hvplot_plot = dataframe.hvplot(x="x", y="y")
hvplot_pane = pn.pane.HoloViews(hvplot_plot, name="Holoviews Plot")

altair_plot = (
    alt.Chart(dataframe).mark_line().encode(x="x", y="y").properties(width="container", height=400)
)
altair_pane = pn.pane.Vega(altair_plot, name="Altair Plot")

plotly_plot = px.line(dataframe, x="x", y="y")
plotly_pane = pn.pane.Plotly(plotly_plot, name="Plotly Plot")


fig = figure()
fig.scatter([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 2, 1, 0, -1, -2, -3])

gspec = pn.GridSpec(sizing_mode="stretch_both", max_height=800, name="GridSpec")

gspec[0, :3] = pn.Spacer(background="#FF0000")
gspec[1:3, 0] = pn.Spacer(background="#0000FF")
gspec[1:3, 1:3] = fig
gspec[3:5, 0] = hv.Curve([1, 2, 3])
gspec[
    3:5, 1
] = "https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png"
gspec[4:5, 2] = pn.Column(
    pn.widgets.FloatSlider(), pn.widgets.ColorPicker(), pn.widgets.Toggle(name="Toggle Me!")
)


if st.checkbox("Only hv_plot?"):
    tabs = pn.Tabs(hvplot_pane)
else:
    tabs = pn.Tabs(intro_pane, hvplot_pane, altair_pane, plotly_pane, gspec)

# tabs.servable()
st.bokeh_chart(tabs.get_root())
