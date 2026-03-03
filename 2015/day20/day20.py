target = 33100000
part1, part2 = 0, 0

max_house = target // 10
presents = [0] * (max_house + 1)

for elf in range(1, max_house + 1):
    for house in range(elf, max_house + 1, elf):
        presents[house] += 10 * elf

for house, p in enumerate(presents):
    if p >= target:
        part1 = house
        break

max_house = target // 11
presents = [0] * (max_house + 1)
elves = [0] * (max_house + 1)

for elf in range(1, max_house + 1):
    for house in range(elf, max_house + 1, elf):
        if elves[elf] < 50:
            presents[house] += 11 * elf
            elves[elf] += 1

for house, p in enumerate(presents):
    if p >= target:
        part2 = house
        break

print(part1, part2)
