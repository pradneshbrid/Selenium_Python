from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

chromeoptions = webdriver.ChromeOptions()
chromeoptions.add_argument("--headless")    
chromeoptions.add_argument("--ignore-certificate-errors")

service_obj = Service("E://Chrome Driver//chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chromeoptions)
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

time.sleep(2)
driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot.png")
print("Screenshot taken and saved as 'screenshot.png'.")