"""Use this module for development with VS Code and the integrated debugger"""
import ptvsd

import app

ptvsd.enable_attach(address=("localhost", 5678))
ptvsd.wait_for_attach()

app.main()
