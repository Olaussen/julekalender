def parts():
    with open('./data/luke1.txt') as f:
        data = sorted([sum(x) for x in [[int(x) for x in y] for y in [y.split('\n') for y in [x for x in f.read().split('\n\n')]]]])[-3:]
        print("Part 1:", data[-1], "\nPart 2:", sum(data))

if __name__ == '__main__':
    parts()