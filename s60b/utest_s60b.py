import unittest
import s60b


class SumOfThe_Test(unittest.TestCase):
    def test_sum_of_the1(self):
        self.assertEqual(s60b.SumOfThe(
            7, [100, -50, 90, 90, 10, -25, -35]), 90)

    def test_sum_of_the2(self):
        self.assertEqual(s60b.SumOfThe(7, [-45, 5, -25, -35, 10]), -45)


if __name__ == '__main__':
    unittest.main()
