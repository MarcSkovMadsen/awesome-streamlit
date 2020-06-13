from typing import List

import streamlit


def _autoflake_params(parent=streamlit.sidebar) -> dict:
    parent.subheader(
        "[Autoflake](https://github.com/myint/autoflake) Parameters")
    return {
        "expand_star_imports": parent.checkbox("Expand Star Imports",
                                               value=False),
        "remove_all_unused_imports": parent.checkbox(
            "Remove Unused Imports", value=False
        ),
        "remove_duplicate_keys": parent.checkbox("Remove Duplicate Keys",
                                                 value=False),
        "remove_unused_variables": parent.checkbox(
            "Remove Unused Variables", value=False
        ),
        "ignore_init_module_imports": parent.checkbox(
            "Ignore Init Module Imports", value=False
        ),
    }


def _autoflake(code: str, **params) -> str:
    import autoflake

    return autoflake.fix_code(code, **params)


def _autopep8_params(parent=streamlit.sidebar) -> dict:
    parent.subheader(
        "[Autopep8](https://github.com/hhatto/autopep8) Parameters")

    return {
        "aggressive": parent.checkbox("Aggressive", value=False),
        "max_line_length": line_length,
    }


def _autopep8(code: str, **params) -> str:
    import autopep8

    return autopep8.fix_code(code, options=params, encoding=None,
                             apply_config=False)


def _docformatter_params(parent=streamlit.sidebar) -> dict:
    parent.subheader(
        "[Docformatter](https://github.com/myint/docformatter) Parameters")
    return {
        "summary_wrap_length": parent.slider(
            "Summary Wrap Length", value=79, min_value=60, max_value=200
        ),
        "description_wrap_length": parent.slider(
            "Description Wrap Length", value=72, min_value=60, max_value=200
        ),
        "pre_summary_newline": parent.checkbox("Pre Summary Newline",
                                               value=False),
        "make_summary_multi_line": parent.checkbox(
            "Make Summary Multi Line", value=False
        ),
        "post_description_blank": parent.checkbox(
            "Post Description Blank", value=False
        ),
        "force_wrap": parent.checkbox("Force Wrap", value=False),
    }


def _docformatter(code: str, **params) -> str:
    import docformatter

    return docformatter.format_code(code, **params)


def _pyformat_params(parent=streamlit.sidebar) -> dict:
    parent.subheader(
        "[Pyformat](https://github.com/myint/pyformat) Parameters")
    return {
        "aggressive": parent.checkbox(
            "Aggressive", value=False, key="pyformat_aggressive"
        ),
        "remove_all_unused_imports": parent.checkbox(
            "Remove unused imports", value=False
        ),
        "remove_unused_variables": parent.checkbox(
            "Remove unused variables", value=False
        ),
    }


def _pyformat(code: str, **params) -> str:
    import pyformat

    return pyformat.format_code(
        code,
        aggressive=True,
        apply_config=False,
        remove_all_unused_imports=False,
        remove_unused_variables=False,
    )


def _yapf_params(parent=streamlit.sidebar) -> dict:
    parent.subheader("[YAPF](https://github.com/google/yapf) Parameters")
    return {
        "style_config": parent.selectbox(
            "Style Config", ("pep8", "google", "facebook", "yapf")
        )
    }


def _yapf(code: str, **params) -> str:
    from yapf.yapflib.yapf_api import FormatCode

    return FormatCode(code, **params)[0]


def _isort_params(parent=streamlit.sidebar) -> dict:
    parent.subheader(
        "[Isort](https://github.com/timothycrosley/isort) Parameters")
    return {}


def _isort(code: str, **params) -> str:
    from isort import SortImports

    return SortImports(file_contents=code).output


def _black_params(parent=streamlit.sidebar) -> dict:
    parent.subheader("[Black](https://github.com/psf/black) Parameters")
    return {
        "line_length": line_length,
        "string_normalization": parent.checkbox("string_normalization",
                                                value=True),
    }


def _black(code: str, **params) -> str:
    import black

    file_mode = black.FileMode(**params)
    return black.format_str(code, mode=file_mode)


formatter_map = {
    "black": (_black, _black_params),
    "autoflake": (_autoflake, _autoflake_params),
    "autopep8": (_autopep8, _autopep8_params),
    "docformatter": (_docformatter, _docformatter_params),
    "pyformat": (_pyformat, _pyformat_params),
    "yapf": (_yapf, _yapf_params),
    "isort": (_isort, _isort_params),
}


def _reformat(code: str, formatters: List[str]):
    """The main reformat function."""

    for formatter in formatters:
        formatter, params = formatter_map[formatter]
        params = params()
        code = formatter(code, **params)

    return code


formatters = streamlit.sidebar.multiselect(
    "Choose your formatters (the order matters)",
    list(formatter_map.keys()),
    default=["black"],
    key="python-formatters",
)

streamlit.sidebar.markdown("---")

streamlit.sidebar.subheader("Parameters")

line_length = streamlit.sidebar.slider(
    "Line Length", value=88, min_value=60, max_value=180
)

title = streamlit.title("Python Code Formatter")

default_text = '''
def format_your_code_here()  ->  None:
    """
    Choose your formatters from the (<=) sidebar on the left
    and set their parameters to see your code being formatted live.
    """


'''
text = streamlit.text_area("Type your code here", value=default_text,
                           height=300)

with streamlit.spinner("Formatting code ..."):
    streamlit.code(_reformat(text, formatters))
