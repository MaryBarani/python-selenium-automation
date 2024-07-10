from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("Open target main page")
def open_target(context):
    context.driver.get('https://www.target.com/')

@when("Click on Cart icon")
def click_card(context):
    context.driver.find_element(By.CSS_SELECTOR,  "div[data-test='@web/CartIcon'] use[href*='Cart']").click()
    sleep(5)

@then("Verify “Your cart is empty” message is shown")
def verify_empty_Cart(context):
    expected_text = "Your cart is empty"
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.sc-fe064f5c-0.dtCtuk").text
    assert expected_text in actual_text, f"{expected_text} is not shown"
    print("test case verify_empty_Cart passed")


