from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ProjectPage(BasePage):
    # XPATH
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

    # name
    login_locator = "login"
    create_project_btn_loc = "commit";

    # class
    sign_in_loc = "login"
    project_loc = "projects"
    new_created_project_loc = "project root leaf "
    # Partial Link
    logged_as_loc = "/redmine/users"

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_create_new_project_form(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.new_project_loc)))
        new_project_we = self.driver.find_element_by_xpath(self.new_project_loc)
        new_project_we.click();
        return self

    def fill_project_name(self, projectname):
        self.wait.until(EC.presence_of_element_located((By.ID, self.project_name_txt_loc)))
        project_name_txt_we = self.driver.find_element_by_id(self.project_name_txt_loc)
        project_name_txt_we.send_keys(projectname)
        return self

    def set_project_modules(self, issue_tracking=None, time_tracking=None):
        new_project_modules_rd_is_issue_tracking_we = self.driver.find_element_by_id \
            (self.new_project_modules_rd_is_issue_tracking_loc)
        new_project_modules_rd_is_time_tracking_we = self.driver.find_element_by_id(
            self.new_project_modules_rd_is_time_tracking_loc)
        if issue_tracking:
            if not new_project_modules_rd_is_issue_tracking_we.is_selected():
                new_project_modules_rd_is_issue_tracking_we.click();
        if time_tracking:
            if not new_project_modules_rd_is_time_tracking_we.is_selected():
                new_project_modules_rd_is_time_tracking_we.click();
        return self

    def create_project_and_continue(self):
        actions = ActionChains(self.driver)
        create_project_btn_we = self.driver.find_element_by_name(self.create_project_btn_loc)
        actions.move_to_element(create_project_btn_we).perform()
        create_project_btn_we.click()
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, self.project_loc)))
        project_lnk_we = self.driver.find_element_by_class_name(self.project_loc)
        project_lnk_we.click();
        return self

    def get_list_project(self):
        list_project_we = self.driver.find_elements_by_xpath(self.list_projects_loc)
        list_projects = []
        for element in list_project_we:
            list_projects.append(element.text)
        return list_projects

    def is_project_created(self, project_name):
        list_project = self.get_list_project()
        return project_name in list_project
