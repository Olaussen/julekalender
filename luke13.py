from math import prod

def read_data1():
    with open("./data/luke13.txt") as f:
        return [[eval(x) for x in pair.splitlines()] for pair in f.read().split("\n\n")]

def read_data2():
    with open("./data/luke13.txt") as f:
        return [eval(x) for x in f.read().splitlines() if len(x) > 0]

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a - b

    if isinstance(a, list) and isinstance(b, list):
        for x, y in zip(a, b):
            if result := compare(x, y):
                return result
        return len(a) - len(b)

    if isinstance(a, list):
        return compare(a, [b])

    if isinstance(b, list):
        return  compare([a], b)

class Comparer:
    def __init__(self, x):
        self.x = x

    def __lt__(self, other):
        return compare(self.x, other.x) < 0

    def __eq__(self, other):
        return compare(self.x, other.x) == 0

def part1():
    print("Part 1:", sum(i + 1 for i, (a, b) in enumerate(read_data1()) if compare(a, b) < 0))

def part2():
    dividers = [[2]], [[6]]
    print("Part 2:", prod(sorted([*read_data2(), *dividers], key=Comparer).index(x) + 1 for x in dividers))

if __name__ == "__main__":
    part1()
    part2()
