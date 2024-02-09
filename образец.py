from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("https://www.labirint.ru/")

search_locator = "#search-field"
#найти книги по слову Python
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)

search_input.send_keys("Python",Keys.RETURN)
#search_input.send_keys (Keys.RETURN)
#cобрать все карточки товаров 
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))

#вывксти в консоль инфо: название + автор +  цена

for book in books:
    author = book.find_element(By.CSS_SELECTOR,"div.product-card__author").text
    title = book.find_element(By.CSS_SELECTOR,"a.product-card__name").text
    price = book.find_element(By.CSS_SELECTOR,"div.product-card__price-current").text

    #try:
    #author = book.find_element(By.CSS_SELECTOR,"div.product-card__author").text
    #except:
        #author = "Автора нету"

    print(author + "/t" + title + "/t" + price)





#sleep(5)