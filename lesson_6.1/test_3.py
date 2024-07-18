from selenium.webdriver.common.by import By
from data import *

def test_shop_form(chrome_browser):
    chrome_browser.get(URL_3)

    #Ввод логина и пароля
    chrome_browser.find_element(By.ID, "user-name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome_browser.find_element(By.ID, "login-button").click()

    #Добавление товара в корзину
    add_to_cart_buttons = [
        (By.ID, "add-to-cart-sauce-labs-backpack"),
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        (By.ID, "add-to-cart-sauce-labs-onesie")
    ]
    for button in add_to_cart_buttons:
        chrome_browser.find_element(*button).click()

    #Переход к корзине и оформление товара
    chrome_browser.find_element(By.ID, "shopping_cart_container").click()
    chrome_browser.find_element(By.ID, "checkout").click()

    #Ввод данных о покупателе
    chrome_browser.find_element(By.ID, "first-name").send_keys("Kate")
    chrome_browser.find_element(By.ID, "last-name").send_keys("Len")
    chrome_browser.find_element(By.ID, "postal-code").send_keys("123456")
    chrome_browser.find_element(By.ID, "continue").click()

    #Получение и вывод общей стоимости заказа
    total_price = chrome_browser.find_element(By.CLASS_NAME, 'summary_total_label')
    total = total_price.text.strip().replace("Total: $", "")
    expected_total = "58.29"
    assert total == expected_total
 