def read_data():
    with open('./data/luke3.txt') as f:
        return [x.strip() for x in f.readlines()]


def get_value(letter):
    ascii = ord(letter)
    if(letter.isupper()):
        return ascii - 38
    return ascii - 96

def part1():
    data = read_data()
    data = [(x[:len(x)//2], x[len(x)//2:]) for x in data]
    total = 0
    for x in data:
        for y in x[0]:
            if y in x[1]:
                total+= get_value(y)
                break
    print(total)

def part2():
    data = read_data()
    data = [(data[i], data[i+1], data[i+2]) for i in range(0, len(data), 3)]
    total = 0
    for x in data:
        for y in x[0]:
            if y in x[1] and y in x[2]:
                total += get_value(y)
                break
    print(total)

if __name__ == '__main__':
    part1()
    part2()