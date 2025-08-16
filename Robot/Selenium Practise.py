import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Service object for ChromeDriver
service_obj = Service("E://Chrome Driver//chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Implicit wait
driver.implicitly_wait(5)

# Lists to hold product names
selected_products = []
cart_products = []

# Open the website
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

# Search for products
search_box = driver.find_element(By.CSS_SELECTOR, "input.search-keyword")
search_box.send_keys("ber")
time.sleep(4)  # Wait for products to load

# Count products and assert
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
print(f"Count: {len(products)}")
assert len(products) > 0, "No products found!"

# Add products to cart
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in buttons:
    product_name = button.find_element(By.XPATH, "parent::div/parent::div/h4").text
    selected_products.append(product_name)
    button.click()

print("Selected Products:", selected_products)

# Proceed to checkout
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Wait for promo code field to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))

# Verify products in the cart
veggies = driver.find_elements(By.CSS_SELECTOR, "p.product-name")
for veg in veggies:
    cart_products.append(veg.text)

print("Cart Products:", cart_products)
assert selected_products == cart_products, "Products in cart do not match selected products!"

# Get initial amount
amount1 = float(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
print(f"amount1:", amount1)

# Apply promo code
promo_code_box = driver.find_element(By.CLASS_NAME, "promoCode")
promo_code_box.send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Wait for promo info
promo_info = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print("Promo Info:", promo_info.text)

# Get discounted amount
amount2 = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print("Amount After Discount:", amount2)

# Validate discount
assert amount1 > amount2, "Discount not applied correctly!"

# Validate total price
veggie_prices = driver.find_elements(By.XPATH, "//tr/td[5]/p")
calculated_sum = sum([float(price.text) for price in veggie_prices])
print("Calculated Total:", calculated_sum)
# time.sleep(1000)
assert calculated_sum >= amount2, "Sum of item prices does not match discounted total!"

# Close the browser
driver.quit()