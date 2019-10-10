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
    try:
        importlib.import_module(module_.__name__)
        importlib.reload(module_)
    except ImportError as e:
        logging.info(
            f"""Warning. cannot reload %s. Please use streamlit run '%s' directly while developing""",
            module_,
            module_.__file__,
        )
    module_.write()
