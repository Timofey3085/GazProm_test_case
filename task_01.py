"""
Имеется текстовый файл file.csv,
в котром разделитель полей с данными: | (верт. черта)
пример ниже содержит небольшую часть этого файла
(начальные 3 строки, включая строку заголовков полей)

Пример:
lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998 |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972 |457865234-3431
Фамилия3|Имя3|Отчество3|21.11.1998|312040348-3048
...

Задание:
1 Реализовать сбор уникальных записей
2 Случается, что под одиннаковым id присутствуют разные данные - собрать отдельно такие записи
"""
import numpy as np
import pandas as pd
import pytest

# Чтение csv файла с разделителем |
df = pd.read_csv('file.csv', sep='|', encoding='cp1251')

# Получение уникальных значений по каждому столбцу
unique_lastname = df['lastname'].unique()
unique_name = df['name'].unique()
unique_patronymic = df['patronymic'].unique()
unique_date_of_birth = df['date_of_birth'].unique()
unique_id = df['id'].unique()

# Объединим уникальные значения из столбцов
unique_values = np.concatenate((unique_lastname, unique_name, unique_patronymic, unique_date_of_birth, unique_id))

# Группировка записей с одинаковым id, но разными данными
duplicates = df[df.duplicated(subset='id', keep=False)]


def test_unique_lastname():
    assert 'Фамилия1' in unique_lastname


def test_unique_name():
    assert 'Имя1' in unique_name


def test_unique_patronymic():
    assert 'Отчество1' in unique_patronymic


def test_unique_date_of_birth():
    assert '21.11.1998' in unique_date_of_birth


def test_unique_id():
    assert '312040348-3048' in unique_id


if __name__ == '__main__':
    print(unique_values)
    print(duplicates)
    pytest.main([__file__])

# увидеть результат работы и результаты тестов в терминале python task_01.py
