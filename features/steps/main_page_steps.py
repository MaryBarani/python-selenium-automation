from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@given("Open target main page")
def open_target(context):
    context.app.main_page.open('https://www.target.com/')



@when("Click on Target circle")
def click_target_circle(context):
    context.driver.wait = WebDriverWait(context.driver, 5)
    TARGET_CIRCLE_ELEMENT = (By.XPATH, "//span[contains(text(), 'Join today to get Target Circle deals')]")
    context.driver.wait.until(EC.element_to_be_clickable(TARGET_CIRCLE_ELEMENT)).click()










