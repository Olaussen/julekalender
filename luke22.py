import re

def read_data():
    with open("./data/luke22.txt") as f:
        map, instructions = f.read().split("\n\n")
        map = {(i, j): cell for i, row in enumerate(map.splitlines()) for j, cell in enumerate(row) if cell != " "}
        return map, re.split(r"(?<=\d)(?=[LR])|(?<=[LR])(?=\d)", instructions)

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def add_tuples(a, b):
    return tuple(x + y for x, y in zip(a, b))

def part1_move(map, dir, column, row, max_column, max_row):
    new_column, new_row = column, row
    while True:
        new_column, new_row = add_tuples((new_column, new_row), DIRS[dir])
        new_column %= max_column
        new_row %= max_row
        if (new_column, new_row) in map:
            break
    return (-1, column, row) if map[new_column, new_row] == "#" else (-1, new_column, new_row)

def part2_move(map, dir, column, row):
    new_dir, new_column, new_row = dir, *add_tuples((column, row), DIRS[dir])

    match new_dir, new_column, new_row:
        case 0, _, 150 if new_column in range(50):
            new_dir, new_column, new_row = 2, 149 - new_column, 99
        case 0, _, 100 if new_column in range(50, 100):
            new_dir, new_column, new_row = 3, 49, 50 + new_column
        case 0, _, 100 if new_column in range(100, 150):
            new_dir, new_column, new_row = 2, 149 - new_column, 149
        case 0, _, 50 if new_column in range(150, 200):
            new_dir, new_column, new_row = 3, 149, new_column - 100

        case 1, 200, _ if new_row in range(50):
            new_dir, new_column, new_row = 1, 0, new_row + 100
        case 1, 150, _ if new_row in range(50, 100):
            new_dir, new_column, new_row = 2, new_row + 100, 49
        case 1, 50, _ if new_row in range(100, 150):
            new_dir, new_column, new_row = 2, new_row - 50, 99

        case 2, _, 49 if new_column in range(0, 50):
            new_dir, new_column, new_row = 0, 149 - new_column, 0
        case 2, _, 49 if new_column in range(50, 100):
            new_dir, new_column, new_row = 1, 100, new_column - 50
        case 2, _, -1 if new_column in range(100, 150):
            new_dir, new_column, new_row = 0, 149 - new_column, 50
        case 2, _, -1 if new_column in range(150, 200):
            new_dir, new_column, new_row = 1, 0, new_column - 100

        case 3, 99, _ if new_row in range(50):
            new_dir, new_column, new_row = 0, 50 + new_row, 50
        case 3, -1, _ if new_row in range(50, 100):
            new_dir, new_column, new_row = 0, new_row + 100, 0
        case 3, -1, _ if new_row in range(100, 150):
            new_dir, new_column, new_row = 3, 199, new_row - 100

    return (new_dir, new_column, new_row) if map[new_column, new_row] == "." else (dir, column, row)

def move(map, dir, column, row, max_column, max_row, part1):
    if part1:
        return part1_move(map, dir, column, row, max_column, max_row)
    return part2_move(map, dir, column, row)

def perform(part1):
    map, instructions = read_data()
    max_column = max(x for x, _ in map) + 1
    max_row = max(y for _, y in map) + 1
    dir, column, row = 0, 0, next(y for y in range(max_row) if (0, y) in map)

    for inst in instructions:
        if inst == "R":
            dir = (dir + 1) % 4
        elif inst == "L":
            dir = (dir - 1) % 4
        else:
            for _ in range(int(inst)):
                new_dir, column, row = move(map, dir, column, row, max_column, max_row, part1)
                if not part1:
                    dir = new_dir
    
    return (column + 1) * 1000 + (row + 1) * 4 + dir

def part1():
    print("Part 1:", perform(True))

def part2():
    print("Part 2:", perform(False))

if __name__ == "__main__":
    part1()
    part2()