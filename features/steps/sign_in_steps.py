from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then("Verify Sign In form opened")
def verify_sign_in_open(context):
    expected_text = "Sign into your Target account"
    context.app.sign_in_page.verify_sign_in_text(expected_text)


@when("Input {email} and {password} on SignIn page")
def input_email_and_password(context, email, password):
    context.app.sign_in_page.input_email_and_password(email, password)

@when("Click Sign In with password")
def click_sign_in_with_password(context):
    context.app.sign_in_page.click_sign_in_with_password()

@then("Verify user is logged in")
def verify_user_is_logged_in(context):
    context.app.sign_in_page.verify_user_is_logged_in()