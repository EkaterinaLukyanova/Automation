from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
chrome.get("https://the-internet.herokuapp.com/inputs")
firefox.get("https://the-internet.herokuapp.com/inputs")
# Находим поле ввода по id и вводим текст "1000"
input_field = chrome.find_element(By.TAG_NAME, "input")
field = firefox.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")
field.send_keys("1000")
# Очищаем поле ввода
input_field.clear()
field.clear()
# Вводим новый текст "999"
input_field.send_keys("999")
field.send_keys("999")
# Закрываем браузер
chrome.quit()
firefox.quit()
