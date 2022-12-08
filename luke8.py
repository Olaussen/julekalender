import numpy as np

def read_data():
    with open('./data/luke8.txt') as f:
        return np.array([np.array(list(x.strip()), dtype=int) for x in f.readlines()])

def is_visible(data, i, j):
    tree = data[i][j]
    if i == 0 or i == len(data) - 1 or j == 0 or j == len(data[i]) - 1:
        return True
    return tree > max(data[i][:j][::-1]) or tree > max(data[i][j+1:]) or tree > max(data[:, j][:i][::-1]) or tree > max(data[:, j][i+1:])

def get_direction_distance(trees, tree):
    return next((i + 1 for i in range(len(trees)) if trees[i] >= tree or i == len(trees) - 1), 0)

def get_view_distance(data, i, j):
    tree = data[i][j]
    return [get_direction_distance(data[:, j][:i][::-1], tree), 
            get_direction_distance(data[i][:j][::-1], tree), 
            get_direction_distance(data[:, j][i+1:], tree), 
            get_direction_distance(data[i][j+1:], tree)]

def part1():
    data = read_data()
    print("Part 1:", sum([1 for i in range(len(data)) for j in range(len(data[i])) if is_visible(data, i, j)]))

def part2():
    data = read_data()
    print("Part 2:", max([np.prod(get_view_distance(data, i, j)) for i in range(len(data)) for j in range(len(data[i]))]))

if __name__ == '__main__':
    part1()
    part2()