from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open target help  page")
def open_help(context):
    context.driver.get('https://help.target.com/help ')
    sleep(5)


@then("Verify UI elements")
def verify_help_ui(context):
    context.driver.find_element(By.XPATH, "//h2[contains(text(),'Target Help')]")
    context.driver.find_element(By.CSS_SELECTOR, ".search-input")
    context.driver.find_element(By.CSS_SELECTOR, ".btn-sm.search-btn")
    num_of_box = len(context.driver.find_elements(By.CSS_SELECTOR, "div.box-column div.boxSmall.txtAC"))
    assert num_of_box == 6
    context.driver.find_element(By.CSS_SELECTOR, "div.salesforceBox.txtAC.bigbox1")
    num_of_box = len(context.driver.find_elements(By.CSS_SELECTOR, "div.grid_4.boxSmallr.txtAC.bigbox2"))
    assert num_of_box == 2
    context.driver.find_element(By.XPATH, "//h2[contains(text(), 'Browse all Help pages')]")
    print("test case Verify UI elements passed")


