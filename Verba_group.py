'''Выполнение тестового задания от VERBA-group.'''


import requests
import json
from bs4 import BeautifulSoup

class Quotes:
    '''Класс описывающий веб-страницу для парсинга.'''

    __domen = 'https://quotes.toscrape.com'
    __path = '/page/'
    __nomber_q = 1 #Номер цитаты
    __q = {} #Словать в котором будут храниться цитаты

    def http_request(self, index):
        '''Метод отправляющий запрос к веб-странице
        для получения её исходного кода.'''

        with requests.Session() as session:
            self.__page = session.get(url=self.__domen+self.__path+index).text

    def parsing(self):
        '''Метод выполняющий парсинг веб-страницы и сохраняющий данные
        в виде словаря в атрибут __q.'''

        soup = BeautifulSoup(self.__page, 'html.parser')
        table = soup.find_all('div', {'class':'quote'})
        for box in table:
            comment = box.find('span', {'class':'text'}).getText()
            author = box.find('small', {'class':'author'}).getText()
            tags = [tag.getText() for tag in box.find_all('a', {'class':'tag'})]
            dict = {'comment':comment[1:-1], 'author':author, 'tags':tags}
            self.__q.update({str(self.__nomber_q)+' quote':dict})
            self.__nomber_q += 1

    def save_to_jason(self):
        '''Метод сохраняющий словарь из атрибута __q в json файл.'''

        with open('Verba_group.json', 'w') as file:
            json.dump(self.__q, file, indent=4)

if __name__ == '__main__':
    quotes = Quotes()
    for index in range(1, 11):
        quotes.http_request(str(index))
        quotes.parsing()
    quotes.save_to_jason()
    