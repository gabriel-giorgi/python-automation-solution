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
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.PROJECTS_LNK)))
        we_project_lnk = self.click_on_element(By.XPATH, self.PROJECTS_LNK)
        we_project_lnk.click()

    def delete_project(self, project_name):
        we_delete_icon = self.driver.find_element_by_xpath(self.DELETE_ICON_LOC.replace('replaceme',project_name.lower().replace(" ", "-")))
        we_delete_icon.click()
        we_confirm_delete = self.driver.find_element_by_id(self.CONFIRM_DELETE_RD)
        we_confirm_delete.click()
        self.driver.find_element_by_name(self.CONFIRM_DELETE_BTN).click()

    def go_to_projects_module(self):
        project_lnk_we = self.driver.find_element_by_class_name(self.PROJECT_LOC)
        project_lnk_we.click()
        return ProjectPage(self.driver)

