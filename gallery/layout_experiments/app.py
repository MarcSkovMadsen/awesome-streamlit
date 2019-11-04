"""This application experiments with the (grid) layout and some styling

Can we make a compact dashboard across several columns and with a dark theme?"""
import streamlit as st


def main():
    st.sidebar.title("Layout and Style Experiments")
    st.sidebar.header("Settings")
    st.markdown(
        """
# Layout and Style Experiments

The basic question is. Can we create a multi-column dashboard with plots, numbers and text using
the CSS Grid? And preferably with a dark theme.
"""
    )

    select_block_container_style()

    st.markdown(
        """
    <style>
       .wrapper {
        display: grid;
        grid-template-columns: 100px 100px 100px;
        grid-gap: 10px;
        background-color: #fff;
        color: #444;
        }

        .box {
        background-color: #444;
        color: #fff;
        border-radius: 5px;
        padding: 20px;
        font-size: 150%;
        }

        .a {
                grid-column-start: 2;
                grid-column-end: 3;
                grid-row-start: 1;
                grid-row-end: 2;
            }
        .b {
            grid-column-start: 2;
            grid-column-end: 3;
            grid-row-start: 2;
            grid-row-end: 3;
        }
        .c {
            grid-column-start: 3;
            grid-column-end: 4;
            grid-row-start: 2;
            grid-row-end: 3;
        }
        .d {
            grid-column-start: 1;
            grid-column-end: 2;
            grid-row-start: 1;
            grid-row-end: 2;
        }
        .e {
            grid-column-start: 1;
            grid-column-end: 2;
            grid-row-start: 2;
            grid-row-end: 3;
        }
        .f {
            grid-column-start: 3;
            grid-column-end: 4;
            grid-row-start: 1;
            grid-row-end: 2;
        }
    </style>
    <div class="wrapper">
    <div class="box a">A</div>
    <div class="box b">B</div>
    <div class="box c">C</div>
    <div class="box d">D</div>
    <div class="box e">E</div>
    <div class="box f">F</div>
    </div>
""",
        unsafe_allow_html=True,
    )


def select_block_container_style():
    st.sidebar.header("Block Container Style")
    max_width = st.sidebar.slider("Select max-width in px", 100, 2000, 1200, 100)
    max_width_100_percent = st.sidebar.checkbox("Max-width: 100%?", False)
    padding_top = st.sidebar.number_input("Select padding top in rem", 0, 200, 5, 1)
    padding_right = st.sidebar.number_input("Select padding right in rem", 0, 200, 1, 1)
    padding_left = st.sidebar.number_input("Select padding left in rem", 0, 200, 1, 1)
    padding_bottom = st.sidebar.number_input(
        "Select padding bottom in rem", 0, 200, 10, 1
    )
    set_block_container_style(
        max_width,
        max_width_100_percent,
        padding_top,
        padding_right,
        padding_left,
        padding_bottom,
    )


def set_block_container_style(
    max_width: int = 1200,
    max_width_100_percent: bool = False,
    padding_top: int = 5,
    padding_right: int = 1,
    padding_left: int = 1,
    padding_bottom: int = 10,
):
    if max_width_100_percent:
        max_width_str = f"max-width: 100%;"
    else:
        max_width_str = f"max-width: {max_width}px;"
    st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        {max_width_str}
        padding-top: {padding_top}rem;
        padding-right: {padding_right}rem;
        padding-left: {padding_left}rem;
        padding-bottom: {padding_bottom}rem;
    }}
</style>
""",
        unsafe_allow_html=True,
    )


main()
