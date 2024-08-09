'''Получение истории заказов с сайта Zenmod в виде pandas DF.'''


import requests
import pandas
import sys
from bs4 import BeautifulSoup


class Zen_mod():
    '''Класс описывающий процесс авторизации на сайте,
    получения данных со страницы заказов,
    парсинг этой страницы и занесение полученныйх данных в DF.'''

    __domen_name = 'https://perm.zenmod.shop'
    __login_path = '/account/login'
    __history_path = '/account/order-history'
    __data_dict = {'login' : None,
                   'password': None}
    __user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/127.0.0.0 Safari/537.36'}
    data_for_pandas = []

    def __init__(self, login, password):
        '''Вводим логин и пароль пользователя.'''

        self.__data_dict['login'] = login
        self.__data_dict['password'] = password

    def http_request(self):
        '''Функция для авторизации на сайте и получения данных со страницы заказов.'''

        with requests.Session() as session:
            session.headers.update(self.__user_agent)
            zm = session.post(url=self.__domen_name+self.__login_path,
                         data=self.__data_dict)
            # Если данные пользователя не верные завершаем программу.
            if 'warning' in zm.json():
                print('НЕ ВЕРНЫЙ ЛОГИН ИЛИ ПАРОЛЬ!')
                sys.exit()
            # Если верные, получаем данные со страницы закозов в виде html.
            self.__history = session.get(url=self.__domen_name+self.__history_path).text

    def parsing(self):
        '''Функция для парсинга страницы заказов и подготовки данных к занесению в DF.'''

        soup = BeautifulSoup(self.__history, 'html.parser')
        # Находим нужную таблицу в html.
        table = soup.find('table', {'class': 'orders__table'})
        # Разбиваем её на строки.
        rows = table.find_all('tr')

        for n in range(len(rows)):
            # Каждую строку разбиваем на ячейки.
            cells = rows[n].find_all('td')
            spisok = []
            # Из каждой ячейки извлекаем текст и добавляем в список.
            for cell in cells:
                cell = cell.getText()
                spisok.append(cell)
            # Если это была первая строка, сохраняем её отдельно,
            # Для последующего переноса в заголовки колонок DFа.
            if not n:
                self.columns = spisok.copy()
            # Если нет, сохраняем строку в переменную данных будущего DFа.
            else:
                self.data_for_pandas.append(spisok)

    def create_pandas(self):
        '''Функция создающая DF из полученных данных.'''

        self.orders = pandas.DataFrame(data=self.data_for_pandas, columns=self.columns)


if __name__ == '__main__':
    client = Zen_mod(input('Введите почту: '), input('Введите пароль: '))
    client.http_request()
    client.parsing()
    client.create_pandas()
    print(client.orders)

    # Сохранил свои данные по заказам
    # client.orders.to_csv('My_Zenmod_orders.csv')