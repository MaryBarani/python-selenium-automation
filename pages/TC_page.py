from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class TCPage(Page):
    TC_URL = "terms-conditions"
    def verify_Tc_is_Open(self):
        self.verify_partial_url(self.TC_URL)
