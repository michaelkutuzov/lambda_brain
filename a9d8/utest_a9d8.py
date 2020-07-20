import unittest
import a9d8


class get_stop_time_test(unittest.TestCase):
    def test_get_stop_time1(self):
        self.assertEqual(a9d8.get_stop_time(3, 5, 5), 2)

    def test_get_stop_time2(self):
        self.assertEqual(a9d8.get_stop_time(7, 2, 2), 0)


class Unmanned_test(unittest.TestCase):
    def test_unmanned1(self):
        self.assertEqual(a9d8.Unmanned(10, 2, [[3, 5, 5], [5, 2, 2]]), 12)

    def test_unmanned2(self):
        self.assertEqual(a9d8.Unmanned(10, 2, [[0, 5, 5], [5, 2, 2]]), 15)

    def test_unmanned3(self):
        self.assertEqual(a9d8.Unmanned(10, 2, [[11, 5, 5], [15, 2, 2]]), 10)

    def test_unmanned4(self):
        self.assertEqual(a9d8.Unmanned(10, 2, [[5, 5, 5], [15, 2, 2]]), 10)
