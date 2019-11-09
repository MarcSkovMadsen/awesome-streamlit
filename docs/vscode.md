# How to use Streamlit with VS Code

## Running Your Streamlit App

You can use the **multi-command** extension to configure a short cut to execute `streamlit run <relativeFile.py>`

You start by installing the multi-command extension and adding the configuration shown to your settings.json file.

![VS Code multi-command](_static/images/vscode_multi-command.png)

```json
{
    "command": "multiCommand.streamlitActiveFile",
    "label": "Streamlit: Run Active File",
    "description": "Streamlit run active file in active terminal",
    "sequence": [
        "workbench.action.terminal.focus",
        {
            "command": "workbench.action.terminal.sendSequence",
            "args": {
                "text": "streamlit run '${relativeFile}'\u000D"
            }
        }
    ]
},
```

Then you can execute your *streamlit run* command via the command palette (CTRL+SHIFT+P)

![VS Code multi-command execute](_static/images/vscode_multi-command_execute.png)

![VS Code multi-command Streamlit Run](_static/images/vscode_multi-command_streamlit_run.png)

Or you can setup a keyboard shortcut in your keybindings.json file to run Streamlit

![VS Code open keyboard settings](_static/images/vscode_open_keyboardshortcuts.png)

![VS Code keybindings](_static/images/vscode_keybindings_json.png)

![VS Code terminal](_static/images/vscode_terminal.png)

## Debugging

### Manual Debugging

You can **debug mannually** by inserting a `breakpoint()` (Python 3.7+) or `import pdb;pdb.set_trace()` (Python 3.6 or below) in your code.

![Debugging via breakpoint](_static/images/vscode_breakpoint.png)

### Integrated Debugging

You can also use the **integrated debugger** in VS Code via the [ptsvd](https://github.com/microsoft/ptvsd) Python package

Please note that [andaag](https://github.com/andaag) reported the below to not work on ubuntu 18.04.3 LTS with Python 3.6.8. He gets a `ValueError: signal only works in main thread` error. See [issue 648](https://github.com/streamlit/streamlit/issues/648). It's working really well for me on Windows with Python 3.7.4 though.

First you should `pip install ptsvd`.

Then you need to insert the following snippet in your `<your-app_name>.py` file.

```python
import ptvsd
ptvsd.enable_attach(address=('localhost', 5678))
ptvsd.wait_for_attach() # Only include this line if you always wan't to attach the debugger
```

Then you can start your Streamlit app

```bash
streamlit run <your-app_name>.py
```

Then you should configure your *Remote Attach: debug PTVSD option*

![Add Configuration](_static/images/vscode_add_configuration.png)

![Debug Configuration](_static/images/vscode_select_debugging_configuration.png)

and update to the below in your launch.json file. Please make sure that you manually insert the *redirectOutput* setting below.

```json
{
    "name": "Python: Remote Attach",
    "type": "python",
    "request": "attach",
    "port": 5678,
    "host": "localhost",
    "justMyCode": true,
    "redirectOutput": true,
    "pathMappings": [
        {
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "."
        }
    ]
}
```

Please note that by default you will be debugging your own code only.
If you wan't to debug into for example the streamlit code, then you can change the `justMyCode` setting from `true` to `false`.

Finally you can attach the debugger by clicking the debugger play button

![Python remote attach](_static/images/vscode_python_remote_attach.png)

and you can debug away.

![Integrated Debugger](_static/images/vscode_integrated_debugger.png)

#### Using a dedicated app_debug_vscode.py file for debugging

Adding and removing the *ptvsd* code above can be cumbersome. So a usefull trick is to setup a dedicated *app_debug_vscode.py* file for debugging.

Assuming your app.py file has a `def main():` function, then your *app_debug_vscode.py* file could look as follows

```python
"""Use this module for development with VS Code and the integrated debugger"""
import ptvsd
import streamlit as st

import app

# pylint: disable=invalid-name
markdown = st.markdown(
    """
## Ready to attach the VS Code Debugger!

![Python: Remote Attach](https://awesome-streamlit.readthedocs.io/en/latest/_images/vscode_python_remote_attach.png)

for more info see the [VS Code section at awesome-streamlit.readthedocs.io]
(https://awesome-streamlit.readthedocs.io/en/latest/vscode.html#integrated-debugging)
"""
)


ptvsd.enable_attach(address=("localhost", 5678))
ptvsd.wait_for_attach()

markdown.empty()

app.main()
```

then you run `streamlit run app_debug_vscode.py` instead of `streamlit run app.py` and attach the debugger.

For a use case see my [app.py](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/app.py) and [app_dev_vscode.py](https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/app_dev_vscode.py) files.

#### Using the integrated Debugging Console

When you are running your integrated debugging in VS Code, you can use the *Debugging Console* with
Streamlit if you `import streamlit as st`. Then you can write dataframes and charts to the browser window
and take a better look at your data, than you can in VS Code.

![Import Streamlit](_static/images/vscode_debugging_console1.png)
![Import Streamlit](_static/images/vscode_debugging_console2.png)
![Import Streamlit](_static/images/vscode_debugging_console3.png)

You should also remember to *print* your dataframes to the debugger console to get a nice formatting.

![Nice Print of DataFrame](_static/images/vscode_print_nice_dataframe.png)