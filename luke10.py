def read_data():
    with open("./data/luke10.txt") as f:
            return [x.split(" ") for x in f.read().splitlines()]

def part1():
    X = 1
    cycle = 0
    signal = 0

    def do_cycle():
        nonlocal cycle, signal
        cycle += 1
        signal += cycle * X if cycle in (20, 60, 100, 140, 180, 220) else 0

    for line in read_data():
        match line:
            case ["addx", num]:
                for _ in range(2):
                    do_cycle()
                X += int(num)
            case ["noop"]:
                do_cycle()
    print("Part 1:", signal)

def part2():
    X = 1
    cycle = 0

    def do_cycle():
        nonlocal cycle
        print("#" if cycle % 40 in (X - 1, X, X + 1) else " ", end="")
        cycle += 1; print() if cycle % 40 == 0 else None

    print("Part 2")
    for line in read_data():
        match line:
            case ["addx", num]:
                do_cycle(); do_cycle()
                X += int(num)
            case ["noop"]:
                do_cycle()

if __name__ == "__main__":
    part1()
    part2()