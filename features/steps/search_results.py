from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text, f'Expected query not in results_heading'
    print("search product's test case passed")