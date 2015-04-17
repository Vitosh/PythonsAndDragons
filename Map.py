class Map():

    def __init__(self):
        self.__chars = []
        self.__listOfEnemies = []
        self.__listOfHealingPotions = []
        self.__listOfObstacles = []

    def __repr__(self):
        return self.__chars

    def show_list_map(self):
        return self.__chars

    def loadMap(self):
        myMap = open("Map.txt", 'rU')
        loadMapChars = []
        for line in myMap:
            for c in line:
                loadMapChars.append(c)
        self.__chars = loadMapChars

    def __str__(self):
        value = str("".join(self.__chars))
        return value

    def move_hero_on_map(self, direction):
        locationHero = self.__chars.index('H')
        self.__chars[locationHero] = "?"

        print(locationHero)
        if (direction == "up"):
            pass
        elif (direction == "down"):
            # WORK HERE
            pass
        elif (direction == "left"):
            self.__chars[locationHero - 1] = "H"
        elif(direction == "right"):
            self.__chars[locationHero + 1] = 'H'
        else:
            print("Error in direction!")

NewMap = Map()
NewMap.loadMap()
print(NewMap)
NewMap.move_hero_on_map("right")
print(NewMap)
NewMap.move_hero_on_map("right")
print(NewMap)
NewMap.move_hero_on_map("left")
print(NewMap)
NewMap.move_hero_on_map("right")
print(NewMap)
NewMap.move_hero_on_map("right")
print(NewMap)
NewMap.move_hero_on_map("right")
print(NewMap)
NewMap.move_hero_on_map("right")
print(NewMap)
