from collections import defaultdict
from math import prod

def parse_monkey(lines):
    return {
        "items": [int(x) for x in lines[1][18:].split(",")],
        "operation": lambda old: eval(lines[2][19:]),
        "test": lambda x: x % int(lines[3][21:]) == 0,
        "testvalue": int(lines[3][21:]),
        "throw": {
            True: int(lines[4][29:]),
            False: int(lines[5][30:]),
        },
    }

def read_data():
    with open("./data/luke11.txt") as f:
        return [parse_monkey(m.splitlines()) for m in f.read().split("\n\n")]

def perform_rounds(monkeys, worry = False, rounds=20):
    counter = defaultdict(int)
    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            for item in monkey["items"]:
                counter[i] += 1
                new = monkey["operation"](item) // 3 if not worry else monkey["operation"](item) % prod(m["testvalue"] for m in monkeys)
                monkeys[monkey["throw"][monkey["test"](new)]]["items"].append(new)
            monkey["items"] = []
    return counter

def part1():
    print("Part1:", prod(sorted(perform_rounds(read_data()).values(), reverse=True)[:2]))

def part2():
    print("Part2:", prod(sorted(perform_rounds(read_data(), True, 10000).values(), reverse=True)[:2]))

if __name__ == "__main__":
    part1()
    part2()