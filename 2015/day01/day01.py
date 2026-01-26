instructions = open("input").read()
part1, part2 = 0, 0

for i, c in enumerate(instructions, 1):
    part1 += 1 if c == '(' else -1
    if part1 == -1 and not part2:
        part2 = i

print(part1, part2)
