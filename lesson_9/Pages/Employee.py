import requests
import json
# from lesson_9.conftest import url

path = '/employee/'

class Employer:
    def __init__(self, url=url):
        self.url = url

        # Список сотрудников компании
