from itertools import combinations
from aocd import data, submit

data = open("d11.in.1").read().strip()

def part_a():
    stones = list(map(int, data.split(" ")))
    for _ in range(6):
        i = 0
        while i < len(stones):
            if stones[i] == 0:
                stones[i] = 1
            else:
                s = str(stones[i])
                l = len(s)
                if l % 2 == 0:
                    stones[i] = int(s[:l // 2])
                    stones.insert(i + 1, int(s[l // 2:]))
                    i += 1
                else:
                    stones[i] *= 2024
        print(stones)

    return len(stones)

def part_b():
    ans = 0
    return ans

a = part_a()
print(a)
# submit(a, part="a")

# b = part_b()
# print(b)
# submit(b, part="b")
