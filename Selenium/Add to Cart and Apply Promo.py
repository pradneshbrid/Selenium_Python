import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def parse_amount(s: str) -> float:
    if s is None:
        raise ValueError("Amount string is None")
    x = s.strip()

    for ch in ['₹', '$', '€', ',', '£']:
        x = x.replace(ch, '')
    # Some sites render non-breaking spaces so handelling this as well
    x = x.replace('\u00A0', '').strip()
    # If it’s something like '88.' or '.50', float will still handle it
    return float(x)

driver = webdriver.Chrome()
driver.implicitly_wait(5)

picked_names = []
cart_names = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, "input.search-keyword").send_keys("ber")

time.sleep(4)

cards = driver.find_elements(By.XPATH, "//div[@class='products']/div")
assert len(cards) == 3, f"Expected 3 products, got {len(cards)}"

buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
for button in buttons:
 
    name = button.find_element(By.XPATH, "parent::div/parent::div/h4").text
    picked_names.append(name)
    button.click()

print("Picked:", picked_names)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoCode")))


for v in driver.find_elements(By.XPATH, "//p[@class='product-name']"):
    cart_names.append(v.text)

print("In cart:", cart_names)
assert picked_names == cart_names, "Picked items do not match cart items"


amount1_text = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
amount1 = parse_amount(amount1_text)


promo = driver.find_element(By.CLASS_NAME, "promoCode")
promo.clear()
promo.send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()


wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.promoInfo"), "applied"))
print(driver.find_element(By.CSS_SELECTOR, "span.promoInfo").text)

amount2_text = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
amount2 = parse_amount(amount2_text)


assert amount1 > amount2, f"Expected discount. Before={amount1}, After={amount2}"


line_totals = driver.find_elements(By.XPATH, "//tr/td[5]/p")
sum_total = 0.0
for v in line_totals:
    sum_total += parse_amount(v.text)

print("Line total sum:", sum_total)
print("Amount before discount:", amount1)
print("Amount after discount:", amount2)

# When comparing floats, prefer a small tolerance (e.g., 1e-6) to avoid issues from rendering/rounding.
assert abs(sum_total - amount1) < 1e-6 or abs(sum_total - amount2) < 1e-6, \
       f"Sum of items {sum_total} doesn't match totals: before={amount1}, after={amount2}"

driver.quit()
