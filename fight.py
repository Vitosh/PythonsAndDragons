from hero_person_and_weapons import *


class FightMessages:

    START = "A fight is  started beetwen  Hero({}) and Enemy ({})"
    SPELL_ATTACK = "Hero casts a {}, hits enemy for {} dmg. Enemy health is {}"
    WEAPON_ATTACK = "Hero hits with {} for {} dmg. Enemy health is {}"
    ENEMY_MOVES = "Enemy moves one square to the {} in order to get to the hero. This is his move."
    NOT_HAVE_MANA = "Hero does not have mana for another {}"
    ENEMY_HIT = "Enemy hits hero for {} dmg. Hero health is {}"
    ENEMY_IS_DEAD = "Enemy is dead!"
    HERO_IS_DEAD = "Hero is dead!"


class Fight:

    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def hero_attack(self, by):
        print(FightMessages.START.format(self.hero, self.enemy))
        if by == "weapon":
            self.enemy_health_down(by)
            print(self.hero_attack_result(by))
            if self.is_enemy_dead(self.enemy):
                print(FightMessages.ENEMY_IS_DEAD)
        # TODO : ADD range  logic
        elif by == "magic" and self.hero.can_cast():
            self.enemy_health_down("magic")
            self.hero_mana_down()
            print(self.hero_attack_result())

    def enemy_health_down(self, by):
        self.enemy.set_health(
            self.enemy.get_health() - self.hero.atack(by))

    def hero_mana_down(self):
        mana_cost = self.hero.get_current_spell().get_mana_cost()
        self.hero.set_mana(
            self.hero.get_mana() - mana_cost)

    def hero_attack_result(self, by):

        if by == "weapon":
            name = self.hero.get_current_weapon().get_name()
        elif by == "magic":
            name = self.hero.get_current_spell().get_name()

        damage = self.hero.atack(by)
        e_health = self.enemy.get_health()

        if by == "weapon":
            return FightMessages.WEAPON_ATTACK.format(name, damage, e_health)
        elif by == "magic":
            return FightMessages.SPELL_ATTACK.format(name, damage, e_health)

    def is_enemy_dead(self, enemy):
        if not self.enemy.is_alive():
            return True
        return False

    def enemy_atack(self, by):
        pass

    def enemy_move(self, direction):
        pass

    def is_Fight(self):
        pass

    @staticmethod
    def test():
        h = Hero(name="rado", title="killer")
        w = Weapon("gun", 10)
        h.set_weapons(w)
        h.equip(w)

        s = Spell("anatema", 20, 10, 2)
        h.set_spells(s)
        h.learn(s)
        e = Enemy(100, 50, 10)
        f = Fight(h, e)
        print(f.hero_attack(by="weapon"))

if __name__ == '__main__':
    Fight.test()
