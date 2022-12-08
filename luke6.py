def read_data():
    with open('./data/luke6.txt') as f:
        return f.read()

def find_marker(s, amount):
    marker = ""
    for i in range(len(s)):
        if len(marker) == amount:
            marker = marker[1:] + s[i]
            if len(set(marker)) == len(marker):
                return i + 1
        elif len(marker) < amount:
            marker += s[i]
    return marker

def part1():
    print("Part 1:", find_marker(read_data(), 4))

def part2():
    print("Part 2:", find_marker(read_data(), 14))
    
if __name__ == '__main__':
    part1()
    part2()