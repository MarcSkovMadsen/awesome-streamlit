"""In this app we show how to create a custom login widget in Streamlit using some different hacks

- `st.text_box` for transfering custom state like username and password between client and server
    - A small js/ React snippet for setting the value and triggering the keypress of the text_box.
- `st.bokeh_chart` for using custom html, css and javascript.

I see custom widgets as a way of enabling even more awesome analytics apps in Streamlit.

Using the ideas and hacks here you should be able to create custom widgets for clicks on tables,
plots and use any kind of Javascript library like for example
[Amphion Robotics](https://github.com/rapyuta-robotics/amphion/blob/devel/examples/README.md)

This hack could be generalized and wrapped into a more general api for creating custom widgets.

Some time in the future the Streamlit developers would develop a secure and robust api for
custom widgets making the need for this type of hack obsolete.

PLEASE NOTE THIS IS A HACK AND MAY NOT BE SECURE! **USE THIS AT YOUR OWN RISK!**
"""
import json
from typing import Dict, Optional

import streamlit as st
from bokeh.models import Div

# Simplification. Don't store passwords in text! Store the hash values only
USERS = {"admin": "logmeinplease!", "guest": "guest"}
# The Path only works if the custom_state_initialize function is run at the top of your code
CUSTOM_STATE_DIV_PATH = (
    "#root > div:nth-child(1) > div > div > div > section.main > div > div:nth-child(1) > "
    "div:nth-child(2)"
)
CUSTOM_STATE_INPUT_PATH = CUSTOM_STATE_DIV_PATH + " > div > div > div > input"
CUSTOM_STATE_STYLE = f"""
<style>
{CUSTOM_STATE_DIV_PATH} {{
    display: none;
}}
</style>
"""

# pylint: disable=line-too-long
# See https://stackoverflow.com/questions/23892547/what-is-the-best-way-to-trigger-onchange-event-in-react-js
# pylint: enable=line-too-long
DISPATCH_MESSAGE_CODE = f"""
var message = JSON.stringify(message_obj);
var channel = document.querySelectorAll('{CUSTOM_STATE_INPUT_PATH}')[0];

var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
nativeInputValueSetter.call(channel, message);
var ev2 = new Event('input', {{ bubbles: true}});
channel.dispatchEvent(ev2);

var ev = document.createEvent('Events');
ev.initEvent('keypress', true, true);
ev.keyCode = 13;
ev.which = 13;
ev.charCode = 13;
ev.key = 'Enter';
ev.code = 'Enter';
channel.dispatchEvent(ev);
"""


def main():
    """Run this function to run the app"""
    # custom widgets and custom_state_initialize() must be run at the top of your app code for now!
    custom_state_initialize()
    if not st.sidebar.checkbox(label="Show Custom State?", value=False):
        custom_state_hide()

    st.title("Custom Login Widget Hack")
    st.markdown(__doc__)

    if st.sidebar.checkbox(label="Show valid usernames and passwords?", value=True):
        text = "**Valid usernames/passwords**:\n" + "\n".join(
            ["- " + user + "/" + password for user, password in USERS.items()]
        )
        st.markdown(text)

    user = LoginWidget().login()
    if user:
        st.info(
            f"**{user}** is succesfully logged in! "
            "Clear the cache and reload the page to try again."
        )
        st.balloons()


@st.cache(allow_output_mutation=True)
def get_custom_state() -> Dict:
    """Holds the custom state

    Returns:
        Dict -- A dictionary like {"username": "", "password": ""} etc.
    """
    return {"username": "", "password": ""}


def custom_state_initialize():
    """Initialize the communication of Custom State between the client and the server

    Needs to be at the top of your code. Don't use any Streamlit `st.X` method prior to using this.
    """
    custom_state = get_custom_state()
    custom_state_str = json.dumps(custom_state)
    custom_state_str = st.text_input(label="Custom State", value=custom_state_str)
    custom_state.update(json.loads(custom_state_str))


def custom_state_hide():
    """Hides the text_box used by the Custom State to communicate between client and server"""
    st.write(CUSTOM_STATE_STYLE, unsafe_allow_html=True)


def custom_state_wrap_message_obj(code: str) -> str:
    """Wraps the widget message_obj code into something that can be synced using the custom state.

    Arguments:
        code {str} -- A JavaScript snippet to be run on the client. Must declare the message_obj
        variable.

    Returns:
        str -- [description]
    """
    return code + DISPATCH_MESSAGE_CODE


class LoginWidget:
    "A Custom Login Widget"

    def __init__(self):
        custom_state = get_custom_state()
        if "username" not in custom_state:
            custom_state["username"] = ""
        if "password" not in custom_state:
            custom_state["password"] = ""

        self.username = custom_state["username"]
        self.password = custom_state["password"]

    def __html__(self):
        js_code = f"""
var message_obj = {{
    username: document.getElementById('username').value,
    password: document.getElementById('password').value,
    }};
"""

        js_code = custom_state_wrap_message_obj(js_code)

        html_code = f"""
    <label for="username">Username:</label>
    <div style="width:100%"><input style="width:100%;background-color: #f0f2f6;border-style: none;" type="text" id="username" name="username" value="{self.username}"></div>
    <label for="pass">Password (8 characters minimum):</label>
    <div style="width:100%"><input style="width:100%;background-color: #f0f2f6;border-style: none;" type="password" id="password" name="password" minlength="8" required value="{self.password}"></div>
    <button type="button" onclick="{js_code}">Sign In</button>"""

        return html_code

    @property
    def is_logged_in(self) -> bool:
        """Whether or not the user is logged in

        Returns:
            bool -- True if the user has entered a valid combination of username and password
        """
        return self.username in USERS and USERS[self.username] == self.password

    def login(self) -> Optional[str]:
        """Runs the login procedure if the user is not already logged in

        Returns:
            Optional[str] -- The username if the user is logged in. Otherwise None.
        """
        if self.is_logged_in:
            return self.username

        # Sprinkle in your widget HTML/CSS/JAVASCRIPT Using Bokeh
        div = Div(text=self.__html__(), sizing_mode="stretch_width")
        st.bokeh_chart(div)
        if self.username:
            st.warning("The username or password is not valid! Please re-enter")

        return None


main()
