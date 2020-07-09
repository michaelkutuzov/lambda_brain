import unittest
import _6d4d


class WordSearch_Test(unittest.TestCase):
    def setUp(self):
        self.firstString = 'строка разбивается на набор строк через выравнивание по заданной ширине.'

    def test_split_string_0(self):
        self.assertEqual(_6d4d.SplitString(12, self.firstString), [
            'строка',
            'разбивается',
            'на набор',
            'строк через',
            'выравнивание',
            'по заданной',
            'ширине.'
        ], f'Test for {self.firstString}')

    def test_split_string_1(self):
        self.assertEqual(_6d4d.SplitString(10, 'ab cd ef'), [
            'ab cd ef'
        ])

    def test_split_string_2(self):
        self.assertEqual(_6d4d.SplitString(2, 'ab cd ef'), [
            'ab',
            'cd',
            'ef'
        ])

    def test_split_string_3(self):
        self.assertEqual(_6d4d.SplitString(3, 'ab cd ef'), [
            'ab',
            'cd',
            'ef'
        ])

    def test_split_string_4(self):
        self.assertEqual(_6d4d.SplitString(5, 'ab cd ef'), [
            'ab cd',
            'ef'
        ])


if __name__ == '__main__':
    unittest.main()
