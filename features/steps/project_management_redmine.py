from faker import Faker
from behave import *
from utils.config_handler import get_property_file_value
from utils.util import table_to_dict
from page_objects.login_page import LoginPage

fake = Faker()
use_step_matcher("re")


@given("I'm logged in redmine homepage")
def step_impl(context):
    context.driver.get(context.redmine_url)
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
    table = table_to_dict(context.table)
    context.project_po.go_to_create_new_project_form()
    context.project_po.fill_project_name(context.project_name)
    context.project_po.set_project_modules(table["issue_tracking"], table["time_tracking"], table["news"]
                                           , table["documents"], table["files"], table["wiki"],
                                           table["repository"], table["calendar"], table["gantt"])
    context.project_po.create_project_and_continue()


@then("I should see the project created inside management module")
def step_impl(context):
    assert context.project_po.is_project_created(context.project_name)


@when("I go to administration module")
def step_impl(context):
    context.admin_po = context.home_po.go_to_administration_module()


@step("I go to projects submodule")
def step_impl(context):
    context.admin_po.go_to_projects()


@step('I delete "(?P<project_name>.+)" project')
def step_impl(context, project_name):
    context.project_name = project_name
    context.admin_po.delete_project(project_name)


@then('I should not see "(?P<project_name>.+)" inside management module')
def step_impl(context, project_name):
    project_po = context.admin_po.go_to_projects_module()
    assert not project_po.is_project_created(project_name)

    # CLEAN UP
    # TODO move out this cleanup from here
    project_po.go_to_create_new_project_form()
    project_po.fill_project_name(context.project_name)
    project_po.create_project_and_continue()


@step("I go to issue statuses")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@step('I create following new status : "(?P<status_name>.+)"')
def step_impl(context, status_name):
    """
    :type context: behave.runner.Context
    :type status_name: str
    """
    pass