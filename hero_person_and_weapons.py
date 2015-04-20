class Person:

    def __init__(self, health, mana):
        self.__health = health
        self.__mana = mana

    def is_alive(self):
        return bool(self.__health)

    def can_cast(self, magic):
        return self.get_mana() > magic.get_mana_cost()

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def set_health(self, newPoints):
        self.__health = newPoints

    def set_mana(self, newPoints):
        self.__mana = newPoints

    def take_mana(self, mana_points):
        manaToBeAdded = mana_points + self.get_mana()
        if (manaToBeAdded > self.get_maximumMana()):
            manaToBeAdded = self.get_maximumMana()

    def take_healing(self, healing_points):
        if not (self.is_alive()):
            return False

        bloodToBeAdded = healing_points + self.get_health()
        if (bloodToBeAdded > self.get_maximumHealth()):
            bloodToBeAdded = self.get_maximumHealth()

        self.set_health(bloodToBeAdded)
        return True


class Hero(Person):

    def __init__(self, name, title, health=100, mana=100, mana_regeneration_rate=1):

        super().__init__(health, mana)
        self.__name = name
        self.__title = title
        self.__health = health
        self.__mana = super().get_mana()
        self.__mana_regeneration_rate = mana_regeneration_rate

        self.__spells = set()
        self.__weapons = set()

        self.__current_weapon = 0
        self.__current_spell = 0
        self.__maximumHealth = health
        self.__maximumMana = mana
        self.__heroSign = "H"

    def __repr__(self):
        return "health : {} , Mana :{}".format(self.get_health(), self.get_mana())

    def set_weapons(self, weapon):
        self.__weapons.add(weapon)

    def set_spells(self, spell):
        self.__spells.add(spell)

    def equip(self, weapon):
        if weapon in self.get_weapons():
            self.__current_weapon = weapon

    def learn(self, spell):
        if spell in self.get_spells():
            self.__current_spell = spell

    def get_weapons(self):
        return self.__weapons

    def get_spells(self):
        return self.__spells

    def get_name(self):
        return self.__name

    def get_title(self):
        return self.__title

    def get_maximumHealth(self):
        return self.__maximumHealth

    def get_maximumMana(self):
        return self.__maximumMana

    def known_as(self):
        return "{} the {}".format(self.get_name(), self.get_title())

    def get_mana_regeneration_rate(self):
        return self.__mana_regeneration_rate

    def take_damage(self, damage_points):
        bloodLeft = self.get_health() - damage_points

        if(bloodLeft <= 0):
            self.set_health(0)

        self.set_health(bloodLeft)

    def take_healing(self, healing_points):
        if not (self.is_alive()):
            return False

        bloodToBeAdded = healing_points + self.get_health()
        if (bloodToBeAdded > self.get_maximumHealth()):
            bloodToBeAdded = self.get_maximumHealth()

        self.set_health(bloodToBeAdded)

        return True

    def take_mana(self, mana_points):
        manaToBeAdded = mana_points + self.get_mana()
        if (manaToBeAdded > self.get_maximumMana()):
            manaToBeAdded = self.get_maximumMana()

        self.set_mana(manaToBeAdded)

    def get_current_weapon(self):
        return self.__current_weapon

    def get_current_spell(self):
        return self.__current_spell

    def get_hero_name(self):
        return self.__name

    def get_hero_title(self):
        return self.__title

    def move_hero(self, direction):
        self.take_mana(self.get_mana_regeneration_rate())

    def atack(self, by):
        if by == "weapon" and self.get_current_weapon() != 0:
            return self.get_current_weapon().get_damage()
        elif by == "magic" and self.get_current_weapon != 0:
            if self.get_mana() >= self.get_current_spell().get_mana_cost():
                self.__mana -= self.get_current_spell().get_mana_cost()
                return self.get_current_spell().get_damage()
        else:
            return 0


class Weapon:

    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage

    def __str__(self):
        return "{}-{}".format(self.get_name(), self.get_damage())

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.get_name() + str(self.get_damage))

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage


class Spell:

    def __init__(self, name, damage, mana_cost, cast_range):
        self.__name = name
        self.__damage = damage
        self.__mana_cost = mana_cost
        self.__cast_range = cast_range

    def __str__(self):
        cost_str = str(self.get_mana_cost())
        range_str = str(self.get_cast_range())

        return "name: {}\ndamage: {}\ncost: {}\nrange: {}\n".format(self.get_name(), self.get_damage(), cost_str, range_str)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.__str__())

    def __int__(self):
        return self.get_damage()

    def get_name(self):
        return self.__name

    def get_damage(self):
        return self.__damage

    def get_mana_cost(self):
        return self.__mana_cost

    def get_cast_range(self):
        return self.__cast_range


class Enemy(Person):

    def __init__(self, health, mana, damage):
        super().__init__(health, mana)
        self.__health = super().get_health()
        self.__mana = super().get_mana()
        self.__damage = damage
        self.__weapon = 0
        self.__spell = 0
        self.__mana = super().get_mana()

    def __repr__(self):
        return "health : {} , Mana :{}".format(self.get_health(), self.get_mana())

    def get_weapon(self):
        return self.__weapon

    def get_spell(self):
        return self.__spell

    def equip(self, weapon):
        if isinstance(weapon, Weapon):
            self.__weapon = weapon
        # raise ->weapon Error

    def learn(self, spell):
        if isinstance(spell, Spell):
            self.__spell = spell
        # raise ->spell Error

    def atack(self, by=False):
        if not by:
            return self.__damage
        if by == "weapon":
            return self.__weapon.get_damage()
        elif by == "magic" and self.__mana >= self.__spell.get_mana_cost():
            self.__mana -= self.__spell.get_mana_cost()
            return self.__spell.get_damage()
        return 0
