import numpy as np

def read_data():
    with open('./data/luke8.txt') as f:
        return np.array([np.array(list(x.strip()), dtype=int) for x in f.readlines()])


def get_directions(data, i, j):
    return (data[i][:j][::-1], data[i][j+1:], data[:, j][:i][::-1], data[:, j][i+1:])

def is_visible(data, i, j):
    row1, row2, col1, col2 = get_directions(data, i, j)
    tree = data[i][j]
    if i == 0 or i == len(data) - 1 or j == 0 or j == len(data[i]) - 1:
        return True
    return tree > max(row1) or tree > max(row2) or tree > max(col1) or tree > max(col2)

def part1():
    data = read_data()
    print(sum([1 for i in range(len(data)) for j in range(len(data[i])) if is_visible(data, i, j)]))

def get_direction_distance(trees, tree):
    for i in range(len(trees)):
        if trees[i] >= tree or i == len(trees) - 1:
            return i + 1
    return 0

def get_view_distance(data, i, j):
    row1, row2, col1, col2 = get_directions(data, i, j)
    tree = data[i][j]

    up = get_direction_distance(col1, tree)
    left = get_direction_distance(row1, tree)
    down = get_direction_distance(col2, tree)
    right = get_direction_distance(row2, tree)
    distances = [up, left, down, right]

    return distances

def part2():
    data = read_data()
    distances = {(i, j): get_view_distance(data, i, j) for i in range(len(data)) for j in range(len(data[i]))}
    print(max([np.prod(distances[distance]) for distance in distances]))


if __name__ == '__main__':
    part1()
    part2()