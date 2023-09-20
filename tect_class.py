import sys
import unittest


class MyList(list):
    ...


class TestMyClass(unittest.TestCase):
    my_list = None

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass')
        cls.my_list = MyList()

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')
        cls.my_list.clear()


    @unittest.skipUnless(sys.platform.startswith('win32'), 'Требуется windows')
    def test_case_append(self):
        print('test_case_append')
        self.my_list.append(1)
        self.assertEqual(self.my_list, [1])

    @unittest.skip('Пропускаю тест')
    def test_case_extend(self):
        print('test_case_extend')
        self.my_list.extend([2, 3, 4])
        self.assertEqual(self.my_list, [1, 2, 3, 4])
    @unittest.skip('Пропускаю тест')
    def test_case_pop(self):
        print('test_case_pop')
        self.my_list.pop()
        self.assertEqual(self.my_list, list(range(1, 4)))

    @unittest.skipIf(__name__ != 'test_case_pop_again', 'Пропускаю тест, если __name__ != "test_case_pop_again"')
    def test_case_pop_again(self):
        print('test_case_pop_again')
        self.assertEqual(self.my_list.pop(), 3)

    @unittest.skipIf(__name__ != 'main', 'Пропускаю тест, если __name__ != "main"')
    def test_case_view(self):
        print('test_case_view')
        self.assertEqual(self.my_list, [1, 2])


if __name__ == '__main__':
    unittest.main()
