"""
№2
В наличии список множеств. внутри множества целые числа
m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

Задание: посчитать
1 общее количество чисел
2 общую сумму чисел
3 посчитать среднее значение
4 собрать все множества в один кортеж
*написать решения в одну строку
"""
import unittest
from itertools import chain

import pytest


def total_amount(m) -> int:
    """Общее количество чисел"""
    return sum(len(i) for i in m)


def total_sum(m) -> int:
    """Общая сумма чисел"""
    return sum(sum(i) for i in m)


def average_value(m) -> float:
    """Среднее значение"""
    return sum(map(sum, m)) / sum(map(len, m))


def collect_to_tuple(m) -> tuple:
    """Все множества в одином кортеже"""
    return tuple(chain.from_iterable(m))


m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]


def test_total_amount():
    """Pytest"""
    assert total_amount([{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]) == 14


def test_total_sum():
    """Pytest"""
    assert total_sum([{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]) == 264


def test_average_value():
    """Pytest"""
    assert average_value([{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]) == 18.857142857142858


class TestCollectToTuple(unittest.TestCase):

    def test_collect_to_tuple(self):
        """Unittest"""
        self.assertEqual(collect_to_tuple(
            [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]),
            (11, 3, 5, 32, 17, 2, 87, 4, 44, 7, 8, 9, 11, 24)
        )


if __name__ == '__main__':
    print(total_amount(m))
    print(total_sum(m))
    print(average_value(m))
    print(collect_to_tuple(m))
    pytest.main()
    unittest.main()
