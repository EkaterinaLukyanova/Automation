from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from data import URL_2


def test_calculator_from(chrome_browser):
    chrome_browser.get(URL_2)
    delay_input = chrome_browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45)
    chrome_browser.find_element(By.XPATH, "//span[text() = '7']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '+']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '8']").click()
    chrome_browser.find_element(By.XPATH, "//span[text() = '=']").click()

    WebDriverWait(chrome_browser, 47).until(
        ES.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text

    assert result_text == "15"
