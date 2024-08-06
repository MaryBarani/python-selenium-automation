from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text, f'Expected query not in results_heading'
    print("search product's test case passed")

@then('Verify that every product has a product name a product image')
def verify_found_products_names_images(context):
    PRODUCT = (By.CSS_SELECTOR, "div[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    products = context.driver.find_elements(*PRODUCT)
    for product in products:
        product_name = product.find_element(By.CSS_SELECTOR, "[data-test='product-title']")
        product_image = product.find_element(By.CSS_SELECTOR, "picture[data-test='@web/ProductCard/ProductCardImage/primary'] img")

        print(f"Product name: {product_name.text}, Product image src: {product_image.get_attribute('src')}")
        assert product_name is not None, 'Product name not found'
        assert product_image is not None, 'Product image not found'

        assert product_image.get_attribute('src') is not None, 'Product image src not found'


