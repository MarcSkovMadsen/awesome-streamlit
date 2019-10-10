"""Extensions of the streamlit api

For now these are hacks and hopefully a lot of them will be removed again as the streamlit api is
extended"""
import importlib
import config
import logging

logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s")


def write_page(module_):  # pylint: disable=redefined-outer-name
    """Writes the specified module

    Arguments:
        module_ {[type]} -- A module with a 'def write():' function
    """
    logging.info(f"module %s reloaded", module_)
    importlib.reload(module_)
    module_.write()
