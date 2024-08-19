from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Cart(Page):
    EMPTY_TITLE = (By.CSS_SELECTOR, "h1.sc-fe064f5c-0.dtCtuk")
    ADD_TEXT = (By.XPATH, "//div[@class= 'h-margin-b-tight h-text-grayDark ']//span[@class = 'sc-93ec7147-3 fUVkzh']")

    def verify_cart_is_empty(self):
        self.verify_text(self.EMPTY_TITLE, "Your cart is empty")

    def verify_item_is_added_to_cart(self):
        expected_text = "total"
        self.wait_until_element_appearance(self.ADD_TEXT)
        self.verify_partial_text(self.ADD_TEXT, expected_text)
        print("item is added to the card")
