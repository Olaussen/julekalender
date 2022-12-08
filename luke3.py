def read_data():
    with open('./data/luke3.txt') as f:
        return [x.strip() for x in f.readlines()]


def get_value(letter):
    return ord(letter) - (38 if letter.isupper() else 96)

def part1():
    data = [(x[:len(x)//2], x[len(x)//2:]) for x in read_data()]
    total = 0
    for x in data:
        for y in x[0]:
            if y in x[1]:
                total += get_value(y)
                break
    print("Part 1:", total)

def part2():
    data = read_data()
    data = [(data[i], data[i+1], data[i+2]) for i in range(0, len(data), 3)]
    total = 0
    for x in data:
        for y in x[0]:
            if y in x[1] and y in x[2]:
                total += get_value(y)
                break
    print("Part 2:", total)

if __name__ == '__main__':
    part1()
    part2()