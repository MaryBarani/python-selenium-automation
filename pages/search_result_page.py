from selenium.webdriver.common.action_chains import  ActionChains
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultPage(Page):
    SEARCH_RESULT_TXT = (By.XPATH, "//div[@data-test='resultsHeading']")
    PRODUCT = (By.CSS_SELECTOR, "div[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div[data-test='@web/site-top-of-funnel/ProductCardWrapper'] a[data-test= 'product-title']")
    PRODUCT_IMAGE = (By.CSS_SELECTOR,"picture[data-test='@web/ProductCard/ProductCardImage/primary'] img")
    ELEMENT = (By.CSS_SELECTOR, "button[data-test*='chooseOptionsButton'][id*=addToCartButton]")
    ADD_TO_CART = (By.CSS_SELECTOR, "button[data-test='shippingButton'][id*='addToCartButtonOrText']")
    CART_ELEMENT = (By.XPATH, "//a[contains(text(), 'View cart')]")
    FAV_BTN = (By.CSS_SELECTOR, "button[data-test ='FavoritesButton']")
    TOOL_TIP = (By.XPATH, "//*[text() ='Click to sign in and save']")

    def hover_fav_icon(self):
        self.wait_until_element_appearance(self.FAV_BTN)
        fav_icon = self.find_element(*self.FAV_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(fav_icon)
        # actions.click()
        actions.perform()



    def verify_fav_tooltip(self):
        self.wait_until_element_appearance(self.TOOL_TIP)
        tool_tip = self.find_element(*self.TOOL_TIP)
        actions = ActionChains(self.driver)
        actions.move_to_element(tool_tip)
        actions.perform()



    def verify_search_result(self, search_word):
        self.verify_partial_text(self.SEARCH_RESULT_TXT, search_word)

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
        elements = self.driver.find_elements(*self.ELEMENT)
        self.wait_and_click(elements[0])
        self.wait_and_click(self.ADD_TO_CART)
        self.wait_and_click(self.CART_ELEMENT)
