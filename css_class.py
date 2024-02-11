
from selenium import webdriver
from selenium.webdriver.common.by import By

Chrome_driver = webdriver.Chrome()
Chrome_driver.maximize_window()
Chrome_driver.get("http://uitestingplayground.com/classattr")

blue_button = Chrome_driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary') and contains(@class, 'btn-test')]")
blue_button.click()

alert_obj = Chrome_driver.switch_to.alert 
alert_obj.accept()

for _ in range(3):
    blue_button.click()
    alert_obj.accept()

Chrome_driver.quit()


Firefox_driver = webdriver.Firefox()
Firefox_driver.maximize_window()
Firefox_driver.get("http://uitestingplayground.com/classattr")

blue_button_f = Firefox_driver.find_element(By.XPATH, "//button[contains(@class, 'btn-primary') and contains(@class, 'btn-test')]")
blue_button_f.click()

alert_obj = Firefox_driver.switch_to.alert 
alert_obj.accept()

for _ in range(3):
    blue_button_f.click()
    alert_obj.accept()

Firefox_driver.quit()
