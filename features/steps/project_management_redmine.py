from faker import Faker
fake = Faker()
from behave import *
import config_handler
from config_handler import get_property_file_value
from login_page import LoginPage
use_step_matcher("re")
redmine_url = config_handler.get_property_file_value('URL')

@given("I'm logged in redmine homepage")
def step_impl(context):
    context.driver.get(redmine_url)
    context.login_po = LoginPage(context.driver)
    user = get_property_file_value("user")
    password = get_property_file_value("password")
    context.home_po = context.login_po.login_with(user, password)


@when("I go to project module")
def step_impl(context):
    context.project_po = context.home_po.go_to_projects_module()


@step("create a new project with following fields")
def step_impl(context):
    context.project_name = fake.name()
    print(str(context))
    context.project_po.go_to_create_new_project_form()
    context.project_po.fill_project_name(context.project_name)
    context.project_po.set_project_modules(context.row["issue_tracking"], context.row["time_tracking"], context.row["news"]
                                           , context.row["documents"], context.row["files"], context.row["wiki"],
                                           context.row["repository"], context.row["calendar"], context.row["gantt"])
    context.project_po.create_project_and_continue()


@then("I should see the project created inside management module")
def step_impl(context):
    assert context.project_po.is_project_created(context.project_name)


