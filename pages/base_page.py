from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Page:
    def __init__(self, driver):
        self.original_window = None
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, *locator, text):
        self.wait_until_element_appearance(locator)
        self.driver.find_element(*locator).send_keys(text)

    def get_current_window(self):
        original_window = self.driver.current_window_handle
        return original_window

    def switch_to_new_window(self):
        self.wait.until(EC.new_window_is_opened)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    def switch_to_window_by_ID(self, window_Id):
        self.driver.switch_to.window(window_Id)

    def close_window(self):
        self.driver.close()

    def open_url(self, url):
        self.driver.get(url)

    def wait_until_clickable(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by locator {locator} is not clickable")

    def wait_and_click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element by locator {locator} is not clickable"
        ).click()
        
    def wait_until_element_appearance(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element by locator {locator} is not visible"
        )

    def wait_until_element_disappearance(self, locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f"Element by locator {locator} is not invisible"
        )

    def verify_text(self, locator, expected_text):
        self.wait_until_element_appearance(locator)
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f"{expected_text} is not shown"

    def verify_partial_text(self, locator, expected_text):
        self.wait_until_element_appearance(locator)
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f"{expected_text} is not in {actual_text}"

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"{expected_url} does not match  {actual_url}"


    def verify_partial_url(self, search_word):
        actual_url = self.driver.current_url
        assert search_word in actual_url, f"{search_word} is not in {actual_url}"


