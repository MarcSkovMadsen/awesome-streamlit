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

## Installing the streamlit repo for development using Visual Studio Online

I would like to experiment with and maybe contribute to the [streamlit/streamlit](https://github.com/streamlit/streamlit) repo.

There is an official Streamlit [Contributing guide](https://github.com/streamlit/streamlit/wiki/Contributing) I can follow to get up and running.

But I'm running on Windows 8.1 so it's a it problematic getting it up and running.

- I cannot install directly on Windows because the Makefile and associated tools are very dependent on Linux.
- I cannot use *Visual Studio Code Remote - Containers* as described [here](https://code.visualstudio.com/docs/remote/containers) because it requires Windows 10 (not 8.1) and Docker (not Docker Toolbox)
- Maybe I could have installed Linux on my machine. But ...
- I guess I could install in a Docker container locally but not integrate with VS Code. But that would not be efficient.

I then settled on trying out the new [Visual Studio Online](https://visualstudio.microsoft.com/services/visual-studio-online/) experience.

I got this working successfully after some time. Below I will describe the steps.

### Forking the streamlit repo

Forking a repository is a simple two-step process.

1 On GitHub navigate to the [streamlit/streamlit](https://github.com/streamlit/streamlit) repository
2 In the top-right corner of the page, click Fork

![Fork Button](https://help.github.com/assets/images/help/repository/fork_button.jpg)

That's it! Now I have a fork of the original streamlit/streamlit repository.

![Fork of Streamlit](_static/images/streamlit_fork.png)

### Creating the Streamlit Visual Studio Online environment

To create a docker container containing the streamlit/streamlit repo I followed step 1-4 of the offical [VS Code Quickstart Guide](https://docs.microsoft.com/en-us/visualstudio/online/quickstarts/vscode). But I replaced the `microsoft/vsonline-quickstart` with `<my-user-name>/streamlit`.

![Replicate with streamlit/streamlit](_static/images/vscode_vso_quickstarts_streamlitstreamlit.png)sp

Finally the environment was created

![Environment created](_static/images/vscode_vso_environment_created.png)

and I click the connect button and it connects.

![Environment connected](_static/images/vscode_vso_connected.png)

SEE THE TROUBLESHOOTING SECTION BELOW IF THE CONNECTION DOES NOT FINISH.

### Verifying the Environment

It's nice to see what is in the environment

```bash
vsonline:~/workspace$ python
Python 2.7.13 (default, Sep 26 2018, 18:42:22)
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
vsonline:~/workspace$ python3
Python 3.5.3 (default, Sep 27 2018, 17:25:39)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
vsonline:~/workspace$ cat /etc/os-release
PRETTY_NAME="Debian GNU/Linux 9 (stretch)"
NAME="Debian GNU/Linux"
VERSION_ID="9"
VERSION="9 (stretch)"
VERSION_CODENAME=stretch
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
vsonline:~/workspace/Python-3.7.4$ nproc
4
vsonline:~/workspace$```

### Installing Python 3.7.4

I followed [this](https://linuxize.com/post/how-to-install-python-3-7-on-debian-9/) guide with

- `3.7.3` replaced by `3.7.4`.
- `make -j 8`replaced by `make -j 4`

Please note that there will be plenty of time for coffea as the installation and tests take 30 minutes!

After verifying the installation I removed the temporary `Python-3.7.4.tar.xz` file and `Python-3.7.4` folder.

```bash
rm Python-3.7.4.tar.xz
rm -r Python-3.7.4
```

Note I also tried using **pyenv**. And it could install Python 3.7.4. But I never got it working with pipenv.

### Troubleshooting

#### Connecting to remote

Quite often VS Code cannot open the remote. I've filed an issue at [MicrosoftDocs/vsonline issue #153](https://github.com/MicrosoftDocs/vsonline/issues/153)

![Opening Remote issue](_static/images/vscode_vso_openingremote.png)

I have experienced a few times that if I **toggle Developer Tools** under the Help menu item then it starts reconnecting and succeeds. Strange :-)

![Developer Tools](_static/images/vscode_vso_developertools.png)

#### Following the Contributing guide

I could not exactly follow the [Contributing guide](https://github.com/streamlit/streamlit/wiki/Contributing). I've filed the issues I saw as [streamlit/streamlit issue #665](https://github.com/streamlit/streamlit/issues/665).
