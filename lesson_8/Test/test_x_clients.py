import pytest
import requests
from lesson_8.Pages.Employee import Employer, Company
# from lesson_8.constants import URL

employer = Employer()
company = Company()


def test_authorization(get_token):
    token = get_token
    """Удостоверяемся, что токен не пустой"""
    assert token is not None
    """Удостовреяемся, что токен имеет строковый формат"""
    assert isinstance(token, str)


def test_getcompany_id():
    company_id = company.last_active_company_id()
    """Удостоверяемся, что ID не пустой"""
    assert company_id is not None
    """ID компании состоит только из цифр"""
    assert str(company_id).isdigit()


def test_add_employer(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Igor',
        'lastName': 'Ivanov',
        'middleName': 'string',
        'companyID': com_id,
        'email': 'test1@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-07-27T10:32:13.088Z',
        'isActive': 'true'
    }
    new_employer_id = (employer.add_newemployee(token, body_employer))['id']
    """Удостоверяемся, что ID этого сотрудника не пустой"""
    assert new_employer_id is not None
    """Проверяем, что ID сотрудника состоит только из цифр"""
    assert str(new_employer_id).isdigit()

    """Получаем инфо о добавлении сотрудника"""
    info = employer.get_info(new_employer_id)
    """Сравниваем ID сотрудника из полученной инфо с ID сотрудника созданного"""
    assert info.json()['id'] == new_employer_id
    """Проверяем, что код ответа == 200"""
    assert info.status_code == 200

    
    """Проверяем невозможность создания клиента без токена"""


def test_add_employer_without_token():
    com_id = company.last_active_company_id()
    token = ""
    body_employer = {
        'id': 0,
        'firstName': 'Igor',
        'lastName': 'Ivanov',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-07-25T10:48:24.769Z',
        'isActive': 'true'
    }
    new_employer = employer.add_newemployee(token, body_employer)
    assert new_employer['message'] == 'Unauthorized'


"""Проверяем невозможность создания клиента без тела запроса"""


def test_add_employer_without_body(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {}
    new_employer = employer.add_newemployee(token, body_employer)
    assert new_employer['message'] == 'Internal server error'


def test_get_employer():
    com_id = company.last_active_company_id()
    """Получаем список работников конкретной компании"""
    list_employers = employer.get_list(com_id)
    """Проверяем, что нам вернулся список [], а не строка, число и тп"""
    assert isinstance(list_employers, list)


"""Проверка обязательного поля 'ID компании' в
запросе на получение списка работников - без ID компании (пустая строка)"""


def test_get_list_employers_invalid_company_id():
    try:
        employer.get_list('')
    except TypeError as e:
        assert str(
            e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"


"""Проверка обязательного поля 'ID сотрудника' в
запросе на получение информации о сотруднике - без ID сотрудника"""


def test_get_info_new_employers_missing_employer_id():
    try:
        employer.get_info()
    except TypeError as e:
        assert str(
            e) == "Employer.get_info() missing 1 required positional argument: 'employee_id'"


def test_change_employer_info(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Igor',
        'lastName': 'Ivanov',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-07-25T10:48:24.769Z',
        'isActive': 'true'
    }
    just_employer = employer.add_newemployee(token, body_employer)
    id = just_employer['id']
    body_change_employer = {
        'lastName': 'Petrov',
        'email': 'test123@mail.ru',
        'url': 'string',
        'phone': 'string',
        'isActive': 'true'
    }
    employer_changed = employer.change_info(token, id, body_change_employer)
    assert employer_changed.status_code == 200

    """Проверка, что ID сотрудника соответствует ID при создании сотрудника"""
    assert id == employer_changed.json()['id']

    """Проверяем, что почта изменилась"""
    assert (employer_changed.json()["email"]
            ) == body_change_employer.get("email")
