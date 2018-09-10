from behave import *
from page_objects.login_page import LoginPage

@given(u'I connect to redmine')
def step_impl(context):
    context.driver.get(context.redmine_url)


@when(u'I enter my username "{user}" and password "{password}"')
def step_impl(context, user, password):
    context.login_po = LoginPage(context.driver)
    context.login_po.login_with(user, password)


@then(u'I should see my username "{user}" logged in the homepage')
def step_impl(context, user):
    assert context.login_po.is_user_logged(user)


