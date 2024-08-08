from lesson_7.Calculator.Pages.calcpage import CalcMain
import allure

@allure.epic("Calculator")
@allure.severity(severity_level='normal')
@allure.title("Работа калькулятора")
@allure.description("Поиск полей, ввод данных и вывод результата вычисления")
@allure.feature('Тест 2')
def test_calculator_assert(chrome_browsers):
    with allure.step("Переходим на страницу сервиса"):
        calcmain = CalcMain(chrome_browsers)
    with allure.step("Вводим время ожидания"):    
        calcmain.insert_time()
    with allure.step("Нажимаем на кнопки калькулятора"):
        calcmain.clicking_buttons()
    with allure.step("Ожидаем и выводим результат"):
        calcmain.wait_button_gettext()
    with allure.step("Сравниваем полученный результат с нашим значением"):
        assert "15" in calcmain.wait_button_gettext()
