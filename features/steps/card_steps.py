from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then("Verify “Your cart is empty” message is shown")
def verify_empty_Cart(context):
    expected_text = "Your cart is empty"
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.sc-fe064f5c-0.dtCtuk").text
    assert expected_text in actual_text, f"{expected_text} is not shown"
    print("test case verify_empty_Cart passed")


@then("Verify the item is added to the cart")
def verify_added_item(context):
    expected_text = "subtotal"
    context.driver.wait = WebDriverWait(context.driver, 10)
    actual_text= context.driver.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class= 'h-margin-b-tight h-text-grayDark ']//span[@class = 'sc-93ec7147-3 fUVkzh']"))).text
    #actual_text= context.driver.find_element((By.XPATH, "//span[@data-test='cart-summary-subtotal']")).text
    assert expected_text in actual_text, f"{expected_text} not in {actual_text}"
    print("item is added to the card")

