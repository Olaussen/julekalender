import math
import re
from collections import deque

REGEX = r"^Blueprint (\w+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."

def read_data():
    with open("./data/luke19.txt") as f:
        return [{"id": int(id), "ore_ore": int(ore_ore), "clay_ore": int(clay_ore), "obsi_ore": int(obsi_ore), "obsi_clay": int(obsi_clay), "geode_ore": int(geode_ore), "geode_obsi": int(geode_obsi) } 
            for id, ore_ore, clay_ore, obsi_ore, obsi_clay, geode_ore, geode_obsi in  re.findall(REGEX, f.read(), re.MULTILINE)]


def evaluate(B, max_time):
    best = 0
    queue = deque([(0, 0, 0, 0, 1, 0, 0, 0, 0)])
    visited = set()

    ore_cap = max(B["ore_ore"], B["clay_ore"], B["obsi_ore"], B["geode_ore"])

    while queue:
        ore, clay, obsidian, geodes, ore_tick, clay_tick, obsidian_tick, geode_tick, tick = queue.popleft()

        if tick == max_time:
            best = max(best, geodes)
            continue

        ore_tick, clay_tick, obsidian_tick = min(ore_tick, ore_cap), min(clay_tick, B["obsi_clay"]), min(obsidian_tick, B["geode_obsi"])
        time_left = max_time - tick
        ore, clay, obsidian = min(ore, time_left * ore_cap - ore_tick * (time_left - 1)), min(clay, time_left * B["obsi_clay"] - clay_tick * (time_left - 1)), min(obsidian, time_left * B["geode_obsi"] - obsidian_tick * (time_left - 1))

        state = (ore, clay, obsidian, geodes, ore_tick, clay_tick, obsidian_tick, geode_tick, tick)
        if state in visited:
            continue
        visited.add(state)

        queue.append(
            (
                ore + ore_tick,
                clay + clay_tick,
                obsidian + obsidian_tick,
                geodes + geode_tick,
                ore_tick,
                clay_tick,
                obsidian_tick,
                geode_tick,
                tick + 1,
            )
        )

        if ore >= B["ore_ore"]:
            queue.append(
                (
                    ore + ore_tick - B["ore_ore"],
                    clay + clay_tick,
                    obsidian + obsidian_tick,
                    geodes + geode_tick,
                    ore_tick + 1,
                    clay_tick,
                    obsidian_tick,
                    geode_tick,
                    tick + 1,
                )
            )

        if ore >= B["clay_ore"]:
            queue.append(
                (
                    ore + ore_tick - B["clay_ore"],
                    clay + clay_tick,
                    obsidian + obsidian_tick,
                    geodes + geode_tick,
                    ore_tick,
                    clay_tick + 1,
                    obsidian_tick,
                    geode_tick,
                    tick + 1,
                )
            )

        if ore >= B["obsi_ore"] and clay >= B["obsi_clay"]:
            queue.append(
                (
                    ore + ore_tick - B["obsi_ore"],
                    clay + clay_tick - B["obsi_clay"],
                    obsidian + obsidian_tick,
                    geodes + geode_tick,
                    ore_tick,
                    clay_tick,
                    obsidian_tick + 1,
                    geode_tick,
                    tick + 1,
                )
            )

        if ore >= B["geode_ore"] and obsidian >= B["geode_obsi"]:
            queue.append(
                (
                    ore + ore_tick - B["geode_ore"],
                    clay + clay_tick,
                    obsidian + obsidian_tick - B["geode_obsi"],
                    geodes + geode_tick,
                    ore_tick,
                    clay_tick,
                    obsidian_tick,
                    geode_tick + 1,
                    tick + 1,
                )
            )
            
    return best

def part1():
    print("Part 1:",  sum(blueprint["id"] * evaluate(blueprint, 24) for blueprint in read_data()))

def part2():
    print("Part 2:", math.prod(evaluate(blueprint, 32) for blueprint in read_data()[:3]))

if __name__ == "__main__":
    part1()
    part2()