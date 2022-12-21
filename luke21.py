from operator import add, mul, sub, truediv

def read_data():
    with open("./data/luke21.txt") as f:
        return f.read().splitlines()

flip = lambda f: lambda *a: f(*reversed(a))

OPERATIONS = {
    "+": (add, sub, sub),
    "-": (sub, add, flip(sub)),
    "*": (mul, truediv, truediv),
    "/": (truediv, mul, flip(truediv)),
}

def extract_monkeys():
    vals = {}
    for line in read_data():
        name, eq = line.split(": ")
        match eq.split():
            case [num]:
                vals[name] = int(num)
            case [a, op, b]:
                vals[name] = a, b, *OPERATIONS[op]
    return vals

def calc(vals, i):
    match vals[i]:
        case a, b, f, _, _:
            av, bv = calc(vals, a), calc(vals, b)
            if None in (av, bv):
                return None
            return f(av, bv)
        case _:
            return vals[i]

def part1():
    print("Part 1:", int(calc(extract_monkeys(), "root")))

def part2():
    monkeys = extract_monkeys()
    monkeys["humn"] = None
    monkeys["root"] = *monkeys["root"][:2], *OPERATIONS["-"]

    def solve(key, value):
        match monkeys[key]:
            case left, right, _, funca, funcb:
                match calc(monkeys, left), calc(monkeys, right):
                    case left_result, None:
                        return solve(right, funcb(value, left_result))
                    case None, right_result:
                        return solve(left, funca(value, right_result))
            case None:
                return value

    print("Part 2:", int(solve("root", 0)))

if __name__ == "__main__":
    part1()
    part2()