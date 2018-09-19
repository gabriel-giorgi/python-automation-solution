from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage
from page_objects.home_page import HomePage


class LoginPage(BasePage):

    # XPATH
    NEW_PROJECT_LOC = ""
    new_project_loc = "//a[ @ href = '/redmine/projects/new']"
    save_project_btn_loc = "//input[@value = 'Save']";
    list_projects_loc = "//a[@class= 'project root leaf ']";

    # ID
    user_loc = "username"
    password_loc = "password"
    project_name_txt_loc = "project_name";
    project_description_txt_loc = "project_description"
    new_project_modules_rd_is_issue_tracking_loc = "project_enabled_module_names_issue_tracking"
    new_project_modules_rd_is_time_tracking_loc = "project_enabled_module_names_time_tracking"
    new_project_modules_rd_is_news_loc = "project_enabled_module_names_news"
    new_project_modules_rd_is_documents_loc = "project_enabled_module_names_documents"
    new_project_modules_rd_is_files_loc = "project_enabled_module_names_files"
    new_project_modules_rd_is_wiki_loc = "project_enabled_module_names_wiki"
    new_project_modules_rd_is_repository_loc = "project_enabled_module_names_repository"
    new_project_modules_rd_is_forums_loc = "project_enabled_module_names_boards"
    new_project_modules_rd_is_calendar_loc = "project_enabled_module_names_calendar"
    new_project_modules_rd_is_gantt_loc = "project_enabled_module_names_gantt"
    rd_is_project_public_loc = "project_is_public"
    logged_as_loc = "loggedas"

    # name
    login_locator = "login"
    create_project_btn_loc = "commit";

    # class
    sign_in_loc = "login"
    project_loc = "projects"
    new_created_project_loc = "project root leaf "
    # Partial Link

    def __init__(self, driver):
        super().__init__(driver)

    def login_with(self, username, password):
        self.click_on_element(By.CLASS_NAME, self.sign_in_loc)
        self.enter_text(By.ID, self.user_loc, username)
        self.enter_text(By.ID, self.password_loc, password)
        self.click_on_element(By.NAME, self.)
        login_bt_we = self.driver.find_element_by_name(self.login_locator)
        login_bt_we.click()

        return HomePage(self.driver)

    def is_user_logged(self, user):
        self.wait.until(EC.presence_of_element_located((By.ID, self.logged_as_loc)))
        logged_as_lbl_we = self.driver.find_element_by_id(self.logged_as_loc)
        if logged_as_lbl_we.text.lower() == "logged in as " + user.lower() and self.driver.title == "Redmine":
            return True
        else:
            return False
