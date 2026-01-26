dimensions = open("input").read().splitlines()
part1, part2 = 0, 0

for d in dimensions:
    l, w, h = sorted(map(int, d.split('x')))
    sides = [l*w, w*h, h*l]

    part1 += 2 * sum(sides) + min(sides)
    part2 += 2*l + 2*w + l*w*h

print(part1, part2)
