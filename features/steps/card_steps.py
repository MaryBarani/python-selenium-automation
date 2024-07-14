from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Verify “Your cart is empty” message is shown")
def verify_empty_Cart(context):
    expected_text = "Your cart is empty"
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.sc-fe064f5c-0.dtCtuk").text
    assert expected_text in actual_text, f"{expected_text} is not shown"
    print("test case verify_empty_Cart passed")


@then("Verify the item is added to the cart")
def verify_added_item(context):
    expected_text = "subtotal"
    actual_text= context.driver.find_element(By.XPATH, "//span[@data-test='cart-summary-subtotal']").text
    assert expected_text in actual_text, f"{expected_text} not in {actual_text}"
    print("item is added to the card")

