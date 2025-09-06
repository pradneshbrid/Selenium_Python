import os
import glob
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
import sys

sys.path.append(r"E:\Selenium\Selenium_Python\Python")
import Read_Excel  

#Variables
fruit_name = "Apple"
newValue = "990"




driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")

driver.find_element(By.ID, "downloadButton").click()
time.sleep(2)
Read_Excel.screenshot(driver)

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
list_of_files = glob.glob(os.path.join(downloads_path, "*.xlsx"))
latest_file = max(list_of_files, key=os.path.getctime)


Read_Excel.update_excel_data(latest_file, fruit_name, "price", newValue)

driver.find_element(By.ID, "fileinput").send_keys(latest_file)

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//*[contains(text(),'Updated Excel Data Successfully.')]")
))

message = driver.find_element(By.XPATH, "//*[contains(text(),'Updated Excel Data Successfully.')]").text 
assert "Updated Excel Data Successfully." in message
print("✅ File uploaded successfully and message verified!")
Read_Excel.screenshot(driver)

priceColumn = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
actual_price = driver.find_element(By.XPATH,"//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+priceColumn+"-undefined']").text
assert actual_price == newValue
Read_Excel.screenshot(driver)

# time.sleep(300)

driver.quit()
