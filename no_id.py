from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
Chrome_driver = webdriver.Chrome()

Chrome_driver.maximize_window()

Chrome_driver.get("http://uitestingplayground.com/dynamicid")

button = WebDriverWait(Chrome_driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Button with Dynamic ID']"))
)
button.click()

for _ in range(3):
    button = WebDriverWait(Chrome_driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Button with Dynamic ID']"))
)
button.click()

Firefox_driver = webdriver.Firefox()
Firefox_driver.maximize_window()

Firefox_driver.get("http://uitestingplayground.com/dynamicid")

button = WebDriverWait(Firefox_driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Button with Dynamic ID']"))
)
button.click()

for _ in range(3):
    button = WebDriverWait(Firefox_driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[text()='Button with Dynamic ID']"))
)
button.click()

Firefox_driver.quit()