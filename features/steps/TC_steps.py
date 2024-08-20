from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Verify Terms and Conditions page is opened")
def verify_terms_and_conditions(context):
    context.app.TCPage.verify_Tc_is_Open()


@then("User can close new window and switch back to original")
def verify_user_can_go_back(context):
    context.app.TCPage.close_window()
    context.app.sign_in_page.switch_to_original_window()