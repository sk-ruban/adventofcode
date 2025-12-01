file = [x.strip() for x in open('input')]
start = 50
part1 = 0

for rotation in file:
    direction = -1 if rotation[0] == 'L' else 1
    distance = int(rotation[1:])
    start += direction * distance
    if start % 100 == 0:
        part1 += 1

print(part1)
