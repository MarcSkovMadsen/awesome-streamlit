import streamlit as st


def html(body):
    st.markdown(body, unsafe_allow_html=True)


def css(body):
    html(f'<script type="text/css">{body}</script>')


def card(header, body, src_image, id_):
    lines = [
        "<style>div.card{background-color:lightblue;border-radius: 5px;box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);transition: 0.3s;}</style>",
        f'<div class="card" id="{id_}>',
        f'<img src="{src_img}" alt="Avatar" style="width:100%">',
        '<div class="container">',
        f"<h3><b>{header}</b></h3>",
        f"<p>{body}</p>",
        "</div>",
        "</div>",
    ]
    html("".join(lines))


src_img = "https://raw.githubusercontent.com/MarcSkovMadsen/awesome-streamlit/master/assets/streamlit-logo.png"
card("Header", "bla bla bla this is that end", src_img, "test")
