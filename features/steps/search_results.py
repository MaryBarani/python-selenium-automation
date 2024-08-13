from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    context.app.search_result_page.verify_text(search_word)

@then('Verify that every product has a product name a product image')
def verify_found_products_names_images(context):
     context.app.search_result_page.verify_products_names_images()


@when("Click on add to card button")
def click_add_to_cart(context):
 context.app.search_result_page.click_add_to_cart_btn()

