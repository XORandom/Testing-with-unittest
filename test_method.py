import unittest


class MyClass(list):
    ...


class TestMyClass(unittest.TestCase):
    def setUp(self) -> None:
        print('setUp')
        self.my_list = MyClass()

    def tearDown(self) -> None:
        print('tearDown')
        self.my_list.clear()

    def test_case_append(self):
        print('test_case_append')
        self.my_list.append(1)
        self.assertEqual(self.my_list, [1])

    def test_case_pop(self):
        print('test_case_pop')
        self.assertRaises(IndexError, lambda x: x.pop(), self.my_list)

    def test_case_pop2(self):
        print('test_case_pop2')
        with self.assertRaises(IndexError):
            self.my_list.pop()

    def test_case_pop3(self):
        print('test_case_pop3')
        self.assertRaises(IndexError, self.my_list.pop)
