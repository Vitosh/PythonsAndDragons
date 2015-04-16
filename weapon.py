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


# Simply test
    @staticmethod
    def test():
        gun = Weapon("gun", 50)
        print(gun.get_damage() == 50)
        print(gun.get_name() == "gun")
        gun1 = Weapon("gun2", 20)
        gun2 = Weapon("gun3", 10)
        print([gun, gun1, gun2])

if __name__ == '__main__':
    Weapon.test()
