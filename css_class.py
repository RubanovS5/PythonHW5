
from selenium import webdriver
from selenium.webdriver.common.by import By
Chrome_driver = webdriver.Chrome()

Chrome_driver.maximize_window()

Chrome_driver.get("http://uitestingplayground.com/classattr")

blue_button = Chrome_driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
)

blue_button.click()

for _ in range(3):
    blue_button = Chrome_driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]"
    )
blue_button.click()

