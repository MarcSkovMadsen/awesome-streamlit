from awesome_streamlit.core.services.resources import to_markdown
from awesome_streamlit.database import RESOURCES

resources = [resource for resource in RESOURCES if resource.is_awesome]
resources = sorted(resources, key=lambda x: x.name)

file = open("docs/awesome-list.md", "w")
awesome_list = to_markdown(resources)
awesome_list = (
    "# Awesome Streamlit Resources [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/MarcSkovMadsen/awesome-streamlit)\n"
    + awesome_list
)
file.write(awesome_list)
file.close()
