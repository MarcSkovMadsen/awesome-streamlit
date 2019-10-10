"""Extensions of the streamlit api

For now these are hacks and hopefully a lot of them will be removed again as the streamlit api is
extended"""
import importlib
import config
import logging
import pages.gallery

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def write_page(module_):  # pylint: disable=redefined-outer-name
    """Writes the specified module

    Arguments:
        module_ {[type]} -- A module with a 'def write():' function
    """
    if config.RELOAD_MODULES:
        try:
            importlib.reload(module_)
            logging.info(f"module %s reloaded", module_)
        except ImportError as identifier:
            if "module pages." in identifier.msg:
                importlib.reload(pages.gallery)
                logging.info(f"module %s reloaded", pages.gallery)

    module_.write()
