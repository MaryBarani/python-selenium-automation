from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SIGN_IN_ELEMENT = (By.CSS_SELECTOR, ".sc-58ad44c0-3.kwbrXj.h-margin-r-x3")
SIGN_IN_NAV = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")


@when("Click on Cart icon")
def click_card(context):
    context.app.header.click_cart()


@when("Click Sign In")
def click_sign_in(context):
    context.app.header.wait_and_click(SIGN_IN_ELEMENT)


@when("From right side navigation menu, click Sign In")
def click_nav_sign_in(context):
    context.app.header.wait_and_click(SIGN_IN_NAV)


@when("Input {product_name} into search field and Click on search icon")
def search_product_name(context, product_name):
    context.app.header.search(product_name)

