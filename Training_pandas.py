
'''Применение Pandas к анализу данных о постаяльцах отелей.'''

import pandas as pd

# Загрузка датасета с отелями.
df_houtels = pd.read_csv('https://stepik.org/media/attachments/lesson/360344/bookings.csv', sep=';')

# Приведение названий колонок к нижнему регистру
# и замена пробелов на нижнее подчёркивание.
cols = df_houtels.columns
cols_new = []
for col_name in cols:
    if ' ' in col_name:
        col_name = col_name.replace(' ', '_')
    cols_new.append(col_name.lower())
df_houtels = df_houtels.rename(columns=dict(zip(cols, cols_new)))

# Топ 5 стран по количеству успешных бронирований.
top5_contrys_fo_reservation = df_houtels.query('is_canceled == 0').\
    groupby(['country']).size().sort_values(ascending=False).\
    head(5)
print('\n\nТоп 5 стран по количеству успешных бронирований: ')
print(top5_contrys_fo_reservation)

# Среднее количество забронированных ночей в отелях разного типа.
mean_nights_different_types_hotels = round(df_houtels.groupby('hotel').\
    agg({'stays_total_nights': 'mean'}), 2)
print('\n\nСреднее количество забронированных ночей в отелях разного типа: ')
print(mean_nights_different_types_hotels)

# Количество случаев овербукинга (фактический номер не совпадает с зарезервированным).
coll_overbookings = df_houtels.query('assigned_room_type!=reserved_room_type').shape[0]
print('\n\nКоличество случаев овербукинга =', coll_overbookings)

# Самые популярные месяца для бронирования в 2016 и 2017 годах.
month_reservation = df_houtels.query('is_canceled == 0').\
    groupby(['arrival_date_year', 'arrival_date_month']).\
    size()
print('\n\nСамые популярные месяца для бронирования')
print(f'2016: {month_reservation[2016].idxmax()}', f'2017: {month_reservation[2017].idxmax()}', sep='\n')

# Месяца с наибольшей отменой бронирования по каждому году.
month_canceled_reservation = df_houtels.query('hotel == "City Hotel" and is_canceled == 1').\
    groupby(['arrival_date_year', 'arrival_date_month']).\
    size()
print('\n\nМесяца с наибольшей отменой бронирования по каждому году')
for year in sorted(list(set(map(lambda x: x[0], month_canceled_reservation.keys())))):
    print(f'{year}: {month_canceled_reservation[year].idxmax()}')

# Поиск возростной группы с наибольшим средним значением.
naib_vozrost_gruppa = df_houtels.loc[:, ['adults', 'children', 'babies']].mean().idxmax()
print('\n\nВозростная группа с наибольшим средним значением:', naib_vozrost_gruppa)

# Поиска типа отелей, который пользуется большей популярностью у людей с детьми.
df_houtels['total_kids'] = df_houtels['children'] + df_houtels['babies']
hotel_typ_for_peoples_with_kids = round(df_houtels.groupby('hotel').\
    agg({'total_kids': 'mean'}), 2)
print('\n\nСреднее количество детей в каждом отеле: ')
print(hotel_typ_for_peoples_with_kids)

# Создание столбца 'has_kids' в котором будет значение True,
# если у клиента есть хотя бы один ребёнок, иначе False.
# Поиск процентного отношения успешной брони,
# в зависимости от наличия детей у клиентов.
df_houtels['has_kids'] = df_houtels['total_kids'] > 0
churn_rate = round(df_houtels.groupby('has_kids')['is_canceled'].\
                   value_counts(normalize=True)*100, 2)
print('\n\nПроцентные доли успешного и отмененного бронирования, в зависимости от наличия детей у клиентов: ')
print(churn_rate)