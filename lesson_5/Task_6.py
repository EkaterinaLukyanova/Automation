from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()
chrome.get("https://the-internet.herokuapp.com/login")
firefox.get("https://the-internet.herokuapp.com/login")
input_name = chrome.find_element(By.ID, "username").send_keys("tomsmith")
input_name = firefox.find_element(By.ID, "username").send_keys("tomsmith")
input_pass = chrome.find_element(
    By.ID, "password").send_keys("SuperSecretPassword!")
button = chrome.find_element(By.TAG_NAME, "button").click()
bts = firefox.find_element(By.TAG_NAME, "button").click()
chrome.quit()
firefox.quit()
