from lesson_7.Swag_Labs.Pages.Shopmain import ShopmainPage
from lesson_7.Swag_Labs.Pages.Shopcontainer import ShopContainer
import allure


@allure.epic("Saucedemo")
@allure.severity(severity_level='normal')
@allure.title("Оформление заказа в магазине")
@allure.description("Оформление заказа с необходимыми товарами с последующеим сравнением стоимости")
@allure.feature('Тест 3')
def test_shop(chrome_browsers):
    expected_total = "58.29"
    with allure.step("Переходим на страницу сервиса"):
        shopmain = ShopmainPage(chrome_browsers)
    with allure.step("Авторизуемся на странице"):    
        shopmain.registration_fields()
    with allure.step("Ищем кнопки добавления нужного товара в корзину"):  
        shopmain.buy_issue()
    with allure.step("Добавляем товар в корзину"): 
        shopmain.click_issue()
    with allure.step("Переходим в корзину"):
        shopmain.into_container()
    container = ShopContainer(chrome_browsers)
    
    with allure.step("Переходим к оформлению заказа"):
        container.checkout()
    with allure.step("Вводим данные получателя: ФИО, индекс"):
        container.info()
    with allure.step("Получаем итоговую стоимость заказа"):
        container.price()
    with allure.step("Сравниваем полученную стоимость с нашим значением и выводим результат"):
        assert expected_total in container.price()  # Проверяем, что итоговая сумма равна $58.29
        print("Итоговая сумма равна $58.29")  # Выводим сообщение в случае успешного выполнения
