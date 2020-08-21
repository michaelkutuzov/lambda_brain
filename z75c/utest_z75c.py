import unittest
import z75c


class BastShoe_test(unittest.TestCase):
    def test_bast_shoe1(self):
        self.assertEqual(z75c.BastShoe('1 Привет'), 'Привет')

    def test_bast_shoe2(self):
        self.assertEqual(z75c.BastShoe('1 , Мир!'), 'Привет, Мир!')

    def test_bast_shoe3(self):
        self.assertEqual(z75c.BastShoe('1 ++'), 'Привет, Мир!++')

    def test_bast_shoe4(self):
        self.assertEqual(z75c.BastShoe('2 2'), 'Привет, Мир!')

    def test_bast_shoe5(self):
        self.assertEqual(z75c.BastShoe('4'), 'Привет, Мир!++')

    def test_bast_shoe6(self):
        self.assertEqual(z75c.BastShoe('4'), 'Привет, Мир!')

    def test_bast_shoe7(self):
        self.assertEqual(z75c.BastShoe('1 *'), 'Привет, Мир!*')

    def test_bast_shoe8(self):
        self.assertEqual(z75c.BastShoe('4'), 'Привет, Мир!')

    def test_bast_shoe9(self):
        self.assertEqual(z75c.BastShoe('4'), 'Привет, Мир!')

    # def test_bast_shoe10(self):
    #     self.assertEqual(z75c.BastShoe('4'), 'Привет, Мир!')

    # def test_bast_shoe11(self):
    #     self.assertEqual(z75c.BastShoe('3 6'), ',')

    # def test_bast_shoe12(self):
    #     self.assertEqual(z75c.BastShoe('2 100'), '')
