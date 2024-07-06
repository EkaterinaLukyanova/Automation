from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ES

try:
   chrome = webdriver.Chrome()
   firefox = webdriver.Firefox()
   chrome.get("https://the-internet.herokuapp.com/entry_ad")
   firefox.get("https://the-internet.herokuapp.com/entry_ad")
   wait = WebDriverWait (chrome, 10)
   bts= WebDriverWait (firefox, 10)
   close_button = wait.until(ES.element_to_be_clickable((By.CSS_SELECTOR, "modal-footer")))
   close_button = bts.until(ES.element_to_be_clickable((By.CSS_SELECTOR, "modal-footer")))
   close_button.click()

except Exception as ex:
   print(ex)
finally:
   chrome.quit()
   firefox.quit()
