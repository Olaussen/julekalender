def read_data():
    with open("./data/luke15.txt") as f:
        return [[(int(line[0][0]), int(line[0][1])), (int(line[1][0]), int(line[1][1]))] for line in [[[line[0][0].replace("Sensor at x=", ""), line[0][1].replace(" y=", "")], [line[1][0].replace("closest beacon is at x=", ""), line[1][1].replace(" y=", "")]] for line in [[[line[0][0].replace("Sensor at x=", ""), line[0][1].replace(" y=", "")], [line[1][0].replace("closest beacon is at x=", ""), line[1][1].replace(" y=", "")]] for line in [[line[0].split(","), line[1].split(",")] for line in [line.split(":") for line in f.read().splitlines()]]]]]

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def perform_count(y):
    segments = []
    beacons = set()
    for sensor, beacon in read_data():
        if beacon[1] == y:
            beacons.add(beacon[0])
        dist = manhattan(sensor, beacon) - abs(sensor[1] - y)
        if dist > 0:
            segments.append((sensor[0] - dist, sensor[0] + dist + 1))
    segments.sort()

    count = 0
    end = segments[0][0]
    for s in segments:
        start = max(s[0], end)
        end = max(end, s[1])
        count += end - start - sum(start <= x < end for x in beacons)
    return count

def find_beacon(y_min, y_max):
    data = read_data()
    beacons = set(beacon for _, beacon in data)
    for y in range(y_min, y_max + 1):
        segments = []
        for sensor, beacon in data:
            dist = manhattan(sensor, beacon) - abs(sensor[1] - y)
            if 0 < dist:
                segments.append((sensor[0] - dist, sensor[0] + dist))
        segments.sort()

        end = y_min
        for s in segments:
            x = end + 1
            if x < s[0] and x <= y_max and (x, y) not in beacons:
                return x, y
            end = max(end, s[1])

def part1():
    print("Part 1:", perform_count(2000000))

def part2():
    beacon = find_beacon(0, 4000000)
    print("Part 2:", beacon[0] * 4000000 + beacon[1])

if __name__ == "__main__":
    part1()
    part2()