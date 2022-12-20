from collections import deque

def read_data():
    with open("./data/luke20.txt") as f:
        return deque((index, int(line)) for index, line in enumerate(f.readlines()))

def perform(amount, nums, order):
    for _ in range(amount):
        for x in order:
            idx = next(i for i, y in enumerate(nums) if x[0] == y[0])
            nums.rotate(-idx)
            nums.popleft()
            nums.rotate(-x[1])
            nums.appendleft(x)

    nums.rotate(-next(i for i, x in enumerate(nums) if x[1] == 0))
    return nums[1000 % len(nums)][1] + nums[2000 % len(nums)][1] + nums[3000 % len(nums)][1]

def part1():
    numbers = read_data()
    print("Part 1:", perform(1, numbers, list(numbers)))

def part2():
    numbers = deque((x[0], x[1] * 811589153) for x in read_data())
    print("Part 2:", perform(10, numbers, list(numbers)))

if __name__ == "__main__":
    part1()
    part2()