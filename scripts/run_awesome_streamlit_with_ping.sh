#!/bin/bash
# The ping job will help keep awesome-streamlit.org alive.
# See https://lnx.azurewebsites.net/python-app-on-azure-web-apps-frequently-restarts/
python "scripts/ping_awesome_streamlit.py" &
top -d 60 -b &
streamlit run app.py