from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@given("Open target main page")
def open_target(context):
    context.driver.get('https://www.target.com/')


@when("Click on Cart icon")
def click_card(context):
    context.driver.find_element(By.CSS_SELECTOR,  "div[data-test='@web/CartIcon'] use[href*='Cart']").click()


@when("Click Sign In and From right side navigation menu, click Sign In")
def click_sign_in(context):
    context.driver.wait = WebDriverWait(context.driver, 5)
    SIGN_IN_ELEMENT = (By.CSS_SELECTOR, ".sc-58ad44c0-3.kwbrXj.h-margin-r-x3")
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_ELEMENT)).click()
    SIGN_IN_NAV = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
    context.driver.wait.until(EC.element_to_be_clickable(SIGN_IN_NAV)).click()



@when("Input {product_name} into search field")
def search_product_name(context, product_name):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']").send_keys(product_name)

@when("Click on search icon")
def click_search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()



@when("Click on Target circle")
def click_target_circle(context):
    context.driver.wait = WebDriverWait(context.driver, 5)
    TARGET_CIRCLE_ELEMENT = (By.XPATH, "//span[contains(text(), 'Join today to get Target Circle deals')]")
    context.driver.wait.until(EC.element_to_be_clickable(TARGET_CIRCLE_ELEMENT)).click()


@when("Click on add to card button")
def click_add_to_cart(context):

    context.driver.wait = WebDriverWait(context.driver, 5)
    elements = context.driver.find_elements(By.CSS_SELECTOR, "button[data-test*='chooseOptionsButton'][id*=addToCartButton]")
    first_element = context.driver.wait.until(EC.element_to_be_clickable(elements[0]))
    sleep(5) #I have to put this sleep here because otherwise I get the error "The element is not clickable at point X. Other element would receive the click"
    first_element.click()
    ADD_TO_CART = (By.CSS_SELECTOR, "button[data-test='shippingButton'][id*='addToCartButtonOrText']")
    add_to_cart_button = context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART))
    add_to_cart_button.click()
    view_cart_element = context.driver.find_element(By.XPATH, "//a[contains(text(), 'View cart')]")
    context.driver.wait.until(EC.element_to_be_clickable(view_cart_element))
    view_cart_element.click()







