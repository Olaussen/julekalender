from collections import deque

DIRS = [
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, -1),
    (0, -1, 0),
    (-1, 0, 0),
]

def read_data():
    with open("./data/luke18.txt") as f:
      return {tuple(map(int, line.split(","))):0 for line in f}

def part1():
    data = read_data()
    sides = len(data) * 6
    for cube in data:
        for dir in DIRS:
            if tuple(x + y for x, y in zip(cube, dir)) in data:
                sides -= 1
                
    print("Part 1:", sides)

def part2(): 
    data = read_data()
    min_c, max_c = tuple(min(x) - 1 for x in zip(*data)), tuple(max(x) + 1 for x in zip(*data))

    queue = deque([min_c])
    visited = set()

    while len(queue) > 0:
        cube = queue.pop()
        if cube in visited:
            continue
        visited.add(cube)

        for dir in DIRS:
            checked = tuple(x + y for x, y in zip(cube, dir))
            if all(a <= b <= c for a, b, c in zip(min_c, checked, max_c)):
                if checked in data:
                    data[checked] += 1
                    continue
                queue.append(checked)
                
    print("Part 2:", sum(data.values()))

if __name__ == "__main__":
    part1()
    part2()