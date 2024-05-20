"""
№3
Имеется список списков
a = [[1,2,3], [4,5,6]]
Задание:
сделать список словарей
b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]
*написать решение в одну строку
"""
import pytest


def list_of_dictionaries(a) -> str:
    """Список словарей"""
    key_list = ['k1', 'k2', 'k3']
    return f'b = {[{key_list[0]: i[0], key_list[1]: i[1], key_list[2]: i[2]} for i in a]}'


a = [[1, 2, 3], [4, 5, 6]]


def test_list_of_dictionaries():
    """Pytest"""
    expected_result = "b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]"
    assert list_of_dictionaries([[1, 2, 3], [4, 5, 6]]) == expected_result


if __name__ == '__main__':
    print(list_of_dictionaries(a))
    pytest.main()
