from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from time import sleep

driver_path = ChromeDriverManager().install()
Service = Service(driver_path)
driver = webdriver.Chrome(service=Service)

# open the page
driver.get("https://www.target.com/ ")
sleep(5)

# search for sneakers
driver.find_element(By.ID, "search").send_keys("sneakers")
sleep(1)

driver.find_element(By.XPATH, "//button[@data-test= '@web/Search/SearchButton']").click()
sleep(5)

# Verify the result page
expected_text = 'sneakers'
actual_text = driver.find_element(By.XPATH, "//div[@data-test= 'resultsHeading']").text

assert expected_text in actual_text , f"{expected_text} != {actual_text}"

print("test case passed")
driver.quit()