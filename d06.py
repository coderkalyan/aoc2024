from functools import cmp_to_key
import copy
from aocd import data, submit

data = open("d06.in.1").read().strip()
# print(data)
field = data.split("\n")
chars = ["^", ">", "v", "<"]
deltas = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def recurse(in_field):
    temp_field = copy.deepcopy(in_field)
    for y, line in enumerate(temp_field):
        found = False
        for dir, char in enumerate(chars):
            if (x := line.find(char)) != -1:
                found = True
                break
        if found: break

    start = True
    while True:
        print(x, y, temp_field[y][x])
        if temp_field[y][x] == ".":
            temp_field[y] = temp_field[y][:x] + "X" + temp_field[y][x + 1:]
        elif temp_field[y][x] == "^":
            if not start and dir == 0: return True
            start = False

        delta = deltas[dir]
        nx = x + delta[0]
        ny = y + delta[1]
        if nx < 0 or nx >= len(temp_field[0]): break
        if ny < 0 or ny >= len(temp_field): break
        if temp_field[ny][nx] == "#" or temp_field[ny][nx] == "O":
            dir = (dir + 1) % len(deltas)

        delta = deltas[dir]
        x += delta[0]
        y += delta[1]

    return False

def part_a():
    for y, line in enumerate(field):
        found = False
        for dir, char in enumerate(chars):
            if (x := line.find(char)) != -1:
                found = True
                break
        if found: break

    ans = 1
    while True:
        if field[y][x] == ".":
            ans += 1
            field[y] = field[y][:x] + "X" + field[y][x + 1:]

        delta = deltas[dir]
        nx = x + delta[0]
        ny = y + delta[1]
        if nx < 0 or nx >= len(field[0]): break
        if ny < 0 or ny >= len(field): break
        if field[ny][nx] == "#":
            dir = (dir + 1) % len(deltas)

        delta = deltas[dir]
        x += delta[0]
        y += delta[1]

    return ans

def part_b():
    ans = 0
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] != ".": continue
            new_field = copy.deepcopy(field)
            new_field[y] = field[y][:x] + "O" + field[y][x + 1:]
            # print("\n".join(new_field))
            # print(recurse(new_field))
            ans += recurse(new_field)
        #     break
        # break

    return ans

# print(part_a())
# submit(part_a(), part="a")
print(part_b())
# submit(part_b(), part="b")
