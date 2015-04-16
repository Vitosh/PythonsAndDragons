import unittest
from Hero import *


class Tests(unittest.TestCase):

    def setUp(self):
        weapons = ["bow", "sword", "sword", "gun", "gun"]
        spells = ["magic1", "anateema", "magic2"]
        hero_name = "Bron"
        hero_title = "DragonSlayer"
        self.h = Hero(hero_name, hero_title, weapons, spells)

    def test_get_weapons(self):
        test_value = self.h.get_weapons()
        self.assertTrue(len(test_value) == 3)
        self.assertTrue(isinstance(test_value, set))

    def test_get_spells(self):
        test_value = self.h.get_spells()
        self.assertTrue(len(test_value) == 3)
        self.assertTrue(isinstance(test_value, set))

    def test_get_hero_name(self):
        test_value = self.h.get_hero_name()
        self.assertEqual(test_value, "Bron")

    def test_get_hero_title(self):
        test_value = self.h.get_hero_title()
        self.assertEqual(test_value, "DragonSlayer")

    def test_known_as(self):
        test_value = self.h.known_as()
        self.assertEqual(test_value, "Bron the DragonSlayer")

    def test_get_mana(self):
        test_value = self.h.get_mana()
        self.assertEqual(test_value, 100)

    def test_is_alive(self):
        test_value = self.h.is_alive()
        self.assertEqual(test_value, True)

        # Make new object with 0 health for test

        weapons = ["bow", "sword", "sword", "gun", "gun"]
        spells = ["magic1", "anateema", "magic2"]
        hero_name = "Bron"
        hero_title = "DragonSlayer"
        human = Hero(hero_name, hero_title, weapons, spells, health=0)
        self.assertEqual(human.is_alive(), False)

    def test_can_cast(self):
        test_value = self.h.can_cast()
        self.assertEqual(test_value, True)

        # Make new object with 0 mana for test

        weapons = ["bow", "sword", "sword", "gun", "gun"]
        spells = ["magic1", "anateema", "magic2"]
        hero_name = "Bron"
        hero_title = "DragonSlayer"
        human = Hero(hero_name, hero_title, weapons, spells, mana=0)
        self.assertEqual(human.can_cast(), False)

    def test_take_damage(self):
        test_value = self.h.take_damage(50)
        self.assertEqual(test_value, 50)
        test_value = self.h.take_damage(50)
        self.assertEqual(test_value, 0)

    def test_take_healing(self):
        test_value = self.h.take_healing(50)
        self.assertEqual(test_value, False)

        # if Hero is dead
        weapons = ["bow", "sword", "sword", "gun", "gun"]
        spells = ["magic1", "anateema", "magic2"]
        hero_name = "Bron"
        hero_title = "DragonSlayer"
        human = Hero(hero_name, hero_title, weapons, spells, health=0)
        self.assertEqual(human.take_healing(50), False)

        # if hero health = 1
        human2 = Hero(hero_name, hero_title, weapons, spells, health=1)
        self.assertEqual(human2.take_healing(50), 51)

        # if hero take healing  = -50
        human2 = Hero(hero_name, hero_title, weapons, spells, health=1)
        self.assertEqual(human2.take_healing(-50), False)

    def test_is_mana_points_over100p(self):
        test_value = self.h.is_mana_points_over_100p(200)
        self.assertEqual(test_value, True)

        weapons = ["bow", "sword", "sword", "gun", "gun"]
        spells = ["magic1", "anateema", "magic2"]
        hero_name = "Bron"
        hero_title = "DragonSlayer"
        human = Hero(hero_name, hero_title, weapons, spells, mana=0)
        self.assertEqual(human.is_mana_points_over_100p(100), False)

    def test_regeneration(self):
        test_value = self.h.regeneration(True)
        self.assertEqual(test_value, 100)

        weapons = ["bow", "sword", "sword", "gun", "gun"]
        spells = ["magic1", "anateema", "magic2"]
        hero_name = "Bron"
        hero_title = "DragonSlayer"
        human = Hero(hero_name, hero_title, weapons, spells, mana=0)
        self.assertEqual(human.regeneration(True), 1)

    def test_equip(self):
        test_value = self.h.equip("bow")
        self.assertEqual(self.h.get_current_weapon(), "bow")

    def test_learn(self):
        test_value = self.h.learn("magic2")
        self.assertEqual(self.h.get_current_spell(), "magic2")

    # I will  write this method after class  Weapon is complited
    def test_atack(self):
        pass

if __name__ == '__main__':
    unittest.main()
