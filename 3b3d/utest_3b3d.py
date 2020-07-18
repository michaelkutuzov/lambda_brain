import unittest
import _3b3d


class convert_test(unittest.TestCase):
    def test_convert1(self):
        self.assertEqual(_3b3d.convert([1234, 1777], 8), [668, 1023])

    def test_convert2(self):
        self.assertEqual(_3b3d.convert([1234, 1777], 16), [4660, 6007])


class UFO_test(unittest.TestCase):
    def test_ufo1(self):
        self.assertEqual(_3b3d.UFO(2, [1234, 1777], False), [4660, 6007])

    def test_ufo2(self):
        self.assertEqual(_3b3d.UFO(2, [1234, 1777], True), [668, 1023])
