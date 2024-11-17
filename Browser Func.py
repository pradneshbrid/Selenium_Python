from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Edge WebDriver setup
service_obj = Service("C:\\DRIVERS\\Chrome Driver V131\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Implicit wait
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")  # Open URL

print(f"Title: ",driver.title)
print(f"URL: ",driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.quit()  # Properly close the browser
