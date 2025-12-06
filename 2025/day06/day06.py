problems = [x.split() for x in open('input').read().splitlines()]
part1 = 0
rows, cols = len(problems), len(problems[0])
signs = problems[-1]

for i in range(cols):
    if signs[i] == '+':
        lineTotal = 0
    else:
        lineTotal = 1
    for line in problems[:-1]:
        if signs[i] == '+':
            lineTotal += int(line[i])
        else:
            lineTotal *= int(line[i])
    part1 += lineTotal

print(part1)
