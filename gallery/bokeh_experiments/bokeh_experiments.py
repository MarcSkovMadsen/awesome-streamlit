import datetime
import random

import bokeh
import bokeh.layouts
import bokeh.models
import bokeh.plotting
import markdown
import pandas as pd
import streamlit as st


def main():
    st.markdown(
        """
    # Bokeh Experiments

    [Bokeh](https://docs.bokeh.org/en/latest/) is an interactive visualization library for modern web
    browsers. Bokeh has an extensive
    [quickstart guide](https://docs.bokeh.org/en/latest/docs/user_guide/quickstart.html), a large
    [gallery of examples](https://docs.bokeh.org/en/latest/docs/gallery.html#gallery) and an extensive
    [reference guide](https://docs.bokeh.org/en/latest/docs/reference.html#refguide)


    You can use it in Streamlit to show charts via
    [`st.bokeh_chart`](https://streamlit.io/docs/api.html?highlight=bokeh_chart#streamlit.bokeh_chart)


    ```python
    import streamlit as st
    import bokeh.plotting
    circle_chart = bokeh.plotting.figure(sizing_mode="stretch_width", height=200)
    circle_chart.circle(
        [1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5
    )
    st.bokeh_chart(circle_chart)
    ```
    """
    )
    # st.echo causing error when run via eval. So I've included the code above directly

    sidebar_settings()

    circle_chart = bokeh.plotting.figure(sizing_mode="stretch_width", height=200)
    circle_chart.circle(
        [1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5
    )
    st.bokeh_chart(circle_chart)

    st.markdown(
        """
    As you will see below you can actually take advantage of many of the super powers of Bokeh
    like layouts, widgets, jslink and potentially even Python callbacks.

    The technical reason being that
    [`st.bokeh_chart`](https://streamlit.io/docs/api.html?highlight=bokeh_chart#streamlit.bokeh_chart)
    is capable of using
    [`bokeh.model.Model`](https://docs.bokeh.org/en/latest/docs/reference/model.html) and not just
    [`bokeh.plotting.Figure`](https://docs.bokeh.org/en/latest/docs/reference/plotting.html)
    objects.

    Feel free to contribute to the code in the
    [awesome-streamlit repo](https://github.com/MarcSkovMadsen/awesome-streamlit/).

    ## Try it out!
    """
    )

    tabs = bokeh.models.Tabs(
        tabs=[
            plotting_panel(),
            layout_panel(),
            widgets_tables_panel(),
            widgets_panel(),
            js_callbacks_panel(),
            vision_panel(),
        ]
    )
    st.bokeh_chart(tabs)


def sidebar_settings():
    """Add selection section for setting setting the max-width and padding
    of the main block container"""
    st.sidebar.header("Bokeh Experiments")
    max_width_100_percent = st.sidebar.checkbox("Max-width?", False)
    if not max_width_100_percent:
        max_width = st.sidebar.slider("Select max-width in px", 100, 2000, 1200, 100)
    else:
        max_width = 1200

    _set_block_container_style(max_width, max_width_100_percent)


def _set_block_container_style(
    max_width: int = 1200, max_width_100_percent: bool = False
):
    if max_width_100_percent:
        max_width_str = f"max-width: 95%;"
    else:
        max_width_str = f"max-width: {max_width}px;"
    st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
</style>
""",
        unsafe_allow_html=True,
    )


def _chart():
    circle_chart = bokeh.plotting.figure(sizing_mode="stretch_both")
    circle_chart.circle(
        [1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5
    )
    return circle_chart


def plotting_panel():
    chart = bokeh.plotting.figure(sizing_mode="stretch_width", height=400)
    chart.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=3, color="navy", alpha=0.5)
    text = """
<br/>Below a simple `bokeh.plotting.figure` line chart is shown.
    """
    column = bokeh.layouts.Column(
        children=[_markdown(text), chart], sizing_mode="stretch_width"
    )
    return bokeh.models.Panel(child=column, title="Plotting")


def layout_panel():
    text = """
<br/>With Bokeh you can do advanced
[layouts](https://docs.bokeh.org/en/latest/docs/reference/layouts.html).
Below a simple `bokeh.layouts.grid` with a plot, text and image is shown.
    """
    grid = bokeh.layouts.grid(
        children=[
            _markdown(text),
            [_image(), _paragraph()],
            [_chart(), _spacer("rgb(246,1,102)")],
        ],
        sizing_mode="stretch_width",
    )
    return bokeh.models.Panel(child=grid, title="Layouts")


def widgets_tables_panel():
    N = 10
    data = dict(
        dates=[datetime.date(2014, 3, i + 1) for i in range(N)] * 100,
        downloads=[random.randint(0, 100) for i in range(N)] * 100,
    )
    source = bokeh.models.ColumnDataSource(data)

    columns = [
        bokeh.models.widgets.TableColumn(
            field="dates", title="Date", formatter=bokeh.models.widgets.DateFormatter()
        ),
        bokeh.models.widgets.TableColumn(field="downloads", title="Downloads"),
    ]
    data_table = bokeh.models.widgets.DataTable(
        source=source, columns=columns, height=280, sizing_mode="stretch_width"
    )
    text = """
<br>With Bokeh you can do advanced
[bokeh.models.widgets.tables](https://docs.bokeh.org/en/latest/docs/reference/models/widgets.tables.html).

Below a simple `bokeh.models.widgets.DataTable` is shown. I believe you can do very advanced things with
the DataTable like filtering and formatting!
    """
    column = bokeh.layouts.Column(
        children=[_markdown(text), data_table], sizing_mode="stretch_width"
    )
    return bokeh.models.Panel(child=column, title="Tables")


def vision_panel():
    text = """
## My Vision on the Bokeh Streamlit Integration

I believe the integration with Bokeh **can give Streamlit Super Powers** if improved slightly.

For example

- Wrapping the Bokeh api into a more **Streamlit like Api** like `st.bokeh.datatable(my_dataframe)`
- Enabling **Python Callbacks** for advanced interactivity. I have a gut feeling it's easy to integrate because
  - Streamlit and Bokeh are both Tornado Applications.
  - There are already a lot of tutorials on integrations with Flask, Django and Jupyter Notebooks.

I believe the integration with Bokeh also can have a downside.
Personally I find the Bokeh documentation and api hard to learn, navigate and use.
And I start spending a lot of time on layout and formatting because I can!
Is it **Pandoras Box** that I've opened?

I believe it should be considered whether the improved integration should be with Bokeh or
[Panel](https://github.com/holoviz/panel). Panel could provide integration to the full suite of
PyViz tools and more advanced layouts and widgets.

I will be adding more examples when I get the time.
"""
    return bokeh.models.Panel(child=_markdown(text), title="Vision")


def js_callbacks_panel():
    x = [x * 0.005 for x in range(0, 200)]
    y = x

    source = bokeh.models.ColumnDataSource(data=dict(x=x, y=y))

    plot = bokeh.plotting.Figure(plot_width=400, plot_height=400)
    plot.line("x", "y", source=source, line_width=3, line_alpha=0.6)

    callback = bokeh.models.CustomJS(
        args=dict(source=source),
        code="""
        var data = source.data;
        var f = cb_obj.value
        var x = data['x']
        var y = data['y']
        for (var i = 0; i < x.length; i++) {
            y[i] = Math.pow(x[i], f)
        }
        source.change.emit();
    """,
    )

    slider = bokeh.models.Slider(start=0.1, end=4, value=1, step=0.1, title="power")
    slider.js_on_change("value", callback)

    text = """<br>
Bokeh enables advanced, custom and interactive widgets via
[`bokeh.models.callbacks`](https://docs.bokeh.org/en/latest/docs/reference/models/callbacks.html?highlight=customjs#bokeh.models.callbacks.CustomJS)
in JavaScript.

**Try moving the slider!**
"""
    layout = bokeh.layouts.column(
        _markdown(text), slider, plot, sizing_mode="stretch_width"
    )
    return bokeh.models.Panel(child=layout, title="JS Callbacks")


def widgets_panel():
    text = """
## Bokeh Widgets

I don't yet know how to enable **Bokeh Widgets** with powerfull **Python Callbacks**.

But I have a gut feeling it should be easy to integrate because
- Streamlit and Bokeh are both Tornado Applications.
- There are already a lot of tutorials on integrations with Flask, Django and Jupyter Notebooks.

So if you know how to do it feel free to reach out or do a pull request at
[awesome-streamlit/](https://github.com/MarcSkovMadsen/awesome-streamlit/)

For technical information see

- [Bokeh Server - User Guide](https://docs.bokeh.org/en/latest/docs/user_guide/server.html)
- [Bokeh Server - Developer Guide](https://docs.bokeh.org/en/latest/docs/dev_guide/server.html#devguide-server)
- [Flask embedding example](https://github.com/bokeh/bokeh/blob/1.1.0/examples/howto/server_embed/flask_embed.py)

If we could get the integration working we would have access the full set of **Bokeh interactive widgets**
as found in the [Bokeh User Guide](https://docs.bokeh.org/en/latest/docs/user_guide/interaction/widgets.html) and shown below

## Try it out!
"""
    button = bokeh.models.widgets.Button(label="Foo", button_type="success")
    checkbox_button_group = bokeh.models.widgets.CheckboxButtonGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])
    checkbox_group = bokeh.models.widgets.CheckboxGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=[0, 1])
    menu = [("Item 1", "item_1"), ("Item 2", "item_2"), None, ("Item 3", "item_3")]
    dropdown = bokeh.models.widgets.Dropdown(label="Dropdown button", button_type="warning", menu=menu)
    text_input = bokeh.models.widgets.TextInput(value="default", title="Text Input:")
    color_picker = bokeh.models.widgets.ColorPicker(color="#ff4466", title="Choose color:", width=200)
    file_input = bokeh.models.widgets.FileInput()
    multi_select =  bokeh.models.widgets.MultiSelect(title="Option:", value=["foo", "quux"],
                           options=[("foo", "Foo"), ("bar", "BAR"), ("baz", "bAz"), ("quux", "quux")])
    radio_button_group = bokeh.models.widgets.RadioButtonGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=0)
    radio_group = bokeh.models.widgets.RadioGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=0)

    select = bokeh.models.widgets.Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])
    slider = bokeh.models.widgets.Slider(start=0, end=10, value=1, step=.1, title="Stuff")
    range_slider = bokeh.models.widgets.RangeSlider(start=0, end=10, value=(1,9), step=.1, title="Stuff")
    text_input = bokeh.models.widgets.TextAreaInput(value="default", rows=6, title="Label:")
    toggle = bokeh.models.widgets.Toggle(label="Foo", button_type="success")
    div = bokeh.models.widgets.Div(text="""Your <a href="https://en.wikipedia.org/wiki/HTML">HTML</a>-supported text is initialized with the <b>text</b> argument.  The
remaining div arguments are <b>width</b> and <b>height</b>. For this example, those values
are <i>200</i> and <i>100</i> respectively.""",
width=200, height=100)
    paragraph = bokeh.models.widgets.Paragraph(text="""Your text is initialized with the 'text' argument.  The
    remaining Paragraph arguments are 'width' and 'height'. For this example, those values
    are 200 and 100 respectively.""",
    width=200, height=100)
    pretext = bokeh.models.widgets.PreText(text="""Your text is initialized with the 'text' argument.

The remaining Paragraph arguments are 'width' and 'height'. For this example,
those values are 500 and 100 respectively.""",
width=500, height=100)

    column = bokeh.layouts.column(
        _markdown(text),
        button,
        checkbox_button_group,
        checkbox_group,
        dropdown,
        text_input,
        color_picker,
        file_input,
        multi_select,
        radio_group,
        radio_button_group,
        select,
        slider,
        range_slider,
        text_input,
        toggle,
        div,
        paragraph,
        pretext,
        sizing_mode="stretch_width"
    )

    return bokeh.models.Panel(child=column, title="Widgets")


def _markdown(text):
    return bokeh.models.widgets.markups.Div(
        text=markdown.markdown(text), sizing_mode="stretch_width"
    )


def _paragraph():
    return bokeh.models.widgets.markups.Paragraph(
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n\n"
        * 4,
        sizing_mode="stretch_width",
    )


def _spacer(background=None):
    return bokeh.layouts.Spacer(background=background, sizing_mode="scale_both")


def _image():
    return bokeh.models.widgets.markups.Div(
        text='<img src="https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/assets/awesome-streamlit-org.png?raw=true" style="width:500px"></img>',
        sizing_mode="scale_both",
    )

main()
