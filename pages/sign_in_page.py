from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SignInPage(Page):
    SIGN_IN_TXT = (By.CSS_SELECTOR, "h1.sc-fe064f5c-0.sc-315b8ab9-2.WObnm.gClYfs")
    EMAIL_TXT = (By.CSS_SELECTOR, "input#username")
    PASSWORD_TXT = (By.CSS_SELECTOR, "input#password")
    SIGN_IN_BTN = (By.ID, "login")
    SIGN_IN_FORM = (By.CSS_SELECTOR, "form")

    def verify_sign_in_text(self, expected_text):
        self.verify_text(self.SIGN_IN_TXT, expected_text)

    def input_email_and_password(self, email, password):
        self.input_text(*self.EMAIL_TXT, text=email)
        self.input_text(*self.PASSWORD_TXT, text=password)

    def click_sign_in_with_password(self):
        self.wait_and_click(self.SIGN_IN_BTN)

    def verify_user_is_logged_in(self):
        self.wait_until_element_disappearance(self.SIGN_IN_FORM)