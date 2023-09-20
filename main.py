import unittest


def add(x, y):
    return x + y


class TestSum(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -3), -4)


if __name__ == '__main__':
    unittest.main()




