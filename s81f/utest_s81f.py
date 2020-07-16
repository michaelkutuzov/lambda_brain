import unittest
import s81f


class col_form_minus_test(unittest.TestCase):
    def test_col_form_minus1(self):
        arg = ('5347', '12')
        self.assertEqual(s81f.col_form_minus(arg), '5335')

    def test_col_form_minus2(self):
        arg = ('5347', '348')
        self.assertEqual(s81f.col_form_minus(arg), '4999')

    def test_col_form_minus3(self):
        arg = ('5347', '4599')
        self.assertEqual(s81f.col_form_minus(arg), '748')

    def test_col_form_minus4(self):
        arg = ('5347', '5347')
        self.assertEqual(s81f.col_form_minus(arg), '0')

    def test_col_form_minus5(self):
        arg = ('0', '0')
        self.assertEqual(s81f.col_form_minus(arg), '0')

    def test_col_form_minus6(self):
        arg = ('98754324387', '347329847')
        self.assertEqual(s81f.col_form_minus(arg), '98406994540')


class check_for_equality_test(unittest.TestCase):
    def test_check_for_equality1(self):
        self.assertEqual(s81f.check_for_equality(
            '23567', '23467'), ('23567', '23467'))

    def test_check_for_equality2(self):
        self.assertEqual(s81f.check_for_equality(
            '23467', '23567'), ('23567', '23467'))

    def test_check_for_equality3(self):
        self.assertEqual(s81f.check_for_equality(
            '23467', '23467'), ('0', '0'))


class BigMinus_test(unittest.TestCase):
    def test_big_minus1(self):
        self.assertEqual(s81f.BigMinus('2531', '1715'), '816')

    def test_big_minus2(self):
        self.assertEqual(s81f.BigMinus('1715', '2531'), '816')

    def test_big_minus3(self):
        self.assertEqual(s81f.BigMinus('1715', '515'), '1200')

    def test_big_minus4(self):
        self.assertEqual(s81f.BigMinus(
            '98754324387', '347329847'), '98406994540')

    def test_big_minus5(self):
        self.assertEqual(s81f.BigMinus(
            '347329847', '98754324387'), '98406994540')
