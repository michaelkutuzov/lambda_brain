import unittest
import d146


class LineAnalisys_Test(unittest.TestCase):
    def test_line_analisys1(self):
        self.assertEqual(d146.LineAnalysis("*..*..*..*..*..*..*"), True)

    def test_line_analisys2(self):
        self.assertEqual(d146.LineAnalysis("*"), True)

    def test_line_analisys3(self):
        self.assertEqual(d146.LineAnalysis("***"), True)

    def test_line_analisys4(self):
        self.assertEqual(d146.LineAnalysis("*.......*.......*"), True)

    def test_line_analisys5(self):
        self.assertEqual(d146.LineAnalysis("**"), True)

    def test_line_analisys6(self):
        self.assertEqual(d146.LineAnalysis("*.*"), True)

    def test_line_analisys7(self):
        self.assertEqual(d146.LineAnalysis("*..*...*..*..*..*..*"), False)

    def test_line_analisys8(self):
        self.assertEqual(d146.LineAnalysis("*.."), False)

    def test_line_analisys9(self):
        self.assertEqual(d146.LineAnalysis(".*."), False)

    def test_line_analisys10(self):
        self.assertEqual(d146.LineAnalysis("*.*..*..*"), False)
