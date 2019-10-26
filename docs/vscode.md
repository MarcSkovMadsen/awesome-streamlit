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

The you can execute you *streamlit run* command via the command palette (CTRL+SHIFT+P)

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

You can also use the **integrated debugger** in VS Code via the [ptsvd](https://github.com/microsoft/ptvsd) python package

First you should `pip install ptsvd`.

Then you need to insert the following snippet in your code

```python
import ptvsd
ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
ptvsd.wait_for_attach()
```

Then you can start your Streamlit app

```bash
streamlit run <your-app_name>.py
```

Then you should configure your *Remote Attach: debug PTVSD option*

![Add Configuration](_static/images/vscode_add_configuration.png)

![Debug Configuration](_static/images/vscode_select_debugging_configuration.png)

which should insert something similar to

```json
{
    "name": "Python: Remote Attach",
    "type": "python",
    "request": "attach",
    "port": 5678,
    "host": "localhost",
    "pathMappings": [
        {
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "."
        }
    ]
}
```

into your launch.json file.

Finally you can attach the debugger by clicking the debugger play button

![Python remote attach](_static/images/vscode_python_remote_attach.png)

and you can debug away.

![Integrated Debugger](_static/images/vscode_integrated_debugger.png)

#### Using the integrated Debugging Console

When you are running your integrated debugging in VS Code, you can use the *Debugging Console* with
Streamlit if you `import awesome_streamlit as st`. Then you can write dataframes and charts to the browser window
and take a better look at your data, than you can in VS Code.

![Import Streamlit](_static/images/vscode_debugging_console1.png)
![Import Streamlit](_static/images/vscode_debugging_console2.png)
![Import Streamlit](_static/images/vscode_debugging_console3.png)