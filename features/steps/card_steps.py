from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then("Verify “Your cart is empty” message is shown")
def verify_empty_Cart(context):
    context.app.cart_page.verify_cart_is_empty()


@then("Verify the item is added to the cart")
def verify_added_item(context):
    context.app.cart_page.verify_item_is_added_to_cart()

