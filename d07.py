from re import L
from aocd import data, submit

# data = open("d07.in.1").read().strip()
equations = []
for line in data.split("\n"):
    result, nums = line.split(":")
    equation = [int(result)] + list(map(int, nums.strip().split()))
    equations.append(equation)

def solve(expected, options):
    if len(options) == 1:
        return options[0] == expected
    elif len(options) == 2:
        return ((options[0] + options[1]) == expected) or ((options[0] * options[1]) == expected)

    ret = solve(expected, [options[0] + options[1]] + options[2:])
    ret = ret or solve(expected, [options[0] * options[1]] + options[2:])
    return ret

def cat(a, b):
    return int(str(a) + str(b)) # could be a lot faster with mul

def solve2(expected, options):
    if len(options) == 1:
        return options[0] == expected
    elif len(options) == 2:
        return ((options[0] + options[1]) == expected) or ((options[0] * options[1]) == expected) or (cat(options[0], options[1]) == expected)

    ret = solve2(expected, [options[0] + options[1]] + options[2:])
    ret = ret or solve2(expected, [options[0] * options[1]] + options[2:])
    ret = ret or solve2(expected, [cat(options[0], options[1])] + options[2:])
    return ret

def part_a():
    ans = 0
    for equation in equations:
        if solve(equation[0], equation[1:]): ans += equation[0]
    return ans

def part_b():
    ans = 0
    for equation in equations:
        if solve2(equation[0], equation[1:]): ans += equation[0]
    return ans

a = part_a()
print(a)
# submit(a, part="a")

b = part_b()
print(b)
submit(b, part="b")
