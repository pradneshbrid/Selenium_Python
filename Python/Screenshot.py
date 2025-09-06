import time
import os

folder = "Screenshots"
os.makedirs(folder, exist_ok=True)

def screenshot(driver):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(folder, f"screenshot_{timestamp}.png")
    driver.save_screenshot(filename)