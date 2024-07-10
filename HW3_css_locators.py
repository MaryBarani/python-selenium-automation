from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

driver_path = ChromeDriverManager().install()
Service = Service(driver_path)
driver = webdriver.Chrome(service=Service)
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&/')

sleep(10)

# To find Amazon logo by Css_Selector
driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")

# To find Your name field by Css_Selector
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")

# To find Email field by Css_Selector
driver.find_element(By.CSS_SELECTOR, "input#ap_email")

# To find Password field by Css_Selector
driver.find_element(By.CSS_SELECTOR, "input#ap_password")

# To find Re-enter password field by Css_Selector
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
# or
driver.find_element(By.CSS_SELECTOR, "input[name=passwordCheck]")

# To find Create your Amazon account by Css_Selector
driver.find_element(By.CSS_SELECTOR, "#continue")
# or
driver.find_element(By.CSS_SELECTOR, "input.a-button-input")


# To find Conditions of use link by Css_Selector
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href *='nodeId=508088']")
#
# To find Privacy Notice link by Css_Selector
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href *='nodeId=468496']")

# To find Other issues with Sign-In link by Css_Selector
driver.find_element(By.CSS_SELECTOR,  ".a-link-emphasis")


