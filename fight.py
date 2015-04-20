from hero_person_and_weapons import *


class Fight:

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def hero_attack(self, by):
        start_fight_message = "A fight is  started beetwen  Hero({}) and Enemy ({})".format(
            self.hero, self.enemy)
        print(start_fight_message)
        if by == "weapon":
            self.enemy.set_health(
                self.enemy.get_health() - self.hero.atack(by="weapon"))
            return "Enemy health is {} Enemy is alive : {}".format(self.enemy.get_health(), self.enemy.is_alive())

    @staticmethod
    def test():
        h = Hero(name="rado", title="killer")
        w = Weapon("gun", 10)
        h.set_weapons(w)
        h.equip(w)
        e = Enemy(100, 50, 10)
        print(e.get_health())
        f = Fight(h, e)
        print(f.hero_attack(by="weapon"))

if __name__ == '__main__':
    Fight.test()
