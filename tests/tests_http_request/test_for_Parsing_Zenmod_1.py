'''Тесты для функции авторизации в файле Parsing_Zenmod.'''


from Parsing_Zenmod import Zen_mod
import pytest


@pytest.mark.parametrize('login, password', [('', ''),
                                             ('GVJhnvsasdg', ''),
                                             ('', 'jihuHFUHFhj'),
                                             ('JHHNGjkngnGFG', 'mkmJGNGJKNG'),
                                             ('login', 'password'),
                                             ('admin', '123123123'),
                                             ('zenmod@gmail.com', 'Zenmod666')])
def test_http_request_logpas_feil(login, password):
    'Проверка завершения программы при вводе не верных пользовательских данных.'

    client = Zen_mod(login, password)
    with pytest.raises(SystemExit):
        client.http_request()

# Вместо REAL_EMAIL и REAL_PASSWORD должны стоять существующие логин и пароль
@pytest.mark.parametrize('login, password', [('REAL_EMAIL', 'REAL_PASSWORD')])
def test_http_request_logpas_sucses(login, password):
    'Проверка создания атрибута __history при успешной авторизации.'

    client = Zen_mod(login, password)
    client.http_request()
    if client.__dict__['_Zen_mod__history']:
        assert True
    else:
        assert False



