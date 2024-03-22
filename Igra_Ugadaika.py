'''Игра на угадывание случайного числа на заданном промежутке'''

from random import *

def is_valid(num):
    '''Проверка ответа пользователя на целочисленность и попадание в диапазон установленных значений'''
    if num.isdigit() and 1<=int(num)<=int(n_max):
        return True
    else:
        return False

# Основное тело программы
flag = True
while flag:
    # Закладывание верхнего предела и генерация случайного числа
    while True:
        n_max = input('Введите целое число от 2 и более: ')
        b = is_valid(n_max)
        if b == False or int(n_max)<2:
            print('Не верные данные!')
        else:
            x = randint(1, int(n_max))
            print('Добро пожаловать в числовую угадайку!')
            cnt = 0
            break

    # Процесс угадывания числа пользователем
    while True:
        num = input(f'Введите целое число от 1 до {n_max}: ')
        a = is_valid(num)
        if a == False:
            print(f'А может быть все-таки введем целое число от 1 до {n_max}?')
        else:
            num = int(num)
            if num<x:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                cnt+=1
            elif num>x:
                print('Ваше число больше загаданного, попробуйте еще разок')
                cnt+=1
            else:
                cnt+=1
                print(f'Вы угадали, поздравляем!\nКоличество попыток: {cnt}')
                break

    # Повторить ли программу ещё раз или завершить
    while True:
        trying = input('Хотите сыграть ещё раз? ')
        if trying.lower().strip()=='да':
            break
        elif trying.lower().strip()=='нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            flag =False
            break
        else:
            print('Ваш ответ непонятен, введите ДА или НЕТ')