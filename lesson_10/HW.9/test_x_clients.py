import pytest
import allure
from Employee import Employer
from DataBase import DataBase

api = Employer("https://x-clients-be.onrender.com/")
db = DataBase(
    "postgresql+psycopg2://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")
# Расшивровка подключения к БД
# - Имя пользователя: x_clients_db_3fmx_user
# - Пароль: mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq
# - Хост: dpg-cour99g21fiec73bsgvug-a.oregon-postgres.render.com
# - База данных: x_clients_db_3fmx

@allure.epic("X-clients")
@allure.severity(severity_level='normal')
@allure.title("Список сотрудников")
@allure.description("Получаем список сотрудников из БД и АПИ, после чего сравниваем их")
@allure.feature('Test_1')
def test_get_list_of_employers():
    with allure.step ("БД - Создание компании"):
        db.create_company_db('Moscow2024', 'cool_company')
    with allure.step ("БД - Получаем ID последней созданной компании"):
        max_id = db.get_max_id()
    with allure.step("БД - добавляем сотрудника в компанию"):
        db.db_create_employer(max_id, "Ivan", "Larkin", 89779779797)
    with allure.step("БД - Получаем список сотрудников из последней созданной компании"):
        db_employer_list = db.db_get_list_employer(max_id)
    with allure.step("API - Получаем список сотрудников из последней созданной компании"):
        api_employer_list = api.get_list_employers(max_id)
    with allure.step("Сравниваем списки сотрудников полученных ид БД и через API"):
        assert len(db_employer_list) == len(api_employer_list)
    with allure.step("БД - Удаляем последнюю созданную компанию"):
        db.delete_company(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Добавление сотрудников")
@allure.description("Добавляем сотрудника в БД и сравниваем с АПИ имя, статус и фамилию")
@allure.feature('Test_2')
def test_add_new_employer():
    db.crdb.create_company_db('MOSCOW2025', 'beautiful')
    max_id = db.get_max_id()
    db.db_create_employer(max_id, "Ivan", "Ivanov", 89779660001)
    response = api.get_list_employers(max_id)
    employer_id = response[0] ["id"]
    """Сравниваем ID компании"""
    assert response[0]["companyId"] == max_id
    """Сравниваем имя сотрудника с заданным"""
    assert response[0]["firstName"] == "Ivan"
    """Удостоверяемся что статус сотрудника - True"""
    assert response[0]["isActive"] == True
    """Сравниваем фамилию сотрудника с заданной"""
    assert response[0]["lastName"] == "Ivanov"
    """БД - удаляем созданого сотрудника"""
    db.db_delete_employer(employer_id)
    """БД - удаляем последнюю созданную компанию"""
    db.delete_company(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level='trivial')
@allure.title("Получение информации о сотруднике по ID")
@allure.description("Сравниваем инф о сотруднике полученную по API с инф указанной при создании сотрудника в БД")
@allure.feature ('Test_3')
def test_get_employer_by_id():
    db.create_company_db('Employer get id company', 'new')
    max_id = db.get_max_id()
    db.db_create_employer(max_id, "Ivan", "Ivanov", 89779660001)
    employer_id = db.db_get_employer_id(max_id)
    """Сравниваем инф о сотруднике полученную по
    API с инф указанной при создании сотрудника в БД"""
    get_info = api.get_employer_by_id(employer_id)
    assert get_info["firstName"] == "Ivan"
    assert get_info["lastName"] == "Ivanov"
    """БД - удаляем созданного сотрудника"""
    db.db_delete_employer(employer_id)
    """БД - удаляем последнюю созданную компанию"""
    db.delete_company(max_id)

@allure.epic("X-clients")
@allure.severity(severity_level='normal')
@allure.title("Обновление информации о сотруднике")
@allure.description("Сравниваем инф о сотруднике полученную по API с измененной инф в БД")
@allure.feature('Test_4')
def test_update_user_info():
    db.create_company_db('MOSCOW24', 'moscow')
    max_id = db.get_max_id()
    db.db_create_employer(max_id, "Ivan", "Ivanov", 89779660001)
    employer_id = db.db_get_employer_id(max_id)
    db.update_employer_info("123456", employer_id)
    """Сравниваем инф о сотруднике полученную по API с измененной инф в БД"""
    get_info = api.get_employer_by_id(employer_id)
    assert get_info["firstName"] == "123456"
    assert get_info["lastName"] == "Ivanov"
    assert get_info["isActive"] == True
    """БД - удаляем созданного сотрудника"""
    db.db_delete_employer(employer_id)
    """БД - удаляем последнюю созданную компанию"""
    db.delete_company(max_id)
 