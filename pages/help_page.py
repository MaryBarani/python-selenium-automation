from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class HelpPage(Page):

   HELP_RETURN_TITLE = (By.XPATH, "//h1[contains(text(), '{text}')]")
   MENU = (By.CSS_SELECTOR, "select[id*= 'ViewHelpTopics']")
   def _get_locator(self, text):
       return [self.HELP_RETURN_TITLE[0], self.HELP_RETURN_TITLE[1].replace("{text}", text)]

   def verify_page_title(self, expected_title):
      self.verify_partial_text(self._get_locator(expected_title), expected_title)

   def select_drop_down_option(self, option):
      drop_down_menu = self.driver.find_element(*self.MENU)
      select = Select(drop_down_menu)
      select.select_by_value(option)
