from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Verify Sign In form opened")
def verify_sign_in_open(context):
    expected_text= "Sign into your Target account"
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.sc-fe064f5c-0.sc-315b8ab9-2.WObnm.gClYfs").text
    assert expected_text in actual_text, f"{expected_text} is not shown"
    print("test case 'Verify Sign In form opened' passed ")