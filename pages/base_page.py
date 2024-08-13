class Page:
    def __init__(self, driver):
        self.driver = driver

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, *locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def open_url(self, url):
        self.driver.get(url)

