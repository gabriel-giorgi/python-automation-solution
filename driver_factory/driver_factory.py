from pip._internal.utils.misc import enum
from selenium import webdriver

# TODO --> IMPLEMENT DRIVER FACTORY
# TODO --> IMPLEMENT DRIVER FACTORY
# TODO --> IMPLEMENT DRIVER FACTORY

CHROME_PATH = r"C:\drivers\chromedriver.exe"


def get_driver(browser_name):
    if browser_name == "Chrome":
        driver = webdriver.Chrome(executable_path=CHROME_PATH)
        return driver


