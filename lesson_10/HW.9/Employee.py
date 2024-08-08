import requests
import allure
from conftest import url

path = '/employee/'
X_client_URL = " https://x-clients-be.onrender.com"

class Employer:
    def __init__(self, url=X_client_URL):
        self.url = X_client_URL
        changed_emp_id = None


    @allure.step("Полуаем токен авторизации")
    def get_token(username='leonardo', password='leads'):
        log_pass = {'username': username, 'password': password}
        resp_token = requests.post(X_client_URL + '/auth/login', json=log_pass)
        token = resp_token.json()['userToken']
        return token

    @allure.step("Создаем компанию по названию и описанию")
    def create_company(self, name: str, description: str):
        headers = {'x-client-token': str(self.get_token)}
        company = {
            "name": name,
            "description": description
        }
        resp = requests.post(self.url + '/company', json=company, headers=headers)
        return resp.json()

    @allure.step("Получаем список сотрудников компании по ID")
    def get_list_employers(self, id: int):
        company = {'company': id}
        resp_employers = requests.get(
            self.url + '/employee', params=company)
        list_employers = resp_employers.json()
        return list_employers

    @allure.step("Добавление нового сотрудника в компанию") 
    def add_new_employer(self, new_id: int, name: str, last_name: str):
        headers = {'x-client-token': str(self.get_token)}
        body_employer = {
            'id': 0,
            'firstName': name,
            'lastName': last_name,
            'middleName': 'string',
            'companyId': new_id,
            'email': 'test@mail.ru',
            'url': 'string',
            'phone': 'string',
            'birthdate': '2023-08-14T11:02:45.622Z',
            'isActive': 'true'
        }
        resp_add_new_employer = requests.post(X_client_URL + '/employee', headers=headers, json=body_employer).json
        return resp_add_new_employer

    @allure.step("Получаем информацию о сотруднике по его ID")
    def get_employer_by_id(self, id_employee: int):
        resp = requests.get(self.url + path + str(id_employee)).json()
        return resp

    @allure.step("Обновляем данные о сотруднике")
    def change_new_employer(self, id_employee: int, last_name: str, email: str):
        headers = {'x-client-token': str(self.get_token)}
        body_change_employer = {
            'lastName': last_name,
            'email': email,
            'url': 'string',
            'phone': 'string',
            'isActive': 'true'
        }
        resp_change_employer = requests.patch(self.url + path + str(id_employee), headers=headers,
                                              json=body_change_employer)
        inform_changed_employer_id = resp_change_employer.json()
        return inform_changed_employer_id