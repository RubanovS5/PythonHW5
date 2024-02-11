from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_driver = webdriver.Chrome()

Chrome_driver.maximize_window()

Chrome_driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

button_add = Chrome_driver.find_element(By.XPATH, "//button[text()='Add Element']")

for _ in range(5):
    button_add.click()

delete = Chrome_driver.find_elements(By.XPATH, "//button[text()='Delete']")
print("Размер списка кнопок 'Delete' в Chrome:", len(delete))

Chrome_driver.quit()

Firefox_driver = webdriver.Firefox()
Firefox_driver.maximize_window()

Firefox_driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

button = Firefox_driver.find_element(By.XPATH, "//button[text()='Add Element']")

for _ in range(5):
    button.click()

delete = Firefox_driver.find_elements(By.XPATH, "//button[text()='Delete']")

print("Размер списка кнопок 'Delete' в Firefox:", len(delete))

Firefox_driver.quit()