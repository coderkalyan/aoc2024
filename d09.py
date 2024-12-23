from itertools import combinations
from aocd import data, submit

data = open("d09.in.1").read().strip()
# for line in data.split("\n"):
#     pass

def part_a():
    ans = 0
    parity = True
    s = ""
    blocks = 0
    for i, char in enumerate(data):
        if parity:
            s += str(i // 2) * int(char)
            blocks += int(char)
        else:
            s += "." * int(char)
        parity = not parity

    i = 0
    j = len(s) - 1
    while True:
        while i < blocks and s[i] != ".":
            i += 1
        if i >= blocks: break
        while j >= 0 and s[j] == ".":
            j -= 1
        # if j < 0: break
        s = s[:i] + s[j] + s[i + 1:j] + "." + s[j + 1:]
        i += 1
        j -= 1

    print(s)
    for i, char in enumerate(s.strip(".")):
        ans += i * int(char)
    return ans

def part_b():
    ans = 0
    return ans

a = part_a()
print(a)
submit(a, part="a")

b = part_b()
# print(b)
# submit(b, part="b")
