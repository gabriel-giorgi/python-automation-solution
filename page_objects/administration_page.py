from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.project_page import ProjectPage


class AdministrationPage(BasePage):

    DELETE_ICON_LOC = "//a[@href='/redmine/projects/replaceme']"
    CONFIRM_DELETE_RD = "confirm"
    CONFIRM_DELETE_BTN = "commit"
    PROJECT_BY_PAGE_100 = "//a[@href='/redmine/admin/projects?per_page=50']"
    PROJECTS_LNK = "//a[@href='/redmine/admin/projects']"
    LIST_PROJECTS_LOC = "//tr[@class= 'project root leaf ']/*[1]"
    PROJECT_LOC = "projects"

    def go_to_projects(self):
        self.click_on_element(By.XPATH, self.PROJECTS_LNK)

    def delete_project(self, project_name):
        delete_icon_locator = self.DELETE_ICON_LOC.replace('replaceme', project_name.lower().replace(" ", "-"))
        self.click_on_element(By.XPATH, delete_icon_locator)
        self.click_on_element(By.ID, self.CONFIRM_DELETE_RD)
        self.click_on_element(By.NAME, self.CONFIRM_DELETE_BTN)

    def go_to_projects_module(self):
        self.click_on_element(By.CLASS_NAME, self.PROJECT_LOC)
        return ProjectPage(self.driver)

