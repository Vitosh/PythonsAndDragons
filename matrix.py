DIRECTIONS = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
OBSTACLE = "#"
WALCABLE_PATH = "."


def file_to_matrix(path):
    matrix = []
    with open(path, "r") as f:
        contents = f.read().split("\n")
        matrix = [list(line) for line in contents]

    return matrix


def find_element_in_matrix(matrix, element):
    row_count = -1

    for row in matrix:
        row_count += 1
        found = -1
        try:
            found = row.index(element)
        except ValueError:
            pass
        if found != -1:
            return (row_count, found)
    return False


def find_all_coordinates(matrix, sign):
    coordinate = []
    row_count = -1
    for row in matrix:
        row_count += 1
        for i in range(len(row)):
            if row[i] == sign:
                coordinate.append((row_count, i))
    return coordinate


# Take matrix, element coordinate, and direction


def move_in_matrix(matrix, element_p, direction):
    # unpacking
    x, y = DIRECTIONS[direction]
    x_c, y_c = element_p

    try:
        if matrix[x_c + x][y_c + y] != OBSTACLE:
            matrix[x_c + x][y_c + y] = matrix[x_c][y_c]
            matrix[x_c][y_c] = WALCABLE_PATH
    except IndexError:
        return (x_c, y_c)

    return (x_c + x, y_c + y)


def matrix_view(matrix):
    remove_e = ["[", "]", ",", " ", "'"]
    matrix_to_str = "\n".join([str(c) for c in matrix])
    for e in remove_e:
        matrix_to_str = matrix_to_str.replace(e, "")
    return matrix_to_str + "\n"


def main():
    matrix = file_to_matrix("Map.txt")
    print(find_all_coordinates(matrix, "E"))
    print(find_all_coordinates(matrix, "T"))
    print(matrix_view(matrix))
    position = move_in_matrix(matrix, (2, 5), "up")
    print(matrix_view(matrix))
    position = move_in_matrix(matrix, position, "up")
    print(matrix_view(matrix))
    position = move_in_matrix(matrix, position, "up")
    print(matrix_view(matrix))


if __name__ == '__main__':
    main()
