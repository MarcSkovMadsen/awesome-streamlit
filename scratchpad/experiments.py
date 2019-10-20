import streamlit as st


def html(body):
    st.markdown(body, unsafe_allow_html=True)


def card_begin_str(header):
    return (
        "<style>div.card{background-color:lightblue;border-radius: 5px;box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);transition: 0.3s;}</style>"
        '<div class="card">'
        '<div class="container">'
        f"<h3><b>{header}</b></h3>"
    )


def card_end_str():
    return "</div></div>"


def card(header, body):
    lines = [card_begin_str(header), f"<p>{body}</p>", card_end_str()]
    html("".join(lines))


def br(n):
    html(n * "<br>")


card("This works", "I can insert text inside a card")

br(2)

html(card_begin_str("This does not work"))
st.info("I cannot insert an st.info element inside a card")
html(card_end_str())
