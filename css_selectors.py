from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

driver_path = ChromeDriverManager().install()
Service = Service(driver_path)
driver = webdriver.Chrome(service=Service)

driver.get("https://www.amazon.com")
sleep(5)

