import requests
import json
from conftest import url

path = '/employee/'


class Employer:
    def __init__(self, url=url):
        self.url = url

    # Список сотрудников компании
    def get_list(self, company_id: int):
        company = {'company': company_id}
        response = requests.get(
            self.url + '/employee', params=company)
        return response.json()

    # Добавление нового сотрудника в компанию
    def add_newemployee(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/employee', headers=headers, json=body)
        return response.json()

    # Получении инфо о сотруднике
    def get_info(self, employee_id: int):
        response = requests.get(self.url + path + str(employee_id))
        return response

    # Изменение инфо о сотруднике
    def change_info(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(
            self.url + path + str(employee_id), headers=headers, json=body)
        return response