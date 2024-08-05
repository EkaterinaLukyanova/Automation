from lesson_7.Data_types.Pages.MainPage import MainPage
from lesson_7.Data_types.Pages.DataFildes import DataFild
import allure

@allure.epic("Data types - registration form")
@allure.severity(severity_level='normal')
@allure.title("Заполнение формы")
@allure.description("Заполнение формы различными данными и проверка валидации данных")
@allure.feature('Тест 1')
def test_assertion(chrome_browsers):
    with allure.step("Переходим на страницу сервиса"):
        main_page = MainPage(chrome_browsers)
    with allure.step("Находим поля для заполнения"):
        main_page.find_fields()
    with allure.step("Заполняем поля"):
        main_page.filling_in_the_fields()
    with allure.step("Подтверждаем заполнение формы"):
        main_page.click_submit_button()

    with allure.step("Получаеи информацию из заполненных полей"):
        data_fild = DataFild(chrome_browsers)
        data_fild.find_fields()
        data_fild.get_class_first_name()
        data_fild.get_class_last_name()
        data_fild.get_class_address()
        data_fild.get_class_phone()
        data_fild.get_class_city()
        data_fild.get_class_country()
        data_fild.get_class_jobposition()
        data_fild.get_class_company()
        data_fild.get_class_zipcode()
    
    with allure.step("Удостоверяемся, что форма заполнена верно"):
        assert "success" in data_fild.get_class_first_name()
        assert "success" in data_fild.get_class_first_name()
        assert "success" in data_fild.get_class_last_name()
        assert "success" in data_fild.get_class_address()
        assert "success" in data_fild.get_class_phone()
        assert "success" in data_fild.get_class_city()
        assert "success" in data_fild.get_class_country()
        assert "success" in data_fild.get_class_jobposition()
        assert "success" in data_fild.get_class_company()
        assert "danger" in data_fild.get_class_zipcode()