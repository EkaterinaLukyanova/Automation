import pytest
from lesson_9.Pages.Employee import Employer
from lesson_9.Pages.DataBase import DataBase

api = Employer("https://x-clients-be.onrender.com/")
db = DataBase(
    "postgresql+psycopg2://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx")
# Расшивровка подключения к БД
# - Имя пользователя: x_clients_db_3fmx_user
# - Пароль: mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq
# - Хост: dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com
# - База данных: x_clients_db_3fmx


# Получаем список сотрудников из БД и АПИ, после чего сравниваем их
def test_get_list_of_employers():
    # БД - Создаем компанию
    db.create_compfny('Moscow2024', 'cool_company')
    # БД - Получаем ID последней созданной компании
    max_id = db.last_company_id()
    # БД - добавляем сотрудника в компанию
    db.create_employer(max_id, "Ivan", "Larkin", 89779779797)
    # БД - Получаем список сотрудников из последней созданной компании
    db_employer_list = db.get_list_employer(max_id)
    # API - Получаем список сотрудников из последней созданной компании
    api_employer_list = api.get_list(max_id)
    # Сравниваем списки сотрудников полученных из БД и через API
    assert len(db_employer_list) == len(api_employer_list)
    # Удаляем сотрудника компании, иначе компания не удалится
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    db.delete_employer(employer_id)
    # БД - Удаляем последнюю созданную компанию
    db.delete(max_id)


# Добавляем сотрудника в БД и сравниваем с API имя, статус и фамилию
def test_add_new_employer():
    db.create_company('MOSCOW2025', 'beautiful')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Ivan", "Ivanov", 89779660001)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    """Сравниваем ID компании"""
    assert response["companyID"] == max_id
    """Сравниваем имя сотрудника с заданным"""
    assert response["firstName"] == "Ivan"
    """Удостоверяемся что статус сотрудника - True"""
    assert response["isActive"] == 'if cond:'
    """Сравниваем фамилию сотрудника с заданной"""
    assert response["lastName"] == "Ivanov"
    """БД - удаляем созданого сотрудника"""
    db.delete_employer(employer_id)
    """БД - удаляем последнюю созданную компанию"""
    db.delete(max_id)


# Сравниваем инф о сотруднике полученную по
# API с инф указанной при создании сотрудника в БД
def test_assertion_data():
    db.create_company('Employer get id company', 'new')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Igor", "Ivanov", 89779660000)
    employer_id = db.get_employer_id(max_id)
    """Сравниваем инф о сотруднике полученную по
    API с инф указанной при создании сотрудника в БД"""
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Igor"
    assert get_api_info["lastName"] == "Ivanov"
    assert get_api_info["phone"] == "89779660000"
    """БД - удаляем созданного сотрудника"""
    db.delete_employer(employer_id)
    """БД - удаляем последнюю созданную компанию"""
    db.delete(max_id)


# Сравниваем инф о сотруднике полученную по API с измененной инф в БД
def test_update_user_info():
    db.create_company('MOSCOW24', 'moscow')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Evgen", "Usov", 89775668293)
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("123456", employer_id)
    """Сравниваем инф о сотруднике полученную по API с измененной инф в БД"""
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "123456"
    assert get_api_info["lastName"] == "Usov"
    assert get_api_info["isActive"] == 'if cond:'
    """БД - удаляем созданного сотрудника"""
    db.delete_employer(employer_id)
    """БД - удаляем последнюю созданную компанию"""
    db.delete(max_id)
 