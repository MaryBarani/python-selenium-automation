from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from time import sleep

driver_path = ChromeDriverManager().install()
Service = Service(driver_path)
driver = webdriver.Chrome(service=Service)


# Test Case: Users can navigate to SignIn page

# Open https: // www.target.com /
driver.get("https://www.target.com/")
sleep(10)

# Click SignIn button
driver.find_element(By.XPATH, "//span[contains(text(), 'Sign in')]").click()
sleep(5)

# Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[contains(text(), 'Sign in')]").click()
sleep(5)

# Verify SignIn page opened
# “Sign into your Target account” text is shown
Expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//h1//span" ).text
assert Expected_text in actual_text , f"The Expected test {Expected_text} did not match Actual {actual_text}"

# SignIn button is shown
driver.find_element(By.ID, "login"), f"No Login Found"

sleep(3)

print("Test case passed")
driver.quit()

