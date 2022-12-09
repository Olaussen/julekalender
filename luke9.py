def read_data():
    with open("./data/luke9.txt") as f:
            return f.read().splitlines()

class Coords(tuple):
    def __add__(self, other):
        return Coords(a + b for a, b in zip(self, other))

    def __sub__(self, other):
        return Coords(a - b for a, b in zip(self, other))

DIRS = {
    "R": Coords((1, 0)),
    "L": Coords((-1, 0)),
    "U": Coords((0, 1)),
    "D": Coords((0, -1)),
}

def move(head, tail):
    diff = Coords(min(1, max(-1, x)) for x in head - tail)
    return tail if head - tail == diff else tail + diff

def part1():
    head = tail = Coords((0, 0))
    positions = set()

    for line in read_data():
        dir, step = line.split()
        for _ in range(int(step)):
            head += DIRS[dir]
            tail = move(head, tail)
            positions.add(tail)
    print("Part 1:", len(positions))


def part2():
    rope = [Coords((0, 0))] * 10
    positions = set()

    for line in read_data():
        dir, step = line.split()
        for _ in range(int(step)):
            rope[0] += DIRS[dir]
            rope[1:] = [move(rope[i], rope[i + 1]) for i in range(len(rope) - 1)]
            positions.add(rope[9])
    print("Part 2:", len(positions))

if __name__ == "__main__":
    part1()
    part2()