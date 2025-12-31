report = [[int(val) for val in line.split()] for line in open("input").read().splitlines()]

def recurse(line):
    if all(val == 0 for val in line):
        return 0
    diffs = [b - a for a, b in zip(line, line[1:])]
    return line[-1] + recurse(diffs)

part1 = sum(recurse(line) for line in report)

print(part1)
