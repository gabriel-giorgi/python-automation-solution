from page_objects.administration_page import AdministrationPage
from page_objects.base_page import BasePage
from page_objects.project_page import ProjectPage


class HomePage(BasePage):
    # BY CLASS NAME
    PROJECT_LOC = "projects"
    ADMINISTRATION_LINK = "administration"

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_projects_module(self):
        project_lnk_we = self.driver.find_element_by_class_name(self.PROJECT_LOC)
        project_lnk_we.click()
        return ProjectPage(self.driver)

    def go_to_administration_module(self):
        administration_lnk_we = self.driver.find_element_by_class_name(self.ADMINISTRATION_LINK)
        administration_lnk_we.click()
        return AdministrationPage(self.driver)
