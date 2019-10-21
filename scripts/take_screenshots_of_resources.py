import logging
import pathlib
import subprocess
import time
import urllib.request

from PIL import Image
from selenium import webdriver

import awesome_streamlit as ast

ROOT = pathlib.Path(__file__).parent.parent / "assets/resources_screenshots"
FILE = ROOT / "resource_urls.txt"

logging.basicConfig(format="%(asctime)s - %(message)s", level=logging.INFO)


def main():
    driver = webdriver.Chrome("C:/repos/private/awesomestreamlit/chromedriver.exe")
    driver.set_window_size(1024, 1024)
    # driver.maximize_window()

    screenshot_non_gallery_resources(driver)
    screenshot_gallery_resources(driver)

    driver.close()


def screenshot_non_gallery_resources(driver):
    other_resources = [
        resource
        for resource in ast.database.RESOURCES
        if not ast.database.tags.APP_IN_GALLERY in resource.tags
    ]

    for index, resource in enumerate(other_resources):
        logging.info(
            f"{resource.name}: {resource.url}, {index}/{len(ast.database.RESOURCES)}"
        )

        screenshot_path = f"{ROOT/resource.screenshot_file}"
        thumbnail_path = f"{ROOT/'thumbnails'/resource.screenshot_file}"

        driver.get(resource.url)
        time.sleep(8)

        driver.save_screenshot(screenshot_path)
        logging.info("screenshot saved")

        image = Image.open(screenshot_path)
        image.thumbnail((512, 512), Image.ANTIALIAS)
        image.save(thumbnail_path, "png")
        logging.info("thumbnail saved")


def screenshot_gallery_resources(driver):
    gallery_resources = [
        resource
        for resource in ast.database.RESOURCES
        if ast.database.tags.APP_IN_GALLERY in resource.tags
    ]

    for index, resource in enumerate(gallery_resources):
        logging.info(
            f"{resource.name}: {resource.url}, {index}/{len(ast.database.RESOURCES)}"
        )

        screenshot_path = f"{ROOT/resource.screenshot_file}"
        thumbnail_path = f"{ROOT/'thumbnails'/resource.screenshot_file}"

        urllib.request.urlretrieve(resource.url, "tmp_code.py")
        p = subprocess.Popen(["streamlit", "run", "tmp_code.py"])
        time.sleep(10)
        driver.get("http://127.0.0.1:8000")
        time.sleep(20)

        driver.save_screenshot(screenshot_path)
        logging.info("screenshot saved")

        im = Image.open(screenshot_path)
        im.thumbnail((128, 128), Image.ANTIALIAS)
        im.save(thumbnail_path, "png")
        logging.info("thumbnail saved")

        p.terminate()
        p.wait()


if __name__ == "__main__":
    main()
