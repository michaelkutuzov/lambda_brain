import unittest
import l1e7


class PrintingCosts_test(unittest.TestCase):
    def test_printing_costs1(self):
        self.assertEqual(l1e7.PrintingCosts('abcd UVW'), 158)

    def test_printing_costs2(self):
        self.assertEqual(l1e7.PrintingCosts('∂ßå   !Y'), 92)

    def test_printing_costs3(self):
        self.assertEqual(l1e7.PrintingCosts('     '), 0)
