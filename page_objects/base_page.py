from selenium.webdriver.support.ui import WebDriverWait
from driver_factory import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePage():

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.wait = WebDriverWait(driver, 10)
    def navigate_to(self, url):
        self.driver.get(url)

