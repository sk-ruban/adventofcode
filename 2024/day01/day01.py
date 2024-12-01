file = [x.strip() for x in open('day01/input')]

col1, col2 = zip(*[map(int, line.split()) for line in file])
col1 = sorted(col1)
col2 = sorted(col2)

part1 = 0
for i in range(len(col1)):
    part1 += abs(col1[i] - col2[i])

part2 = 0
for num in col1:
    part2 += num * col2.count(num)

print(part1)
print(part2)