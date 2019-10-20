import awesome_streamlit as ast
import pathlib
import subprocess
import time
import os
from selenium import webdriver


from selenium import webdriver


ROOT = pathlib.Path(__file__).parent
FILE = ROOT / "resource_urls.txt"

driver = webdriver.Chrome("C:/repos/private/awesomestreamlit/chromedriver.exe")

for resource in ast.database.RESOURCES:
    print(f"{resource.name}: {resource.url}")
    driver.get(resource.url)
    print("sleeping 15")
    time.sleep(15)
    print("save screenshot")
    driver.save_screenshot(f"{resource.name}.png")
    print("sleeping 3")
    time.sleep(3)

driver.close()
