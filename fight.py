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

    def start_a_fight(self, by):
        print(FightMessages.START.format(self.hero, self.enemy))
        self.hero_attack(by)
        while (not self.is_enemy_dead(self.enemy)):
            self.hero_attack(by)
            if(not self.is_enemy_dead(self.enemy)):
                self.enemy_attack

    def hero_attack(self, by):
        if by == "weapon":
            self.enemy_health_down(by)
            print(self.hero_attack_result(by))
            if self.is_enemy_dead(self.enemy):
                print(FightMessages.ENEMY_IS_DEAD)
        # TODO : ADD range  logic
        elif by == "magic" and self.hero.can_cast(self.hero.get_current_spell()):
            self.enemy_health_down("magic")
            self.hero_mana_down()
            print(self.hero_attack_result(by))

    def enemy_health_down(self, by):
        self.enemy.set_health(
            self.enemy.get_health() - self.hero.attack(by))

    def hero_health_down(self):
        pass


    def hero_mana_down(self):
        mana_cost = self.hero.get_current_spell().get_mana_cost()
        self.hero.set_mana(
            self.hero.get_mana() - mana_cost)

    def hero_attack_result(self, by):

        if by == "weapon":
            name = self.hero.get_current_weapon().get_name()
        elif by == "magic":
            name = self.hero.get_current_spell().get_name()

        damage = self.hero.attack(by)
        e_health = self.enemy.get_health()

        if by == "weapon":
            return FightMessages.WEAPON_ATTACK.format(name, damage, e_health)
        elif by == "magic":
            return FightMessages.SPELL_ATTACK.format(name, damage, e_health)

    def is_enemy_dead(self, enemy):
        if self.enemy.is_alive():
            return False
        return True

    def enemy_attack(self):
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
        print(f.hero_attack(by="magic"))

if __name__ == '__main__':
    Fight.test()
