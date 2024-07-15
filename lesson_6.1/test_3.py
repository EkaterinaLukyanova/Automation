import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_purchase(browser):
    browser.get("https://www.saucedemo.com/")
    username_input = browser.find_element(By.CSS_SELECTOR, "#user-name")
    password_input = browser.find_element(By.CSS_SELECTOR, "#password")
    login_button = browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]')

    username_input.send_keys("standart_user")
    password_input.send_keys("secret_sause")

    login_button.click()

    items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
    for item in items_to_add:
        add_to_cart_button = browser.find_element_by_xpath(f"//div[text()='{item}']/following-sibling::button")
        add_to_cart_button.click()

        cart_icon = browser.find_element_by_css_selector(".shopping_cart_link")
        cart_icon.click()

        checkout_button = browser.find_element_by_css_selector(".checkout-button")
        checkout_button.click()

        first_name_input = browser.find_element_by_id('first-name')
        last_name_input = browser.find_element_by_id('last-name')
        postal_code_input = browser.find_element_by_id('postal-code')

        first_name_input.sendkeys('Kate')
        last_name_input.sendkeys('Len')
        postal_code_input.sendkeys('12345')

        continue_button = browser.find_element_by_class_name('btn_primary.cart_checkout_link')
        continue_button.click()

        total_cost = browser.find_element_by_class_name('.summary_total_label').get.text()
        assert total_cost == "$58,29"

