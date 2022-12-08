def read_data():
    with open('./data/luke3.txt') as f:
        return [x.strip() for x in f.readlines()]

def part1():
    total = 0
    for x in [(x[:len(x)//2], x[len(x)//2:]) for x in read_data()]:
        for y in x[0]:
            if y in x[1]:
                total += ord(y) - (38 if y.isupper() else 96)
                break
    print("Part 1:", total)

def part2():
    data = read_data()
    total = 0
    for x in [(data[i], data[i+1], data[i+2]) for i in range(0, len(data), 3)]:
        for y in x[0]:
            if y in x[1] and y in x[2]:
                total += ord(y) - (38 if y.isupper() else 96)
                break
    print("Part 2:", total)

if __name__ == '__main__':
    part1()
    part2()