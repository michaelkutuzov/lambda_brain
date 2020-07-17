import unittest
import cb0f


class MassVote_test(unittest.TestCase):
    def test_mass_vote1(self):
        self.assertEqual(cb0f.MassVote(
            5, [60, 10, 10, 15, 5]), 'majority winner 1')

    def test_mass_vote2(self):
        self.assertEqual(cb0f.MassVote(
            3, [10, 15, 10]), 'minority winner 2')

    def test_mass_vote3(self):
        self.assertEqual(cb0f.MassVote(
            4, [111, 110, 111, 15]), 'no winner')

    def test_mass_vote4(self):
        self.assertEqual(cb0f.MassVote(
            4, [100, 99]), 'majority winner 1')
