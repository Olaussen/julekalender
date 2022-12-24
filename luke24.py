from collections import deque

def read_data():
    with open('./data/luke24.txt') as f:
        lines = [row[1:-1] for row in f.read().splitlines()[1:-1]]
        return lines, {(i, j): cell for i, row in enumerate(lines) for j, cell in enumerate(row)}

DIRS = [(1, 0, 0), (1, 1, 0), (1, 0, 1), (1, -1, 0), (1, 0, -1)]

def add_tuples(a, b):
    return tuple(sum(x) for x in zip(a, b))

def is_blizzard(grid, rows, columns, time, i, j, start, end):
    if (i, j) in (start, end):
        return False
    try:
        return (
            grid[(i - time) % rows, j] == "v"
            or grid[(i + time) % rows, j] == "^"
            or grid[i, (j - time) % columns] == ">"
            or grid[i, (j + time) % columns] == "<"
        )
    except KeyError:
        return True

def shortest_path(grid, start, end, rows, columns, time=0):
    grid[-1, 0] = grid[rows, columns - 1] = "."

    visited = set()
    queue = deque([(time, *start)])
    while len(queue) > 0:
        time, i, j = current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        if (i, j) == end:
            return time

        for dir in DIRS:
            x = add_tuples(current, dir)
            if not is_blizzard(grid, rows, columns, *x, start, end):
                queue.append(x)

def part1():
    lines, grid = read_data()
    rows, columns = len(lines), len(lines[0])
    print("Part 1:", shortest_path(grid, (-1, 0), (rows, columns - 1), rows, columns))

def part2():
    lines, grid = read_data()
    rows, columns = len(lines), len(lines[0])
    first = shortest_path(grid, (-1, 0), (rows, columns - 1), rows, columns)
    back = shortest_path(grid, (rows, columns - 1), (-1, 0), rows, columns, first)
    print("Part 2:", shortest_path(grid, (-1, 0), (rows, columns - 1), rows, columns, back))

if __name__ == '__main__':
    part1()
    part2()