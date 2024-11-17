import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

service_obj=Service("C:\\DRIVERS\\Chrome Driver V128\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
###
driver.find_element(By.XPATH,"/html/body/app-root/form-comp/div/form/div[1]/input").send_keys("Pradnesh")
driver.find_element(By.NAME, "email").send_keys("pradneshbrid@gmil.com")
driver.find_element(By.XPATH, "//*[@id='exampleInputPassword1']").send_keys("PASSWORD123")
driver.find_element(By.XPATH, "//*[@id='exampleCheck1']").click()
scrollto = driver.find_element(By.XPATH,"//*[@class='btn btn-success']")
select = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
actions = ActionChains(driver)
actions.scroll_to_element(scrollto).perform()
select.select_by_visible_text('Male')

time.sleep(5)



###
# print (driver.title)
# print(driver.current_url)
# driver.quit()