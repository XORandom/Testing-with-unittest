import random
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self) -> None:
        print('Создание данных для тестов')
        # self.seq = [i for i in range(10)]
        self.seq = list(range(10))  # То же самое

    def test_shuffle(self):
        print('test_shuffle')
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        tup = (1, 2, 3, 4, 5)
        self.assertRaises(TypeError, random.shuffle, tup)

    def test_choise(self):
        print('test_choise')
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)
        self.assertIn(element, self.seq)


if __name__ == '__main__':
    unittest.main()
