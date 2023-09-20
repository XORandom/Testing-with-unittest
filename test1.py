import unittest

from calculator import Calculator


class TestStringMethod(unittest.TestCase):
    print('TestString')

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_isupper(self):
        self.assertTrue('TEST'.isupper())
        self.assertFalse('test'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
        self.assertRaises(TypeError, lambda x: x.split(2), s)


class TestCalculator(unittest.TestCase):
    print('TestCalculator')

    def test_add(self):
        print('test_add')
        self.assertEqual(Calculator.add(5, 3), 8)

    def iadd(self, value):
        print('test_iadd')
        c = Calculator(2)
        c.iadd(3)
        self.assertEqual(c.value, 5)

    def test_class_color(self):
        print('test_class_color')
        self.assertEqual(Calculator.color, 'black')
        Calculator.color = 'red'
        self.assertEqual(Calculator.color, 'red')

    def test_object_color(self):
        print('test_object_color')
        c = Calculator(0)
        c.color = 'yellow'
        self.assertEqual(Calculator.color, 'yellow')
        c.set_color('red')
        self.assertEqual(Calculator.color, 'red')


if __name__ == '__main__':
    unittest.main()
