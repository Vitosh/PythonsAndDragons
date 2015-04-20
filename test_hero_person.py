import unittest
from hero_person_and_weapons import *


class Tests(unittest.TestCase):

    def setUp(self):
        hero_name = "Bron"
        hero_title = "DragonSlayer"
        self.h = Hero(hero_name, hero_title)
        self.anatema = Spell("anateema", 50, 10, 2)

    def test_class_hero_get_weapons(self):
        test_value = self.h
        test_value.set_weapons("bradva")
        self.assertTrue(len(test_value.get_weapons()) == 1)
        self.assertTrue(isinstance(test_value.get_weapons(), set))

    def test_class_hero_get_spells(self):
        test_value = self.h
        test_value.set_spells("spell1")
        self.assertTrue(len(test_value.get_spells()) == 1)
        self.assertTrue(isinstance(test_value.get_spells(), set))

    def test_class_hero_get_hero_name(self):
        test_value = self.h.get_hero_name()
        self.assertEqual(test_value, "Bron")

    def test_class_hero_get_hero_title(self):
        test_value = self.h.get_hero_title()
        self.assertEqual(test_value, "DragonSlayer")

    def test_class_hero_known_as(self):
        test_value = self.h.known_as()
        self.assertEqual(test_value, "Bron the DragonSlayer")

    def test_class_hero_get_mana(self):
        test_value = self.h.get_mana()
        self.assertEqual(test_value, 100)

    def test_class_hero_is_alive(self):
        test_value = self.h.is_alive()
        self.assertEqual(test_value, True)

        # Make new object with 0 health for test
        hero_name = "Bron"
        hero_title = "DragonSlayer"
        human = Hero(hero_name, hero_title, health=0)
        self.assertEqual(human.is_alive(), False)

    def test_class_hero_can_cast(self):
        magic = Spell("anateema", 50, 10, 2)
        test_value = self.h.can_cast(magic)
        self.assertEqual(test_value, True)

        # Make new object with 0 mana for test
        hero_name = "Bron"
        hero_title = "DragonSlayer"
        human = Hero(hero_name, hero_title, mana=0)
        self.assertEqual(human.can_cast(self.anatema), False)

    def test_class_hero_take_damage(self):
        test_value = self.h.take_damage(60)
        self.assertEqual(self.h.get_health(), 40)
        # Test if
        test_value = self.h.take_damage(40)
        self.assertEqual(self.h.get_health(), 0)

    def test_class_hero_take_healing(self):
        test_value = self.h.take_healing(50)
        self.assertEqual(self.h.get_health(), 100)
        test_value = self.h.take_healing(50)
        self.assertEqual(self.h.get_health(), 100)
        # Kill  hero
        self.h.take_damage(100)
        self.assertEqual(self.h.take_healing(10), False)

    def test_class_hero_equip(self):
        self.h.set_weapons("bow")
        self.h.equip("bow")
        self.assertEqual(self.h.get_current_weapon(), "bow")

    def test_class_hero_learn(self):
        self.h.set_spells("magiq2")
        self.h.learn("magiq2")
        self.assertEqual(self.h.get_current_spell(), "magiq2")

    def test_class_hero_atack(self):
        # Weapon test
        w = Weapon("gun", 50)
        self.h.set_weapons(w)
        self.h.equip(w)
        gun = self.h.atack("weapon")
        self.assertEqual(gun, 50)
        # Spell test
        s = Spell("anatema", 20, 10, 2)
        self.h.set_spells(s)
        self.h.learn(s)
        self.h.equip(s)
        magic = self.h.atack("magic")
        self.assertEqual(magic, 20)

    def test_class_enemy_equip(self):
        e = Enemy(100, 100, 20)
        w = Weapon("gun", 50)
        e.equip(w)
        self.assertEqual(e.get_weapon(), w)

    def test_class_enemy_learn(self):
        e = Enemy(100, 100, 20)
        s = Spell("anatema", 20, 10, 2)
        e.learn(s)
        self.assertEqual(e.get_spell(), s)

    def test_class_enemy_atack(self):
        e = Enemy(100, 100, 20)
        w = Weapon("gun", 50)
        e.equip(w)
        self.assertEqual(e.atack(), 20)
        self.assertEqual(e.atack("weapon"), 50)


if __name__ == '__main__':
    unittest.main()
