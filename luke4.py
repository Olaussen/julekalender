def convert_to_list(data):
    # convert '1-3' to [1,2,3] and '2-5' to [2,3,4,5]
    data = data.split('-')
    data = [i for i in range(int(data[0]), int(data[1])+1)]
    return data

def read_data():
    with open('./data/luke4.txt') as f:
        data = f.readlines()
        data = [x.strip() for x in data]
        data = [x.split(',') for x in data]
        data = [(convert_to_list(x[0]), convert_to_list(x[1])) for x in data]
        return data


def part1():
    data = read_data()
    total = sum([1 for x in data if set(x[0]).issuperset(set(x[1])) or set(x[1]).issuperset(set(x[0]))])
    print(total)
    
def part2():
    data = read_data()
    total = sum([1 for x in data if set(x[0]).intersection(set(x[1]))])
    print(total)
    

if __name__ == '__main__':
    part1()
    part2()