import unittest
import z0ec


class Squirrel_Test(unittest.TestCase):
    def test_squirrel_0(self):
        self.assertEqual(z0ec.squirrel(0), 1)

    def test_squirrel_1(self):
        self.assertEqual(z0ec.squirrel(1), 1)

    def test_squirrel_6(self):
        self.assertEqual(z0ec.squirrel(6), 7)


if __name__ == '__main__':
    unittest.main()
