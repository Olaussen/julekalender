from collections import defaultdict, deque

def read_data():
    with open('./data/luke23.txt') as f:
        return {(i, j) for i, line in enumerate(f) for j, c in enumerate(line) if c == '#'}

def ground_tiles(elves):
    r1, r2 = min(r for (r,_) in elves), max(r for (r,_) in elves)
    c1, c2 = min(c for (_,c) in elves), max(c for (_,c) in elves)
    return sum(1 for r in range(r1,r2+1) for c in range(c1,c2+1) if (r,c) not in elves)

DIRS = ["N", "S", "W", "E"]

def perform(rounds = 0, part1=True):
    elves = read_data()
    directions = deque(DIRS)

    for i in range(rounds if part1 else 10000000):
        any_moved = False
        props = defaultdict(list)
        for elf in elves:
            neighbor = False
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if (dx, dy) != (0, 0) and (elf[0] + dx, elf[1] + dy) in elves:
                        neighbor = True
            if not neighbor:
                continue
            
            moved = False
            for dir in directions:
                if dir == "N" and not moved and (elf[0] - 1, elf[1]) not in elves and (elf[0] - 1, elf[1] - 1) not in elves and (elf[0] - 1, elf[1] + 1) not in elves:
                    props[elf[0]-1, elf[1]].append(elf)
                    moved = True
                elif dir == "S" and not moved and (elf[0] + 1, elf[1]) not in elves and (elf[0] + 1, elf[1] - 1) not in elves and (elf[0] + 1, elf[1] + 1) not in elves:
                    props[elf[0]+1, elf[1]].append(elf)
                    moved = True
                elif dir == "W" and not moved and (elf[0], elf[1] - 1) not in elves and (elf[0] - 1, elf[1] - 1) not in elves and (elf[0] + 1, elf[1] - 1) not in elves:
                    props[elf[0], elf[1]-1].append(elf)
                    moved = True
                elif dir == "E" and not moved and (elf[0], elf[1] + 1) not in elves and (elf[0] - 1, elf[1] + 1) not in elves and (elf[0] + 1, elf[1] + 1) not in elves:
                    props[elf[0], elf[1]+1].append(elf)
                    moved = True

        directions.rotate(-1)
        for key, value in props.items():
            if len(value) == 1:
                any_moved = True
                elves.discard(value[0])
                elves.add(key)

        if not any_moved:
            return i + 1

    if part1:
        return ground_tiles(elves)

def part1():
    print("Part 1:", perform(rounds=10))

def part2():
    print("Part 2:", perform(part1=False))

if __name__ == '__main__':
    part1()
    part2()