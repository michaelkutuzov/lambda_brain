import unittest
import ab53


class TheRabbitsFoot_test(unittest.TestCase):
    def test_the_rabbits_foot1_encode(self):
        self.assertEqual(ab53.TheRabbitsFoot(
            'отдай мою кроличью лапку', True), 'омоюу толл дюиа акчп йрьк')

    def test_the_rabbits_foot1_decode(self):
        self.assertEqual(ab53.TheRabbitsFoot(
            'омоюу толл дюиа акчп йрьк', False), 'отдаймоюкроличьюлапку')

    def test_the_rabbits_foot2_encode(self):
        self.assertEqual(ab53.TheRabbitsFoot(
            'старт финиш аллес капут полёт', True), 'сфакп тилао анлпл риеуё тшстт')

    def test_the_rabbits_foot2_decode(self):
        self.assertEqual(ab53.TheRabbitsFoot(
            'сфакп тилао анлпл риеуё тшстт', False), 'стартфинишаллескапутполёт')


if __name__ == '__main__':
    unittest.main()
