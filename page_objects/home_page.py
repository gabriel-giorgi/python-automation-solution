from base_page import BasePage
from project_page import ProjectPage


class HomePage(BasePage):
    #class
    project_loc = "projects"

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_projects_module(self):

        project_lnk_we = self.driver.find_element_by_class_name(self.project_loc)
        project_lnk_we.click();
        return ProjectPage(self.driver)


