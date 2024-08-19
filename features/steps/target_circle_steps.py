from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Verify target circle page is open")
def verify_target_circle_page(context):
    expected_text = "Meet the new"
    actual_text = context.driver.find_element(By.XPATH, "//span[contains(text(), 'Meet the new')]").text
    assert expected_text in actual_text, f"{expected_text} != {actual_text}"
    print("Verifying target circle page is open passed")


@then("Verify there are {number} benefit cells on the target circle page")
def verify_benefit_cells(context, number):
    benefit_cells = len(context.driver.find_elements(By.CSS_SELECTOR, ".h-margin-b-tiny"))
    assert benefit_cells == int(number), f"{benefit_cells} != {number}"


