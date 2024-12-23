reports = []
with open("d02.in") as f:
    for line in f:
        reports.append(list(map(int, line.strip().split())))

def part_a():
    ans = 0
    for report in reports:
        diffs = list(map(lambda xy: xy[1] - xy[0], zip(report[:-1], report[1:])))
        safe = True
        safe = safe and (all(map(lambda x: x >= 0, diffs)) or all(map(lambda x: x < 0, diffs)))
        safe = safe and all(map(lambda x: 1 <= abs(x) <= 3, diffs))
        ans += safe

    return ans

def part_b():
    ans = 0
    for report in reports:
        diffs = list(map(lambda xy: xy[1] - xy[0], zip(report[:-1], report[1:])))
        safe = True
        safe = safe and (all(map(lambda x: x >= 0, diffs)) or all(map(lambda x: x < 0, diffs)))
        safe = safe and all(map(lambda x: 1 <= abs(x) <= 3, diffs))
        really_safe = safe

        for i in range(len(report)):
            new = report[:i] + report[i + 1:]
            diffs = list(map(lambda xy: xy[1] - xy[0], zip(new[:-1], new[1:])))
            safe = True
            safe = safe and (all(map(lambda x: x >= 0, diffs)) or all(map(lambda x: x < 0, diffs)))
            safe = safe and all(map(lambda x: 1 <= abs(x) <= 3, diffs))
            really_safe = really_safe or safe

        ans += really_safe

    return ans

print(part_a())
print(part_b())
