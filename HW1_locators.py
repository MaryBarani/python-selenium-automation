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

 # To find Amazon logo by ID
driver.find_element(By.ID, "authportal-main-section")

# To find Email field by XPATH
driver.find_element(By.XPATH, "//input[@id='ap_email_login' or @id='ap_email']").send_keys("mary@yahoo.com")

# To find Continue button by ID
driver.find_element(By.ID, "continue")

# To find Conditions of use link by XPATH
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(),'Conditions of Use') and contains(@href, 'Id=508088')]")
#
# To find Privacy Notice link by XPATH
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(),'Privacy Notice') and contains(@href, 'Id=468496')]")

# To find Need help link by XPATH
driver.find_element(By.XPATH, "//span[contains(text(),'Need help?')]").click()
sleep(2)

# To find Forgot your password link by ID
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# To find Other issues with Sign-In link by ID
driver.find_element(By.ID, 'ap-other-signin-issues-link')

# To find Create your Amazon account by XPATH
driver.find_element(By.ID, 'createAccountSubmit')

# To find Create your Amazon account by XPATH
driver.find_element(By.ID, 'createAccountSubmit')

sleep(5)
