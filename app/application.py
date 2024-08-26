from pages.cart_page import Cart
from pages.main_page import MainPage
from pages.base_page import Page
from pages.header import Header
from pages.help_page import HelpPage
from pages.search_result_page import SearchResultPage
from pages.sign_in_page import SignInPage
from pages.TC_page import TCPage

class Application:
    def __init__(self, driver):
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_result_page = SearchResultPage(driver)
        self.page = Page(driver)
        self.cart_page = Cart(driver)
        self.sign_in_page = SignInPage(driver)
        self.TCPage = TCPage(driver)
        self.help_page = HelpPage(driver)
