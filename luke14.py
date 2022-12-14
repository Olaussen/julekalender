from itertools import count, product

def read_data():
    with open("./data/luke14.txt") as f:
        return f.read().splitlines()

def fill_rocks():
    rocks = set()
    for line in read_data():
        rock = line.split(" -> ")
        for i in range(len(rock) - 1):
            x1, y1 = rock[i].split(",")
            rocks.add((int(x1), int(y1)))
            x2, y2 = rock[i + 1].split(",")
            rocks.add((int(x2), int(y2)))
            if x1 == x2:
                for y in range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1):
                    rocks.add((int(x1), y))
                continue
            for x in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1):
                rocks.add((x, int(y1)))
    return rocks
    
def adjacent(x, y):
    return (x, y + 1), (x - 1, y + 1), (x + 1, y + 1)

def pour_sand(part2 = False):
    rocks = fill_rocks()
    lowest_rock = max(y for _, y in rocks)
    for i in count():
        current = 500, 0
        while current[1] < lowest_rock or part2:
            try:
                current = next(x for x in adjacent(*current) if x not in rocks and x[1] < lowest_rock + 2) \
                    if part2 else next(x for x in adjacent(*current) if x not in rocks)
            except StopIteration:
                break
        else:
            if not part2:
                return i
                
        if part2 and current == (500, 0):
            return i + 1

        rocks.add(current)

def part1():
    print("Part 1:", pour_sand())

def part2():
    print("Part 2:", pour_sand(True))

if __name__ == "__main__":
    part1()
    part2()
