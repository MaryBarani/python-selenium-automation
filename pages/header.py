from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
class Header(Page):

    SEARCH_FIELD = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchInput']")
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR,  "div[data-test='@web/CartIcon'] use[href*='Cart']")

    def search(self,product_name ):
        self.input_text(*self.SEARCH_FIELD, text= product_name)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart(self):
        self.click(*self.CART_ICON)
