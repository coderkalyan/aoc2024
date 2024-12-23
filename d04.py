import re
import numpy as np

xmas = list(map(ord, ["X", "M", "A", "S"]))

data = []
with open("d04.in.1") as f:
    for line in f:
        data.append(list(map(ord, line.strip())))
    rows, cols = len(data), len(data[0])
    # data = np.array(data)
    # rows, cols = data.shape
    # data = np.pad(data, ((rows, rows), (rows, cols)))

def count(visited, x, y, state):
    if x < 0 or x >= cols: return 0
    if y < 0 or y >= rows: return 0
    if visited[y][x]: return 0
    visited[y][x] = True

    if data[y][x] != xmas[state]: return 0

    if state == 3:
        return 1

    ans = 0
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            ans += count(visited, x + dx, y + dy, state + 1)
    return ans

def part_a():
    ans = 0
    for y in range(rows):
        for x in range(cols):
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            ans += count(visited, x, y, 0)

    return ans

def part_b():
    pass

print(part_a())
# print(part_b())
