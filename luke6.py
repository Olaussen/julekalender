def read_data():
    with open('./data/luke6.txt') as f:
        return f.read()

def unique(s):
    return len(set(s)) == len(s)

def find_marker(s, amount):
    marker = ""
    for i in range(len(s)):
        if len(marker) == amount:
            marker = marker[1:] + s[i]
            if unique(marker):
                print(i+1)
                break
        elif len(marker) < amount:
            marker += s[i]

def part1():
    data = read_data()
    find_marker(data, 4)

    
def part2():
    data = read_data()
    find_marker(data, 14)
    
if __name__ == '__main__':
    part1()
    part2()