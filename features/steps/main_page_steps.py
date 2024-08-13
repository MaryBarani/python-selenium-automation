from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@given("Open target main page")
def open_target(context):
    context.app.main_page.open('https://www.target.com/')


@when("Click on Cart icon")
def click_card(context):
    context.app.header.click_cart()

@when("Click Sign In and From right side navigation menu, click Sign In")
def click_sign_in(context):
    context.driver.wait = WebDriverWait(context.driver, 5)
    SIGN_IN_ELEMENT = (By.CSS_SELECTOR, ".sc-58ad44c0-3.kwbrXj.h-margin-r-x3")
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_ELEMENT)).click()
    SIGN_IN_NAV = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_NAV)).click()



@when("Input {product_name} into search field and Click on search icon")
def search_product_name(context, product_name):
    # context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']").send_keys(product_name)
    context.app.header.search(product_name)


@when("Click on Target circle")
def click_target_circle(context):
    context.driver.wait = WebDriverWait(context.driver, 5)
    TARGET_CIRCLE_ELEMENT = (By.XPATH, "//span[contains(text(), 'Join today to get Target Circle deals')]")
    context.driver.wait.until(EC.element_to_be_clickable(TARGET_CIRCLE_ELEMENT)).click()










