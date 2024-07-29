import pytest
import requests
from lesson_8.constants import URL

@pytest.fixture()
def get_token(username='leonardo', password='leads'):
    log_pass = {'username': username, 'password': password}
    resp_token = requests.post(URL + '/auth/login', json=log_pass)
    token = resp_token.json()['userToken']
    return token
