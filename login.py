from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

Chrome_driver = webdriver.Chrome()

Chrome_driver.maximize_window()

Chrome_driver.get("http://the-internet.herokuapp.com/login")

username = Chrome_driver.find_element(By.XPATH, "//input[@type='text']")
username.send_keys("tomsmith")

password = Chrome_driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys("SuperSecretPassword!")

login_button = Chrome_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()
Chrome_driver.quit()

Firefox_driver = webdriver.Firefox()
Firefox_driver.maximize_window()
Firefox_driver.get("http://the-internet.herokuapp.com/login")

username_f = Firefox_driver.find_element(By.XPATH, "//input[@type='text']")
username_f.send_keys("tomsmith")
password_f = Firefox_driver.find_element(By.XPATH, "//input[@type='password']")
password_f.send_keys("SuperSecretPassword!")


login_buttonf = Firefox_driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_buttonf.click()

Firefox_driver.quit()