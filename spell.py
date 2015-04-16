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

# Simply test
    @staticmethod
    def test():
        magic = Spell("m", 50, 10, 2)
        print(magic.get_damage() == 50)
        print(magic.get_name() == "m")
        magic1 = Spell("m", 4, 10, 2)
        magic2 = Spell("m", 7, 10, 2)
        magic3 = Spell("m", 8, 10, 2)
        magics = [magic1, magic2, magic3]
        print(int(magic) > int(magic3))
        for m in magics:
            print(m)

if __name__ == '__main__':
    Spell.test()
