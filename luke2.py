def read_data():
    with open('./data/luke2.txt') as f:
        return f.readlines()

win_scores = {
    'A': {'X': 4, 'Y': 8, 'Z': 3}, 
    'B': {'X': 1, 'Y': 5, 'Z': 9},
    'C': {'X': 7, 'Y': 2, 'Z': 6}
}

choose_table = {
    'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'}, 
    'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'},
    'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}
}

def part1():
    print("Part 1:",sum([win_scores[x.strip().split(' ')[0]][x.strip().split(' ')[1]] for x in read_data()]))

def part2():
    print("Part 2:", sum([win_scores[x.strip().split(' ')[0]][choose_table[x.strip().split(' ')[0]][x.strip().split(' ')[1]]] for x in read_data()]))

if __name__ == '__main__':
    part1()
    part2()