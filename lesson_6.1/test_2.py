import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit

    def test_slow_calculator(browser):
        browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        delay_input = browser.find_element_by_css_selector("#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        buttons = ['seven', 'plus', 'eight', 'equal']
        for button in buttons:
            browser.find_element_by_id(button).click()
            time.sleep(45)
            result = browser.find_element_by_id('result')
            assert result.text == "15"

            


