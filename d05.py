from functools import cmp_to_key
from aocd import data, submit

rules = []
updates = []
for line in data.split("\n"):
    if "|" in line:
        rules.append(list(map(int, line.strip().split("|"))))
    elif line != "":
        updates.append(list(map(int, line.strip().split(","))))

def part_a():
    ans = 0
    for update in updates:
        valid = True
        for x, y in rules:
            if x not in update: continue
            if y not in update: continue
            if update.index(x) >= update.index(y):
                valid = False
                break
        if valid:
            ans += update[len(update) // 2]

    return ans

def cmp(a, b):
    for x, y in rules:
        if a == x and b == y:
            return -1
        elif a == y and b == x:
            return 1
    return 0

def part_b():
    ans = 0
    for update in updates:
        valid = True
        for x, y in rules:
            if x not in update: continue
            if y not in update: continue
            if update.index(x) >= update.index(y):
                valid = False
                break
        if not valid:
            # print(update, end=" ")
            update = sorted(update, key=cmp_to_key(cmp))
            # print(update)
            ans += update[len(update) // 2]

    return ans

# print(part_a())
submit(part_a(), part="a")
# print(part_b())
submit(part_b(), part="b")
