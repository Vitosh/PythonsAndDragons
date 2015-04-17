import unittest
from Hero import *


class Tests(unittest.TestCase):

    def setUp(self):
        weapons = ["bow", "sword", "sword", "gun", "gun"]
        spells = ["magic1", "anateema", "magic2"]
        hero_name = "Bron"
        hero_title = "DragonSlayer"
        self.h = Hero(hero_name, hero_title)
        self.anatema = Spell("anateema", 50, 10, 2)

    def test_get_weapons(self):
        test_value = self.h
        test_value.set_weapons("bradva")
        self.assertTrue(len(test_value.get_weapons()) == 1)
        self.assertTrue(isinstance(test_value.get_weapons(), set))

    def test_get_spells(self):
        test_value = self.h
        test_value.set_spells("spell1")
        self.assertTrue(len(test_value.get_spells()) == 1)
        self.assertTrue(isinstance(test_value.get_spells(), set))

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
        hero_name = "Bron"
        hero_title = "DragonSlayer"
        human = Hero(hero_name, hero_title, health=0)
        self.assertEqual(human.is_alive(), False)

    def test_can_cast(self):
        magic = Spell("anateema", 50, 10, 2)
        test_value = self.h.can_cast(magic)
        self.assertEqual(test_value, True)

        # Make new object with 0 mana for test
        hero_name = "Bron"
        hero_title = "DragonSlayer"
        human = Hero(hero_name, hero_title, mana=0)
        self.assertEqual(human.can_cast(self.anatema), False)

    def test_take_damage(self):
        test_value = self.h.take_damage(60)
        self.assertEqual(self.h.get_health(), 40)
        #Test if
        test_value = self.h.take_damage(40)
        self.assertEqual(self.h.get_health(), 0)



    def test_take_healing(self):
        test_value = self.h.take_healing(50)
        self.assertEqual(self.h.get_health(), 100)
        test_value = self.h.take_healing(50)
        self.assertEqual(self.h.get_health(), 100)
        #Kill  hero
        self.h.take_damage(100)
        self.assertEqual(self.h.take_healing(10),False)


    def test_equip(self):
        self.h.set_weapons("bow")
        self.h.equip("bow")
        self.assertEqual(self.h.get_current_weapon(), "bow")

    def test_learn(self):
        self.h.set_spells("magiq2")
        self.h.learn("magiq2")
        self.assertEqual(self.h.get_current_spell(),"magiq2")


    # I will  write this method after class  Weapon is complited
    def test_atack(self):
        pass

if __name__ == '__main__':
    unittest.main()
