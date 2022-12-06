def read_data():
    with open('./data/luke5.txt') as f:
        data = f.readlines()
        data = [x.rstrip('\n') for x in data]
        data = (data[:data.index('')], data[data.index('')+1:])
        return data

def convert_containers(data):
    indexes = data[-1]
    indexes = [i for i, x in enumerate(indexes) if x.isdigit()]
    containers = [[] for _ in range(len(indexes))]
    for box in data[:-1][::-1]:
        for i, index in enumerate(indexes):
            letter = box[index]
            if letter.isalpha():
                containers[i].append(letter)
    return containers

def convert_instructions(data):
    data = [x.strip() for x in data]
    data = [re.split(r'[^0-9]', x) for x in data]
    instructions = [[int(y) for y in x if y] for x in data]
    return instructions

def part1():
    data = read_data()
    containers = convert_containers(data[0])
    instructions = convert_instructions(data[1])
    for instruction in instructions:
        amount = instruction[0]
        from_container = instruction[1]-1
        to_container = instruction[2]-1
        for _ in range(amount):
            containers[to_container].append(containers[from_container].pop())
    last_letters = [x[-1] for x in containers]
    print(''.join(last_letters))

    
def part2():
    data = read_data()
    containers = convert_containers(data[0])
    instructions = convert_instructions(data[1])
    for instruction in instructions:
        amount = instruction[0]
        from_container = instruction[1]-1
        to_container = instruction[2]-1
        to_move_sublist = containers[from_container][-amount:]
        containers[from_container] = containers[from_container][:-amount]
        containers[to_container] = containers[to_container] + to_move_sublist
    last_letters = [x[-1] for x in containers]
    print(''.join(last_letters))

if __name__ == '__main__':
    part1()
    part2()