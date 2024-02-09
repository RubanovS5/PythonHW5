from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Chrome_driver = webdriver.Chrome()
Chrome_driver.maximize_window()

Chrome_driver.get("http://the-internet.herokuapp.com/entry_ad")

button = WebDriverWait(Chrome_driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal-footer"))
)
button.click()


Firefox_driver = webdriver.Firefox()
Firefox_driver.maximize_window()
Firefox_driver.get("http://the-internet.herokuapp.com/entry_ad")

button_f = WebDriverWait(Firefox_driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modal-footer"))
)
button_f.click()

Firefox_driver.quit()

