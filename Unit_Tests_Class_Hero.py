import unittest
from Hero import *


class Tests(unittest.TestCase):

    def setUp(self):
        hero_name_1 = "Bron"
        hero_title_1 = "DragonSlayer"
        hero_health_1 = 100
        hero_mana_1 = 100
        hero_mana_regeneration_rate_1 = 2
        self.Bron = Hero(hero_name_1, hero_title_1, hero_health_1,
                         hero_mana_1, hero_mana_regeneration_rate_1)

        hero_name_2 = "Pesho"
        hero_title_2 = "GoshoSlayer"
        hero_health_2 = 60
        hero_mana_2 = 120
        hero_mana_regeneration_rate_2 = 5
        self.Pesho = Hero(
            hero_name_2, hero_title_2, hero_health_2, hero_mana_2, hero_mana_regeneration_rate_2)

    def test_get_name_Pesho(self):
        self.assertTrue(self.Pesho.get_name() == "Pesho")

    def test_get_title_Pesho(self):
        self.assertTrue(self.Pesho.get_title() == "GoshoSlayer")

    def test_get_maximumHealth(self):
        self.assertEqual(self.Pesho.get_maximumHealth(), 60)

    def test_get_maximumMana(self):
        self.assertEqual(self.Pesho.get_maximumMana(), 120)

    def test_known_as(self):
        self.assertEqual(self.Pesho.known_as(), "Pesho the GoshoSlayer")

    def test_is_alive(self):
        self.Pesho.set_health(0)
        self.assertEqual(self.Pesho.is_alive(), False)

    def test_is_alive_2(self):
        self.assertEqual(self.Pesho.is_alive(), True)

    def test_get_health_and_take_damage(self):
        self.Pesho.take_damage(40)
        self.assertEqual(self.Pesho.get_health(), 20)

    def test_take_healing(self):
        self.Pesho.take_damage(55)
        self.Pesho.take_healing(5)
        self.assertEqual(self.Pesho.get_health(), 10)

    def test_take_mana(self):
        self.Pesho.set_mana(30)
        self.Pesho.move_hero("left")
        self.assertEqual(self.Pesho.get_mana(), 35)


if __name__ == '__main__':
    unittest.main()
