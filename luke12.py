from collections import deque

def read_data():
    with open("./data/luke12.txt") as f:
            return {
                (i, j): x
                    for i, row in enumerate(f.read().splitlines())
                    for j, x in enumerate(row)
                }

def adjacent(i, j):
    return (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)

def perform_bfs(data, starts, end):
    dist = {}
    queue = deque([(0, x) for x in starts])

    while len(queue) > 0:
        value, coord = queue.popleft()
        if coord in dist:
            continue
        dist[coord] = value

        for adj in adjacent(*coord):
            if ord(data.get(adj, "|")) - ord(data[coord]) > 1:
                continue
            queue.append((value + 1, adj))
    return dist[end]

def part1():
    data = read_data()
    start, end = next(k for k, v in data.items() if v == "S"), next(k for k, v in data.items() if v == "E")
    data[start], data[end] = "a", "z"

    print("Part 1:", perform_bfs(data, [start], end))

def part2():
    data = read_data()
    starts, end = {k for k, v in data.items() if v == "S" or v == "a"}, next(k for k, v in data.items() if v == "E")
    for start in starts:
        data[start] = "a"
    data[end] = "z"

    print("Part 2:", perform_bfs(data, starts, end))

if __name__ == "__main__":
    part1()
    part2()