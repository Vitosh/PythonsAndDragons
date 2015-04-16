class Hero:

    def __init__(self, hero_name, hero_title, weapons, spells, health=100, mana=100, mana_regeneration_rate=1):
        self.__name = hero_name
        self.__title = hero_title
        self.__health = health
        self.__mana = mana
        self.__mana_regeneration_rate = mana_regeneration_rate
        # Each hero can have  a lot of weapons and spells, but can equip one
        # weapon and one spell class
        self.__spells = set(spells)
        self.__weapons = set(weapons)
        self.__current_weapon = None
        self.__current_spell = None
        self.__max_health = health
        self.__max_mana = mana

    def get_weapons(self):
        return self.__weapons

    def get_spells(self):
        return self.__spells

    def get_hero_name(self):
        return self.__name

    def get_hero_title(self):
        return self.__title

    def known_as(self):
        return "{} the {}".format(self.get_hero_name(), self.get_hero_title())

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def is_alive(self):
        return self.get_health() > 0

    def can_cast(self):
        return self.get_mana() > 0

    def take_damage(self, damage_point):
        self.__health -= damage_point
        return self.get_health()

    def take_healing(self, healing_points):

        # Hero is dead logic or Hero health  is  max_health%
        if not self.is_alive() or self.get_health() == self.__max_health or not self.is_alive() or healing_points < 0:
            return False

        # Other cases
        self.__health += healing_points
        return self.get_health()

    # take mana regeneration logic

    def is_mana_point_over_max(self, points):
        if self.__mana + points > self.__max_mana:
            return True
        return False

    def regeneration(self, is_move):
        # Hero make move => is_move = True
        if is_move:
            self.__mana += self.__mana_regeneration_rate
            # Hero's mana cannot go above the start mana given to him,
            # neither he can go down below 0 mana
            if self.is_mana_point_over_max(self.__mana_regeneration_rate):
                self.__mana = self.__max_mana
        # valid if  is_move = True or is_move = False
        # always return mana
        return self.get_mana()

    def take_mana(self, mana_points):
        if self.is_mana_point_over_max(mana_points):
            self.__mana = self.__max_mana
        self.__mana += mana_points
        return self.get_mana()

    def equip(self, weapon):
        if weapon in self.get_weapons():
            self.__current_weapon = weapon
        # In all other cases return Exception
        # TODO : Make equip exception ("This weapon not in hero inventory")

    def learn(self, spell):
        if spell in self.get_spells():
            self.__current_spell = spell
        # TODO : Make learn exception ("This spell not in hero inventory")

    # This method get Weapon or Spell object
    def atack(self, by):
        return by.get_damage()

    def get_current_weapon(self):
        return self.__current_weapon

    def get_current_spell(self):
        return self.__current_spell
