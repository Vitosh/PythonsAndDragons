from hero_person_and_weapons import *


class Fight:

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def hero_attack(self, by):
        start_fight_message = "A fight is  started beetwen  Hero{} and Enemy".format(
            self.hero, self.enemy)
        weapon_atack_messaages = "Enemy health is {}".format(e)
        if by == "weapon":
            self.enemy.set_health(
                self.enemy.get_health() - self.hero.atack(by="weapon"))
            return weapon_atack_messaages
            # Magic  make  latter

h = Hero(name="rado", title="killer")
w = Weapon("gun", 50)
h.set_weapons(w)
h.equip(w)
e = Enemy(100, 50, 10)
f = Fight(h, e)
print(f.hero_attack(by="weapon"))
