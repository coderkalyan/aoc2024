import re

with open("d03.in") as f:
    line = f.read().strip()

def part_a():
    pattern = re.compile("mul\(\d+,\d+\)")
    ans = 0
    for mul in re.findall(pattern, line):
        a, b = map(int, mul[4:-1].split(","))
        ans += a * b
    return ans

def part_b():
    pattern = re.compile("(mul\(\d+,\d+\))|(do\(\))|(don't\(\))")
    ans = 0
    enabled = True
    for mul in re.findall(pattern, line):
        if mul[1]:
            enabled = True
        elif mul[2]:
            enabled = False
        else:
            a, b = map(int, mul[0][4:-1].split(","))
            if enabled: ans += a * b
    return ans

print(part_a())
print(part_b())
