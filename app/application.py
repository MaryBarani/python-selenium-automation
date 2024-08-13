from pages.cart_page import Cart
from pages.main_page import MainPage
from pages.base_page import Page
from pages.header import Header
from pages.search_result_page import SearchResultPage

class Application:
    def __init__(self, driver):
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultPage(driver)
        self.page = Page(driver)
        self.cart_page = Cart(driver)

