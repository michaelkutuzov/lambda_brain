import unittest
import b519


class ShopOLAP_test(unittest.TestCase):
    def test_shopolap1(self):
        self.assertEqual(b519.ShopOLAP(5, ['платье1 5',
                                           'сумка32 2',
                                           'платье1 1',
                                           'сумка23 2',
                                           'сумка128 4']), [
                         'платье1 6', 'сумка128 4', 'сумка23 2', 'сумка32 2'])

    def test_shopolap2(self):
        self.assertEqual(b519.ShopOLAP(8, ['платье1 5',
                                           'сумка32 2',
                                           'платье1 2',
                                           'сумка0 1',
                                           'платье1 1',
                                           'сумка23 2',
                                           'сумка128 4',
                                           'сумка0 28', ]), [
                         'сумка0 29', 'платье1 8', 'сумка128 4', 'сумка23 2', 'сумка32 2'])
