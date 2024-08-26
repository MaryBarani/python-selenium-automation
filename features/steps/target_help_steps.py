from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given("Open target help  page")
def open_help(context):
    context.driver.get('https://help.target.com/help ')


@given("Open target help return page")
def open_help_return(context):
    context.driver.get('https://help.target.com/help/subcategoryarticle?childcat=Returns&parentcat=Returns+%26+Exchanges&searchQuery=')


@given("Select {topic} from Browse help dropdown")
def select_topic(context, topic):
    context.app.help_page.select_drop_down_option(topic)

@then("Verify {expected_title} page is open")
def verify_expected_text(context, expected_title):
    context.app.help_page.verify_page_title(expected_title)

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


