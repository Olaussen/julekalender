def convert_to_list(data):
    return [i for i in range(int(data.split('-')[0]), int(data.split('-')[1])+1)]

def read_data():
    with open('./data/luke4.txt') as f:
        return [(convert_to_list(x[0]), convert_to_list(x[1])) for x in [x.split(',') for x in [x.strip() for x in open('./data/luke4.txt').readlines()]]]

def part1():
    print("Part 1:", sum([1 for x in read_data() if set(x[0]).issuperset(set(x[1])) or set(x[1]).issuperset(set(x[0]))]))
    
def part2():
    print("Part 2:", sum([1 for x in read_data() if set(x[0]).intersection(set(x[1]))]))
    
if __name__ == '__main__':
    part1()
    part2()