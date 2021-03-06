from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from page_objects.base_page import BasePage


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
        self.click_on_element(By.XPATH, self.new_project_loc)
        return self

    def fill_project_name(self, projectname):
        self.enter_text(By.ID,  self.project_name_txt_loc, projectname)
        return self

    def set_project_modules(self, issue_tracking, time_tracking, news, documents, files,
                            wiki, repository, calendar, gantt):
        new_project_modules_rd_is_issue_tracking_we = self.find(By.ID,
                                                                self.new_project_modules_rd_is_issue_tracking_loc)
        new_project_modules_rd_is_time_tracking_we = self.find(By.ID,
                                                               self.new_project_modules_rd_is_time_tracking_loc)
        new_project_modules_rd_is_news_we = self.find(By.ID, self.new_project_modules_rd_is_news_loc)
        new_project_modules_rd_is_documents_we = self.find(By.ID,
                                                           self.new_project_modules_rd_is_documents_loc)
        new_project_modules_rd_is_files_we = self.find(By.ID,
                                                       self.new_project_modules_rd_is_files_loc)
        new_project_modules_rd_is_wiki_we = self.find(By.ID, self.new_project_modules_rd_is_wiki_loc)
        new_project_modules_rd_is_repositoy_we = self.find(By.ID,
                                                           self.new_project_modules_rd_is_repository_loc)
        new_project_modules_rd_is_calendar_we = self.find(By.ID,
                                                          self.new_project_modules_rd_is_calendar_loc)
        new_project_modules_rd_is_gantt_we = self.find(By.ID,
                                                       self.new_project_modules_rd_is_gantt_loc)
        if issue_tracking:
            if not new_project_modules_rd_is_issue_tracking_we.is_selected():
                new_project_modules_rd_is_issue_tracking_we.click();
        elif new_project_modules_rd_is_issue_tracking_we.is_selected():
            new_project_modules_rd_is_issue_tracking_we.click();

        if time_tracking:
            if not new_project_modules_rd_is_time_tracking_we.is_selected():
                new_project_modules_rd_is_time_tracking_we.click();
        elif new_project_modules_rd_is_time_tracking_we.is_selected():
            new_project_modules_rd_is_time_tracking_we.click();

        if news:
            if not new_project_modules_rd_is_news_we.is_selected():
                new_project_modules_rd_is_news_we.click();
        elif new_project_modules_rd_is_news_we.is_selected():
            new_project_modules_rd_is_news_we.click();

        if documents:
            if not new_project_modules_rd_is_documents_we.is_selected():
                new_project_modules_rd_is_documents_we.click();
            elif new_project_modules_rd_is_documents_we.is_selected():
                new_project_modules_rd_is_documents_we.click();

        if files:
            if not new_project_modules_rd_is_files_we.is_selected():
                new_project_modules_rd_is_files_we.click();
            elif new_project_modules_rd_is_files_we.is_selected():
                new_project_modules_rd_is_files_we.click();

        if wiki:
            if not new_project_modules_rd_is_wiki_we.is_selected():
                new_project_modules_rd_is_wiki_we.click();
            elif new_project_modules_rd_is_wiki_we.is_selected():
                new_project_modules_rd_is_wiki_we.click();

        if repository:
            if not new_project_modules_rd_is_repositoy_we.is_selected():
                new_project_modules_rd_is_repositoy_we.click();
            elif new_project_modules_rd_is_repositoy_we.is_selected():
                new_project_modules_rd_is_repositoy_we.click();

        if calendar:
            if not new_project_modules_rd_is_calendar_we.is_selected():
                new_project_modules_rd_is_calendar_we.click();
            elif new_project_modules_rd_is_calendar_we.is_selected():
                new_project_modules_rd_is_calendar_we.click();

        if gantt:
            if not new_project_modules_rd_is_gantt_we.is_selected():
                new_project_modules_rd_is_gantt_we.click();
            elif new_project_modules_rd_is_gantt_we.is_selected():
                new_project_modules_rd_is_gantt_we.click();
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
