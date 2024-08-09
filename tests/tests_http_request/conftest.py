'''Файл с фикстурой для тестов авторизации.'''


import pytest
import requests


@pytest.fixture(autouse=True)
def check_requests_status():
    '''Функция проверяет стаут URl для авторизации,
    если статус больше 400 пропускает тест.'''

    url = 'https://perm.zenmod.shop/account/login'
    auth_form = requests.head(url, timeout=30)
    if auth_form.status_code >= 400:
        pytest.skip(f'Error: {auth_form.status_code}')
