def read_data():
    with open('./data/luke2.txt') as f:
        return f.readlines()

win_scores = {
    # A is rock B is paper C is scissors
    'A': {'X': 4, 'Y': 8, 'Z': 3}, # X is rock, Y is paper, Z is scissors
    'B': {'X': 1, 'Y': 5, 'Z': 9},
    'C': {'X': 7, 'Y': 2, 'Z': 6}
}

choose_table = {
    # A is rock B is paper C is scissors
    'A': {'X': 'Z', 'Y': 'X', 'Z': 'Y'}, # Loses to Y paper, draws with X rock, wins against Z scissors
    'B': {'X': 'X', 'Y': 'Y', 'Z': 'Z'}, # Loses to Z scissors, draws with Y paper, wins against X rock
    'C': {'X': 'Y', 'Y': 'Z', 'Z': 'X'}  # Loses to X rock, draws with Z scissors, wins against Y paper
}

def part1():
    data = read_data()
    total = 0
    for x in data:
        x = x.strip().split(' ')
        score = win_scores[x[0]][x[1]]
        total += score
    print(total)

def part2():
    data = read_data()
    total = 0
    for x in data:
        x = x.strip().split(' ')
        choice = choose_table[x[0]][x[1]]
        score = win_scores[x[0]][choice]
        total += score
    print(total)

if __name__ == '__main__':
    part1()
    part2()