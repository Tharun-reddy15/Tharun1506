from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# 1️⃣ Implicit Wait (applies globally)
driver.implicitly_wait(10)

try:
    # 2️⃣ Explicit Wait – wait until element is clickable
    wait = WebDriverWait(driver, 15)
    username = wait.until(
        EC.element_to_be_clickable((By.NAME, "username"))
    )
    print("✅ Username field is clickable (Explicit Wait)")

    username.send_keys("Admin")

    # 3️⃣ Fluent Wait – custom polling interval
    fluent_wait = WebDriverWait(
        driver,
        timeout=20,
        poll_frequency=2,
        ignored_exceptions=[NoSuchElementException]
    )

    password = fluent_wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    print("✅ Password field is available (Fluent Wait)")

    password.send_keys("admin123")

    print("🎯 Element is ready for interaction")

except TimeoutException:
    print("❌ Element not available within time")

finally:
    time.sleep(3)
    driver.quit()