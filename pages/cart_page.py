from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class Cart(Page):

    EMPTY_TITLE = (By.CSS_SELECTOR, "h1.sc-fe064f5c-0.dtCtuk")
    ADD_TEXT = (By.XPATH,"//div[@class= 'h-margin-b-tight h-text-grayDark ']//span[@class = 'sc-93ec7147-3 fUVkzh']")

    def verify_cart_is_empty(self):
        expected_text = "Your cart is empty"
        self.driver.wait = WebDriverWait(self.driver, 5)
        actual_text_shown = self.driver.wait.until(EC.text_to_be_present_in_element(self.EMPTY_TITLE, expected_text))
        assert actual_text_shown, f"{expected_text} is not shown"
        print("test case verify_empty_Cart passed")


    def verify_item_is_added_to_cart(self):
        expected_text = "total"
        self.driver.wait = WebDriverWait(self.driver, 10)
        actual_text_shown = self.driver.wait.until(EC.text_to_be_present_in_element(self.ADD_TEXT,expected_text))
        # actual_text= context.driver.find_element((By.XPATH, "//span[@data-test='cart-summary-subtotal']")).text
        assert actual_text_shown, f"{expected_text} not in shown"
        print("item is added to the card")