from itertools import combinations
from aocd import data, submit

# data = open("d08.in.1").read().strip()
nodes = dict()
height = len(data.split("\n"))
for y, line in enumerate(data.split("\n")):
    width = len(line.strip())
    for x, char in enumerate(list(line.strip())):
        if char == ".": continue
        if char not in nodes: nodes[char] = list()
        nodes[char].append((x, y))

def antinodes(antennas):
    ret = []
    for a, b in combinations(antennas, 2):
        dx, dy = b[0] - a[0], b[1] - a[1]
        ret.append((a[0] - dx, a[1] - dy))
        ret.append((b[0] + dx, b[1] + dy))
    return ret

def antinodes2(antennas):
    ret = []
    for a, b in combinations(antennas, 2):
        ret.append(a)
        ret.append(b)
        dx, dy = b[0] - a[0], b[1] - a[1]
        while True:
            b = (b[0] + dx, b[1] + dy)
            if not in_bounds(b): break
            ret.append(b)
        while True:
            a = (a[0] - dx, a[1] - dy)
            if not in_bounds(a): break
            ret.append(a)
    return ret

def in_bounds(n):
    x, y = n
    return x >= 0 and x < width and y >= 0 and y < height

def part_a():
    ans = []
    for freq, antennas in nodes.items():
        ans.extend(list(filter(in_bounds, antinodes(antennas))))

    return len(set(ans))

def part_b():
    ans = []
    for freq, antennas in nodes.items():
        ans.extend(antinodes2(antennas))

    return len(set(ans))

a = part_a()
# print(a)
# submit(a, part="a")

b = part_b()
print(b)
submit(b, part="b")
