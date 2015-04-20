from hero_person_and_weapons import *
from fight import *


class Map():  # inherits Fight

    def __init__(self, hero, enemy):

        self.__chars = []
        self.__listOfEnemies = []
        self.__listOfHealingPotions = []
        self.__listOfObstacles = []

        self.__x = 0
        self.__y = 0

        self.__sign = 'H'
        self.__enemy_s = 'E'
        self.__obstable = '#'
        self.__gate = 'G'
        self.__treasure = 'T'
        self.__road = '.'

        self.__hero = hero
        self.__enemy = enemy
        self.__fight = Fight(self.__hero, self.__enemy)

    def __repr__(self):
        return self.__chars

    def show_x(self):
        return int(self.__x)

    def show_y(self):
        return int(self.__y)

    def show_list_map(self):
        return self.__chars

    def loadMap(self):
        myMap = open("Map.txt", 'rU')
        loadMapChars = []
        for line in myMap:
            loadMapLines = []
            for c in line:
                loadMapLines.extend([c])
            loadMapChars.extend([loadMapLines])

        for line in loadMapChars:
            for char in line:
                char.strip()
                if (char == "" or char == "\n"):
                    line.remove(char)

        for line in loadMapChars:
            xSetter = 0
            for char in line:
                xSetter += 1

        self.__chars = loadMapChars
        self.__y = len(self.__chars)
        self.__x = xSetter

    def show_line_map(self):
        firstLine = True
        sMap = ""
        for line in self.__chars:
            if not (firstLine):
                sMap += "\n"
            for char in line:
                firstLine = False
                sMap += char
        return sMap

    def find_item_in_nested_list(self, nestedList, item):
        for i in range(len(nestedList)):
            part = nestedList[i]
            for j in range(len(part)):
                if part[j] == item:
                    return (i, j)
        return "ERROR"

    def move_hero_on_map(self, direction):

        locationHero = self.find_item_in_nested_list(self.__chars, self.__sign)
        xHeroLocation = int(locationHero[1])
        yHeroLocation = int(locationHero[0])

        if (direction == "up"):

            if ((yHeroLocation - 1) <= 0):
                return

            elif (self.__chars[yHeroLocation - 1][xHeroLocation] == self.__enemy_s):
                print("ENEMY found! Start a fight! :)")
                print(self.__fight.hero_attack("weapon"))

            elif (self.__chars[yHeroLocation - 1][xHeroLocation] == self.__obstable):
                # When obstacle is found you shall not pass
                return

            elif (self.__chars[yHeroLocation - 1][xHeroLocation] == self.__gate):
                print("YOU WIN")

            self.__chars = [
                [subelt.replace(self.__sign, '_') for subelt in elt]for elt in self.__chars]
            self.__chars[yHeroLocation - 1][xHeroLocation] = self.__sign

        elif (direction == "down"):
            if (yHeroLocation + 1 >= self.show_y()):
                return

            elif (self.__chars[yHeroLocation + 1][xHeroLocation] == self.__enemy_s):
                print("ENEMY found! Start a fight! :)")
                print(self.__fight.hero_attack("weapon"))

            elif (self.__chars[yHeroLocation + 1][xHeroLocation] == self.__obstable):
                # When obstacle is found you shall not pass
                return

            elif (self.__chars[yHeroLocation + 1][xHeroLocation] == self.__gate):
                print("YOU WIN")

            self.__chars = [
                [subelt.replace(self.__sign, '_') for subelt in elt]for elt in self.__chars]
            self.__chars[yHeroLocation + 1][xHeroLocation] = self.__sign

        elif (direction == "left"):

            if (xHeroLocation - 1 <= 0):
                return

            elif (self.__chars[yHeroLocation][xHeroLocation - 1] == self.__enemy_s):
                print("ENEMY found! Start a fight! :)")
                print(self.__fight.hero_attack("weapon"))

            elif (self.__chars[yHeroLocation][xHeroLocation - 1] == self.__obstable):
                # When obstacle is found you shall not pass
                return

            elif (self.__chars[yHeroLocation][xHeroLocation - 1] == self.__gate):
                print("YOU WIN")

            self.__chars = [
                [subelt.replace(self.__sign, '_') for subelt in elt]for elt in self.__chars]
            self.__chars[yHeroLocation][xHeroLocation - 1] = self.__sign

        elif(direction == "right"):
            if (xHeroLocation + 1 >= self.show_x()):
                return

            elif (self.__chars[yHeroLocation][xHeroLocation + 1] == self.__enemy_s):
                print("ENEMY found! Start a fight! :)")
                print(self.__fight.hero_attack("weapon"))
                pass

            elif (self.__chars[yHeroLocation][xHeroLocation + 1] == self.__obstable):
                # When obstacle is found you shall not pass
                return

            elif (self.__chars[yHeroLocation][xHeroLocation + 1] == self.__gate):
                print("YOU WIN")

            self.__chars = [
                [subelt.replace(self.__sign, '_') for subelt in elt]for elt in self.__chars]
            self.__chars[yHeroLocation][xHeroLocation + 1] = self.__sign

    @staticmethod
    def test():
        h = Hero(name="rado", title="killer")
        w = Weapon("gun", 10)
        h.set_weapons(w)
        h.equip(w)
        e = Enemy(100, 50, 10)
        NewMap = Map(h, e)
        NewMap.loadMap()
        print(NewMap.move_hero_on_map("right"))
        print(NewMap.show_line_map())
        print(NewMap.move_hero_on_map("right"))
        print(NewMap.show_line_map())
        print(NewMap.move_hero_on_map("down"))
        print(NewMap.show_line_map())
        print(NewMap.move_hero_on_map("left"))


if __name__ == '__main__':
    Map.test()
