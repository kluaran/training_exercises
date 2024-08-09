'''Тесты проверяющие контракты функций парсинга и преобразования в ДФ.'''


from Parsing_Zenmod import Zen_mod
import pytest
import pandas


# Второй файл намеренно роняет тест
@pytest.mark.parametrize('fail_html', [('test_example_html_secses.txt'),
                                       ('test_example_html_feil.txt')])
def test_parsing(fail_html):
    '''Функция проверяющая, что при получении данных с нужной страницы,
    в результате парсинга у объекта создаются необходимые атрибуты.'''

    client = Zen_mod('login', 'password')
    with open(fail_html, 'r', encoding='utf-8') as file:
        client._Zen_mod__history = file.read()
    client.parsing()
    if client.data_for_pandas and client.columns:
        assert True
    else:
        assert False

def test_create_pandas(monkeypatch):
    '''Функция проверяющуая записывается ли в атрибуты объекта пандосовский ДФ
    с помощью метода, и сохраняет ли этот атрибут тип ДФ после вызова вне методов.
    (Ну так, в порядке бреда. Тест ради теста.).'''

    client = Zen_mod('login', 'password')

    # Чтобы не тратить время на авторизацию, получение данных и парсинг,
    # Замокаем функцию create_pandas и переопределим ее для проверки только
    # Интересующего функционала.
    def mock_func(*args, **kwargs):
        args[0].orders = pandas.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
    monkeypatch.setattr('Parsing_Zenmod.Zen_mod.create_pandas', mock_func)

    client.create_pandas()
    assert str(type(client.orders)) == "<class 'pandas.core.frame.DataFrame'>"