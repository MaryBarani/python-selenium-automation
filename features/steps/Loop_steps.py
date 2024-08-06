from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("Open target product {product_id} page")
def open_levi_products(context, product_id):
    context.driver.get(f"https://www.target.com/p/{product_id}")
    sleep(10)


@then('Verify each color has been selected')
def verify_colors(context):
    COLOR_OPTIONS = (By.CSS_SELECTOR, "ddiv.sc-a26a6bf9-0.koeyvB[aria-label='Carousel'] ul.sc-a26a6bf9-2.hjgjqB li.sc-a26a6bf9-3.kobkMm")
    SELECTED_COLOR = (By.CSS_SELECTOR, "div.sc-40df79dd-1.kda-dqB")
    expected_colors = ["dark khaki", "stone/grey", "white/sand/tan"]
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'