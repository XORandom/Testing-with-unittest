import unittest


def setUpModule():
    """
    Глобальная настройка параметров для класса. Устанавливает параметры для всех тестов.
    :return:
    """
    print('setUpModule')


def tearDownModule():
    """
    Завершает работу теста. Необязательно использовать в обычных случаях, т.кю сборщик мусора работает.
    :return:
    """
    print('tearDownModule')


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Глобальная настройка для класса.
        :return:
        """
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self) -> None:
        """
        Запускается перед выполнением каждого теста в классе.
        :return:
        """
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test1(self):
        print('test1')

    def test2(self):
        print('test2')


if __name__ == '__main__':
    unittest.main()
