file = open("input").read().splitlines()
part1, part2 = 0, 0

for line in file:
    i = 0
    part1 += 2
    while i < len(line):
        if line[i:i+2] == r'\\':
            part1 += 1
            i += 2
        elif line[i:i+2] == r'\"':
            part1 += 1
            i += 2
        elif line[i:i+2] == r'\x':
            part1 += 3
            i += 4
        else:
            i += 1
    part2 += 2 + line.count('"') + line.count('\\')

print(part1, part2)
