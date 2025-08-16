
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions

# Service object for ChromeDriver
service_obj = Service("E://Chrome Driver//chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Implicit wait
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.XPATH, '//a[@class="blinkingText"]').click()

windowhandels = driver.window_handles
driver.switch_to.window(windowhandels[1])   

# Wait for the new window to load
wait = WebDriverWait(driver, 10)        
Email_ID = wait.until(EC.presence_of_element_located((By.XPATH, '//p[normalize-space(text())="Please email us at"]//strong/a')))
Email_ID = Email_ID.text
print("Email ID:", Email_ID)

#Switch back to the original window
driver.switch_to.window(windowhandels[0])   
driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(Email_ID)
driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("12345")
driver.find_element(By.XPATH, '//input[@id="signInBtn"]').click()   
# Detch Incorrect Credentials Error
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, '(//form[@id="login-form"]/div)[1]')))
error_message = driver.find_element(By.XPATH, '(//form[@id="login-form"]/div)[1]').text
print("Error Message:", error_message)