from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")
my_button = driver.find_element(
    "id", "newButtonName").send_keys("Skypro")
confirm_my_button = driver.find_element(
    "id", "updatingButton").click()
new_my_button = driver.find_element("id", "updatingButton").text
print(new_my_button)

driver.quit()

