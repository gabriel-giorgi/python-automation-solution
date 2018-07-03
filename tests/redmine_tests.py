import os
import unittest
import time
from selenium import webdriver
from faker import Faker
from page_objects.login_page import LoginPage
from utils.config_handler import get_property_file_value

head, tail = os.path.split(os.path.dirname(os.path.abspath(__file__)))
CHROME_PATH = head + r"\drivers\chromedriver.exe"


class RedmineTestScript(unittest.TestCase):
    base_url = get_property_file_value('URL')
    faker = Faker()
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(3)
    def test_success_loggin(self):
        user = get_property_file_value('user')
        password = get_property_file_value('password')
        login_po = LoginPage(self.driver)
        login_po.login_with(user, password)
        time.sleep(10)
        # TODO asserts

    def tearDown(self):
        self.driver.close()

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_PATH)
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(3)

    def test_success_project_creation(self):
        user = get_property_file_value('user')
        password = get_property_file_value('password')
        project_name = self.faker.name()
        issue_tracking = True
        time_tracking = True
        login_po = LoginPage(self.driver)
        home_po = login_po.login_with(user, password)
        project_po = home_po.go_to_projects_module()
        project_po.go_to_create_new_project_form()
        project_po.fill_project_name(project_name)
        project_po.set_project_modules(issue_tracking, time_tracking)
        project_po.create_project_and_continue()
        assert project_po.is_project_created(project_name)

    def tearDown(self):
        self.driver.close()
