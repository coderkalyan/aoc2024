l1 = []
l2 = []

with open("d01.in") as f:
    for line in f:
        a, b = map(int, line.strip().split())
        l1.append(a)
        l2.append(b)

def part_a():
    ans = sum(map(lambda xy: abs(xy[0] - xy[1]), zip(sorted(l1), sorted(l2))))
    return ans

def part_b():
    ans = sum(x * l2.count(x) for x in l1)
    return ans

print(part_a())
print(part_b())
