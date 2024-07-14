from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open target main page")
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(5)

@when("Click on Cart icon")
def click_card(context):
    context.driver.find_element(By.CSS_SELECTOR,  "div[data-test='@web/CartIcon'] use[href*='Cart']").click()
    sleep(5)


@when("Click Sign In and From right side navigation menu, click Sign In")
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, ".sc-58ad44c0-3.kwbrXj.h-margin-r-x3").click()
    sleep(1)
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()
    sleep(5)


@when("Input {product_name} into search field")
def search_product_name(context, product_name):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']").send_keys(product_name)

@when("Click on search icon")
def click_search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(2)


@when("Click on Target circle")
def click_target_circle(context):
    sleep(5)
    context.driver.find_element(By.XPATH, "//span[contains(text(), 'Check out Target Circle deals')]").click()
    sleep(5)


@when("Click on add to card button")
def click_add_to_cart(context):
    sleep(5)
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test*='chooseOptionsButton'][id*=addToCartButton]").click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='shippingButton']").click()
    sleep(2)
    context.driver.find_element(By.XPATH, "//a[contains(text(), 'View cart')]").click()
    sleep(2)






