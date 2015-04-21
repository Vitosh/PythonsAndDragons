import matrix as m
from fight import *
from hero_person_and_weapons import *

ENEMY = "E"
HERO = "H"
TREASURE = "T"
SPAWN = "S"
GATEWAY = "G"
NEGHBORS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Dungeon:

    # take one hero and list of enemys

    def __init__(self, hero, enemys):
        self.__hero = hero
        self.__enemys = enemys
        self.__enemys_coordinate = self.__init_enemy_in_map()
        self.__matrix = m.file_to_matrix("Map.txt")
        self.__fights_l = []
        self.__all_enemys = []
        self.__all_treasures = m.find_all_coordinates(self.__matrix, TREASURE)

    def __init_enemy_in_map(self):
        enemys_d = {}
        self.__all_enemys = m.find_all_coordinates(self.__matrix, ENEMY)
        for enemy in self.__enemys:
            for coordinate in self.__enemys:
                enemys_d[enemy] = (enemy, coordinate)
        return enemys_d

    def print_map(self):
        print(m.matrix_view(self.__matrix))

    def spawn(self):
        str_map = m.matrix_view(self.__matrix)
        self.__matrix = str_map.replace(SPAWN, HERO)

    # return tuple with new position hero
    def move_hero(self, direction):
        hero_position = m.find_element_in_matrix(self.__matrix, HERO)
        new_hero_position = m.move_in_matrix(
            self.__matrix, hero_position, direction)
        if new_hero_position != hero_position:
            regeneration = self.__hero.get_mana_regeneration_rate()
            self.__hero.take_mana(regeneration)
        return new_hero_position

    # take enemy object and direction
    def move_enemy(self, enemy, direction):
        enemy_position = self.__enemys_coordinate[enemy][1]
        new_enemy_position = m.move_in_matrix(
            self.__matrix, enemy_position, direction)
        self.__enemys_coordinate[enemy] = (enemy, new_enemy_position)

    def is_treasure_found(self):
        hero_position = m.find_element_in_matrix(self.__matrix, HERO)
        return hero_position in self.__all_treasures

    def enemy_found(self):
        self.__fights_l.clear()
        hero_position = m.find_element_in_matrix(self.__matrix, HERO)
        self.__all_enemys = m.find_all_coordinates(self.__matrix, ENEMY)
        x_h, y_h = hero_position
        for coordinate in NEGHBORS:
            x, y = coordinate
            if (x_h + x, y_h + y) in self.__all_enemys:
                self.__fights_l.append((x_h + x, y_h + y))

    def view_enemy_to_fight(self):
        return "\n".join(str(enemy) for enemy in self.__fights_l)

    def select_enemy_to_fight(self, enemy):
        if enemy in self.__fights_l:
            return Fight(self.__hero, enemy)
        return False  # Create Exception

    # I will write after Tresure class is done
    def add_treasure_in_hero(self):
        if self.__is_treasure_found:
            pass
        pass
