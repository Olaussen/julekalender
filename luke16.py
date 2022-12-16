from collections import defaultdict
from functools import cache
import math
import re

def read_data():
    with open("./data/luke16.txt") as f:
        valves = {}
        dist = defaultdict(lambda: defaultdict(lambda: math.inf))
        for i, flow_rate, tunnels in re.findall(r"^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w ,]+)$", f.read(), re.MULTILINE):
            valves[i] = int(flow_rate)
            dist[i][i] = 0
            for j in tunnels.split(", "):
                dist[i][j] = 1

    for k in valves:
        for i in valves:
            for j in valves:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return valves, dist

def best_flow(start, time, elephant):
    valves, dist = read_data()
    
    @cache
    def find_best_flow(current, time, remaining, elephant):
        best_flow = find_best_flow("AA", 26, remaining, False) if elephant else 0
        for item in remaining:
            if (next_item := time - dist[current][item] - 1) >= 0:
                best_flow = max(best_flow, valves[item] * next_item + find_best_flow(item, next_item, remaining - {item}, elephant))
        return best_flow
    
    return find_best_flow(start, time, frozenset(x for x in valves if valves[x] > 0), elephant)

def part1():
    print("Part 1:", best_flow("AA", 30, False))

def part2():
    print("Part 2:", best_flow("AA", 26, True))

if __name__ == "__main__":
    part1()
    part2()