from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

Chrome_driver = webdriver.Chrome()

Chrome_driver.maximize_window()

Chrome_driver.get("http://the-internet.herokuapp.com/inputs")

search_input = Chrome_driver.find_element(By.XPATH, "//input[@type='number']")
search_input.send_keys("1000",Keys.RETURN)

search_input.clear()
search_input.send_keys("999",Keys.RETURN)

Chrome_driver.quit()

Firefox_driver = webdriver.Firefox()
Firefox_driver.maximize_window()

Firefox_driver.get("http://the-internet.herokuapp.com/inputs")

input = Firefox_driver.find_element(By.XPATH, "//input[@type='number']")
input.send_keys("1000",Keys.RETURN)

input.clear()
input.send_keys("999",Keys.RETURN)

Firefox_driver.quit()