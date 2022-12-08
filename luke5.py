import re

def read_data():
    with open('./data/luke5.txt') as f:
        data = [x.rstrip('\n') for x in f.readlines()]
        return (data[:data.index('')], data[data.index('')+1:])

def part1():
    data = read_data()
    containers = [[box[index] for box in data[0][:-1][::-1] if box[index].isalpha()] for index in [i for i, x in enumerate(data[0][-1]) if x.isdigit()]]
    instructions = [[int(y) for y in x if y] for x in [re.split(r'[^0-9]', x) for x in [x.strip() for x in data[1]]]]
    for instruction in instructions:
        for _ in range(instruction[0]):
            containers[instruction[2] - 1].append(containers[instruction[1] - 1].pop())
    print("Part 1:", ''.join([x[-1] for x in containers]))

def part2():
    data = read_data()
    containers = [[box[index] for box in data[0][:-1][::-1] if box[index].isalpha()] for index in [i for i, x in enumerate(data[0][-1]) if x.isdigit()]]
    instructions = [[int(y) for y in x if y] for x in [re.split(r'[^0-9]', x) for x in [x.strip() for x in data[1]]]]
    for instruction in instructions:
        to_move_sublist = containers[instruction[1] - 1][-instruction[0]:]
        containers[instruction[1] - 1] = containers[instruction[1] - 1][:-instruction[0]]
        containers[instruction[2] - 1] = containers[instruction[2] - 1] + to_move_sublist
    print("Part 2:", ''.join([x[-1] for x in containers]))

if __name__ == '__main__':
    part1()
    part2()