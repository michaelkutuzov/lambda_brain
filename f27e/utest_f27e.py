import unittest
import f27e


# class find_min_greatest_num_test(unittest.TestCase):
#     def test_fmgn1(self):
#         self.assertEqual(f27e.find_min_greatest_num('вкиб'), 2)

#     def test_fmgn2(self):
#         self.assertEqual(f27e.find_min_greatest_num('ddd'), 0)

#     def test_fmgn3(self):
#         self.assertEqual(f27e.find_min_greatest_num('ая'), 1)

#     def test_fmgn4(self):
#         self.assertEqual(f27e.find_min_greatest_num('яа'), 0)


# class switch_letters_test(unittest.TestCase):
#     def test_sl1(self):
#         self.assertEqual(f27e.switch_letters('вкиб', 0, 2), 'иквб')

#     def test_sl2(self):
#         self.assertEqual(f27e.switch_letters('иквб', 1, 3), 'ибвк')


# class check_asc_test(unittest.TestCase):
#     def test_ca1(self):
#         self.assertEqual(f27e.check_asc('abc'), True)

#     def test_ca2(self):
#         self.assertEqual(f27e.check_asc('bac'), False)

#     def test_ca3(self):
#         self.assertEqual(f27e.check_asc('бвк'), True)

#     def test_ca4(self):
#         self.assertEqual(f27e.check_asc('кмл'), False)


class BiggerGreater_test(unittest.TestCase):
    def test_bg1(self):
        self.assertEqual(f27e.BiggerGreater('ая'), 'яа')

    def test_bg2(self):
        self.assertEqual(f27e.BiggerGreater('fff'), '')

    def test_bg3(self):
        self.assertEqual(f27e.BiggerGreater('нклм'), 'нкмл')

    def test_bg4(self):
        self.assertEqual(f27e.BiggerGreater('вибк'), 'викб')

    def test_bg5(self):
        self.assertEqual(f27e.BiggerGreater('вкиб'), 'ибвк')
