class Hero:

    def __init__(self, name, title, health, mana, mana_regeneration_rate):

        self.__name = name
        self.__title = title
        self.__health = health
        self.__mana = mana
        self.__mana_regeneration_rate = mana_regeneration_rate

        self.__maximumHealth = health
        self.__maximumMana = mana

    def get_name(self):
        return self.__name

    def get_title(self):
        return self.__title

    def get_maximumHealth(self):
        return self.__maximumHealth

    def get_maximumMana(self):
        return self.__maximumMana

    def known_as(self):
        return "{0} the {1}".format(self.get_name(), self.get_title())

    def is_alive(self):
        return bool(self.__health)

    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana

    def get_mana_regeneration_rate(self):
        return self.__mana_regeneration_rate

    def can_cast(self):
        pass

    def set_health(self, newPoints):
        self.__health = newPoints

    def set_mana(self, newPoints):
        self.__mana = newPoints

    def take_damage(self, damage_points):
        bloodLeft = self.get_health() - damage_points

        if(bloodLeft <= 0):
            self.set_health(0)
            return
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

    def move_hero(self, direction):
        self.take_mana(self.get_mana_regeneration_rate())

        if (direction == "up"):
            pass
        elif (direction == "down"):
            pass
        elif (direction == "left"):
            pass
        elif(direction == "right"):
            pass
        else:
            print("Error in direction!")


h = Hero(name="Bron", title="Dragonslayer", health=100,
         mana=100, mana_regeneration_rate=2)

# print(h.known_as())
# print(h.is_alive())
# print(h.get_health())
# print(h.get_mana())
# h.take_damage(50)
# print(h.get_health())
# h.take_damage(100)
# print(h.get_health())
# print(h.is_alive())
# h.set_mana(50)
# h.move_hero("left")
# h.move_hero("right")
# print(h.get_mana())
