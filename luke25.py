def read_data():
    with open("./data/luke25.txt") as f:
        return f.read().splitlines()

POWERS = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
REVERSED = {v: k for k, v in POWERS.items()}

def get_snafu(line):
    return sum(POWERS[num] * 5**i for i, num in enumerate(line[::-1])) 

def reverse_snafu(total):
    snafu = ""
    while total:
        total, num = divmod(total, 5)
        if num > 2:
            num -= 5
            total += 1
        snafu += REVERSED[num]
        
    return snafu[::-1]

def part1():
    print("Part 1:",  reverse_snafu(sum(get_snafu(line) for line in read_data())))

if __name__ == "__main__":
    part1()