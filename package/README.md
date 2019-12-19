# Awesome Streamlit Package.

This package supports the [Awesome Streamlit Project](https://github.com/MarcSkovMadsen/awesome-streamlit) and provides features that are not yet and maybe never will be provided by the [Streamlit package](https://pypi.org/project/streamlit/).

This package is currently **highly experimental** and

- The **api might change** dramatically and often!
  - If the Streamlit package starts providing the functionality, then it should be removed from this package.
- If you find a version that works for you, then please **pin the version number**!
  - An example of pinning the version number is `awesome-streamlit==20191014.2`.

You can install it using

```bash
pip install awesome-streamlit
```

You can use it using

```python
import awesome_streamlit as ast

ast.experiments.write_hello_world()
```

or alternatively if you just need the experimental features

```python
from awesome_streamlit import experiments as ste

ste.write_hello_world()
```

and the result should look like **Awesome Streamlit Gallery ![Awesome Streamlit Gallery](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)**.

For more information please visit the [Awesome Streamlit Project](https://github.com/MarcSkovMadsen/awesome-streamlit) on GitHub.
