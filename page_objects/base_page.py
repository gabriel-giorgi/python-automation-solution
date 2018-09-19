from selenium.webdriver.support.ui import WebDriverWait
import logging
from selenium.webdriver.support import expected_conditions as EC
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, url):
        self.driver.get(url)

    def find(self, locator_type, locator_value):
        self.wait.until(EC.presence_of_element_located((locator_type, locator_value)))
        logging.warning("Locating element by locator type: " + locator_type + " --> value: " + locator_value)
        return self.driver.find_element(locator_type, locator_value)

    def click_on_element(self, locator_type, locator_value):
        self.find(locator_type, locator_value).click()
        logging.warning("Clicking on element located by: " + locator_type + " --> value: " + locator_value)

    def enter_text(self, locator_type, locator_value, text):
        self.find(locator_type, locator_value).send_keys(text)
        logging.warning("Filling text on element located by: " + locator_type + " --> value: " + locator_value + " ,text: " + text)

