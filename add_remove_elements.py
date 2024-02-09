from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
Chrome_driver = webdriver.Chrome()

Chrome_driver.maximize_window()

Chrome_driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    button = WebDriverWait(Chrome_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Add Element']"))
    )
    button.click()

delete = Chrome_driver.find_elements(By.XPATH, "//button[text()='Delete']")

print("Размер списка кнопок 'Delete' в Chrome:", len(delete))
Chrome_driver.quit()

Firefox_driver = webdriver.Firefox()
Firefox_driver.maximize_window()

Firefox_driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    button = WebDriverWait(Firefox_driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Add Element']"))
    )
    button.click()

delete = Firefox_driver.find_elements(By.XPATH, "//button[text()='Delete']")

print("Размер списка кнопок 'Delete' в Firefox:", len(delete))
Firefox_driver.quit()