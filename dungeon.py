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

    # take one hero and list of enemies

    def __init__(self, hero, enemies):
        self.__matrix = m.file_to_matrix("Map.txt")
        self.__hero = hero
        self.__enemies = enemies
        self.__enemies_coordinate = self.__init_enemy_in_map()
        self.__fights_l = []
        self.__all_enemies = []
        self.__all_treasures = m.find_all_coordinates(self.__matrix, TREASURE)
        self.__all_gateways = m.find_all_coordinates(self.__matrix, GATEWAY)

    def __init_enemy_in_map(self):
        enemies_d = {}
        added = set()
        self.__all_enemies = m.find_all_coordinates(self.__matrix, ENEMY)
        # TODO : if self.__enemies < self.__all_enemies random enimies in map
        if len(self.__enemies) == 1:
            for coordinate in self.__all_enemies:
                enemies_d[coordinate] = (enemy, coordinate)
        else:
            for enemy in self.__enemies:
                for coordinate in self.__all_enemies:
                    if coordinate not in added:
                        enemies_d[coordinate] = (enemy, coordinate)
                        added.add(coordinate)
                        break
        return enemies_d

    def print_map(self):
        print(m.matrix_view(self.__matrix))

    def spawn(self):
        positon = m.find_element_in_matrix(self.__matrix, SPAWN)
        x, y = positon
        self.__matrix[x][y] = HERO

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
    def move_enemy(self, s_coordinate, direction):
        enemy_position = self.__enemies_coordinate[s_coordinate][1]
        new_enemy_position = m.move_in_matrix(
            self.__matrix, enemy_position, direction)
        self.__enemies_coordinate[s_coordinate] = (
            s_coordinate, new_enemy_position)

    def is_treasure_found(self):
        hero_position = m.find_element_in_matrix(self.__matrix, HERO)
        return hero_position in self.__all_treasures

    # if is True "Player Win"
    def is_gateway_found(self):
        hero_position = m.find_element_in_matrix(self.__matrix, HERO)
        return hero_position in self.__all_gateways

    def enemy_found(self):
        self.__fights_l.clear()
        hero_position = m.find_element_in_matrix(self.__matrix, HERO)
        self.__all_enemies = m.find_all_coordinates(self.__matrix, ENEMY)
        x_h, y_h = hero_position
        for coordinate in NEGHBORS:
            x, y = coordinate
            for v in self.__enemies_coordinate.values():
                if v[1] == (x_h + x, y_h + y):
                    self.__fights_l.append(v[0])

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


def main():
    h = Hero(name="rado", title="killer")
    w = Weapon("gun", 10)
    h.set_weapons(w)
    h.equip(w)
    e = Enemy(100, 50, 10)
    e2 = Enemy(40, 20, 10)
    e3 = Enemy(40, 2, 10)
    e4 = Enemy(40, 2, 10)
    e5 = Enemy(40, 2, 10)
    e6 = Enemy(40, 2, 10)
    map_d = Dungeon(h, [e, e2, e3, e4, e5, e6])
    map_d.print_map()
    map_d.spawn()
    map_d.print_map()
    map_d.move_hero("right")
    map_d.print_map()
    map_d.move_hero("down")
    map_d.print_map()
    map_d.move_hero("right")
    map_d.print_map()
    map_d.enemy_found()
    print(map_d.view_enemy_to_fight())
    print(map_d.select_enemy_to_fight(e2))


if __name__ == '__main__':
    main()
