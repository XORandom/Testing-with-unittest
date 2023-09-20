import unittest
from typing import Optional, List


class SuperFunction:
    def __init__(self, data: Optional[List] = None):
        self.data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value: Optional[List] = None):
        if not isinstance(value, (type(None), List)):
            raise TypeError
        if value is None:
            self._data = []
        else:
            self._data = value

    def append(self, value):
        if isinstance(value, (int, float)):
            self._data.append(value)
        else:
            raise TypeError

    @staticmethod
    def sum_value(lis_: list):
        for i in range(1, len(lis_)):
            if type(lis_[i]) != type(lis_[i - 1]):
                """Сумма, только если все аргументы одного типа"""
                raise TypeError('объекты разного типа')
        return sum(lis_)

    def __str__(self):
        return f'Данные = {self._data}'

    def __repr__(self):
        return f'{self.__class__.__name__}, data={self._data}'


if __name__ == '__main__':
    data = SuperFunction([1, 2, 3])
    data.append(4)
    print(SuperFunction.sum_value([1, 2, 3, 4, 5]))
