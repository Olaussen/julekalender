
from itertools import cycle

DIRS = {">": 1, "<": -1}

def read_data():
    with open("./data/luke17.txt") as f:
      return cycle(enumerate([DIRS[x] for x in f.read().strip()]))
      
ROCKS = [
    {0 + 0j, 1 + 0j, 2 + 0j, 3 + 0j},
    {1 + 2j, 0 + 1j, 1 + 1j, 2 + 1j, 1 + 0j},
    {2 + 2j, 2 + 1j, 0 + 0j, 1 + 0j, 2 + 0j},
    {0 + 3j, 0 + 2j, 0 + 1j, 0 + 0j},
    {0 + 0j, 0 + 1j, 1 + 0j, 1 + 1j},
]

def highest(grid):
    return int(max(p.imag for p in grid))

def perform(timestep):
    data = read_data()
    floor = set(x - 1j for x in range(7))
    falling_rocks = cycle(enumerate(ROCKS))
    last = {}

    while timestep > 0:
        start = 2 + (4 + highest(floor)) * 1j
        rock_index, rock = next(falling_rocks)
        rock = {start + part for part in rock}

        while True:
            wind_index, next_wind = next(data)
            new_rock = {part + next_wind for part in rock}
            if not new_rock & floor and all(0 <= p.real <= 6 for p in new_rock):
                rock = new_rock

            new_rock = {part - 1j for part in rock}
            if floor & new_rock:
                floor.update(rock)
                break

            rock = new_rock

        max_y = highest(floor)
        heights = tuple(max_y - highest(part for part in floor if part.real == i) for i in range(7))
        timestep -= 1

        try:
            old_t, old_max_y = last[rock_index, wind_index, heights]
            floor = {part + timestep // (old_t - timestep) * (max_y - old_max_y) * 1j for part in floor}
            timestep %= old_t - timestep
        except KeyError:
            last[rock_index, wind_index, heights] = timestep, max_y

    return highest(floor) + 1

def part1():
    print("Part 1:", perform(2022))

def part2(): 
    print("Part 2:", perform(1000000000000))

if __name__ == "__main__":
    part1()
    part2()