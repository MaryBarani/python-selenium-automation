from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SearchResultPage(Page):
    SEARCH_RESULT_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    PRODUCT = (By.CSS_SELECTOR, "div[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div[data-test='@web/site-top-of-funnel/ProductCardWrapper'] a[data-test= 'product-title']")
    PRODUCT_IMAGE = (By.CSS_SELECTOR,"picture[data-test='@web/ProductCard/ProductCardImage/primary'] img")
    ELEMENT = (By.CSS_SELECTOR, "button[data-test*='chooseOptionsButton'][id*=addToCartButton]")
    ADD_TO_CART = (By.CSS_SELECTOR, "button[data-test='shippingButton'][id*='addToCartButtonOrText']")

    def verify_text(self, search_word ):
        actual_text = self.driver.find_element(*self.SEARCH_RESULT_TXT).text
        assert search_word in actual_text, f'Expected {search_word} not in results_heading'

    def verify_url(self):
        actual_url = self.driver.current_url
        assert "coffee" in actual_url, f'Expected coffee in {actual_url}'


    def verify_products_names_images(self):
        products = self.driver.find_elements(*self.PRODUCT)
        for product in products[:4]:
            product_name = product.find_element(*self.PRODUCT_TITLE)
            product_image = product.find_element(*self.PRODUCT_IMAGE)

            print(f"Product name: {product_name.text}, Product image src: {product_image.get_attribute('src')}")
            assert product_name, 'Product name not found'
            assert product_image, 'Product image not found'

            assert product_image.get_attribute('src') is not None, 'Product image src not found'


    def click_add_to_cart_btn(self):
        self.driver.wait = WebDriverWait(self.driver, 5)
        elements = self.driver.find_elements(*self.ELEMENT)
        first_element = self.driver.wait.until(EC.element_to_be_clickable(elements[0]))
        sleep(5)  # I have to put this sleep here because otherwise I get the error "The element is not clickable at point X. Other element would receive the click"
        first_element.click()

        add_to_cart_button = self.driver.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART))
        add_to_cart_button.click()
        view_cart_element = self.driver.find_element(By.XPATH, "//a[contains(text(), 'View cart')]")
        self.driver.wait.until(EC.element_to_be_clickable(view_cart_element))
        view_cart_element.click()