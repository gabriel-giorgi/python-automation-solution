from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, url):
        self.driver.get(url)

    def find(self, locator_type, locator_value):
        return self.driver.find_element(locator_type, locator_value)
