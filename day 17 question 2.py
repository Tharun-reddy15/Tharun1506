from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# ---------------------------------
# 1. Trigger JavaScript Alert
# ---------------------------------
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(1)

alert = driver.switch_to.alert
print("Alert Message:", alert.text)

# 2. Accept alert
alert.accept()

# Verify result
print(driver.find_element(By.ID, "result").text)

# ---------------------------------
# 3. Dismiss Confirmation Pop-up
# ---------------------------------
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(1)

confirm = driver.switch_to.alert
print("Confirm Message:", confirm.text)
confirm.dismiss()

# Verify result
print(driver.find_element(By.ID, "result").text)

# ---------------------------------
# 4. Prompt Alert – Enter Text
# ---------------------------------
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(1)

prompt = driver.switch_to.alert
print("Prompt Message:", prompt.text)
prompt.send_keys("Selenium Test")
prompt.accept()

# ---------------------------------
# 5. Verify Result on Page
# ---------------------------------
result = driver.find_element(By.ID, "result").text

if "Selenium Test" in result:
    print("✅ Test Passed – Prompt text verified")
else:
    print("❌ Test Failed")

time.sleep(2)
driver.quit()

