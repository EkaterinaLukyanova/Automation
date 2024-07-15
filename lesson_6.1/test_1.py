from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import *
from time import sleep

def test_data_types_form(chrome_browser: WebDriver):
    chrome_browser.get(URL_1)
    chrome_browser.find_element(By.NAME, "first-name").send_keys(first_name)
    chrome_browser.find_element(By.NAME, "last-name").send_keys(last_name)
    chrome_browser.find_element(By.NAME, "address").send_keys(address)
    chrome_browser.find_element(By.NAME, "email").send_keys(email)
    chrome_browser.find_element(By.NAME, "phone").send_keys(phone)
    chrome_browser.find_element(By.NAME, "zip_code").send_keys(zip_code)
    chrome_browser.find_element(By.NAME, "city").send_keys(city)
    chrome_browser.find_element(By.NAME, "country").send_keys(country)
    chrome_browser.find_element(By.NAME, "job_position").send_keys(job_position)
    chrome_browser.find_element(By.NAME, "company").send_keys(company)
    WebDriverWait(chrome_browser, 40, 0.1).until(ES.element_to_be_clickable((By.TAG_NAME, "button")))
    sleep(2)
    assert "success" in chrome_browser.find_element(By.ID, "first_name").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "last_name").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "address").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "email").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "phone").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "city").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "country").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "job_position").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "company").get_attribute("class")
    assert "danger" in chrome_browser.find_element(By.ID, "zip_code").get_attribute("class")



