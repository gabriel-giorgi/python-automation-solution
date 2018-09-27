from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.home_page import HomePage


class LoginPage(BasePage):

    # ID
    USER_LOC = "username"
    PASSWORD_LOC = "password"
    LOGGED_AS_LOC = "loggedas"
    # name
    LOGIN_LOCATOR = "login"
    CREATE_PROJECT_BTN_LOC = "commit";
    # class
    SIGN_IN_LOC = "login"

    def __init__(self, driver):
        super().__init__(driver)

    def login_with(self, username, password):
        self.click_on_element(By.CLASS_NAME, self.SIGN_IN_LOC)
        self.enter_text(By.ID, self.USER_LOC, username)
        self.enter_text(By.ID, self.PASSWORD_LOC, password)
        self.click_on_element(By.NAME, self.LOGIN_LOCATOR)
        return HomePage(self.driver)

    def is_user_logged(self, user):
        logged_as_lbl_we = self.find(By.ID, self.LOGGED_AS_LOC)
        if logged_as_lbl_we.text.lower() == "logged in as " + user.lower() and self.driver.title == "Redmine":
            return True
        else:
            return False
