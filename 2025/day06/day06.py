import math

problems = [x.split() for x in open('input').read().splitlines()]

part1 = sum(
    sum(int(line[i]) for line in problems[:-1]) if sign == '+'
    else math.prod(int(line[i]) for line in problems[:-1])
    for i, sign in enumerate(problems[-1])
)

lines = open('input').read().splitlines()
cols = list(zip(*lines))

part2 = 0
problems = []
curr = []

for col in cols:
    if all(c == ' ' for c in col):
        if curr:
            problems.append(curr)
            curr = []
    else:
        curr.append(col)

if curr:
    problems.append(curr)

for prob in problems:
    op = prob[0][-1]
    nums = [int("".join(digits[:-1]).strip()) for digits in prob]
    part2 += (sum(nums) if op == '+' else math.prod(nums))

print(part1, part2)
