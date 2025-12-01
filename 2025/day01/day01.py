file = [x.strip() for x in open('input')]
dial = 50
part1 = part2 = 0

for rotation in file:
    delta = int(rotation[1:]) * (-1 if rotation[0] == 'L' else 1)
    dial = (dial + delta) % 100

    if dial == 0:
        part1 += 1
        part2 += 1

    part2 += abs(delta) // 100
    part2 += delta > 0 and dial < (delta % 100) and dial != 0
    part2 += delta < 0 and dial > 100 - (abs(delta) % 100)

print(part1, part2)
