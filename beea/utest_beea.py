import unittest
import beea


class MaximumDiscount_Test(unittest.TestCase):
    def test_maximum_discount1(self):
        self.assertEqual(beea.MaximumDiscount(
            7, [100, 300, 150, 250, 200, 400, 350]), 450)

    def test_maximum_discount2(self):
        self.assertEqual(beea.MaximumDiscount(
            2, [100, 300]), 0)

    def test_maximum_discount3(self):
        self.assertEqual(beea.MaximumDiscount(
            7, [100, 100, 100, 100, 100, 100, 100]), 200)
