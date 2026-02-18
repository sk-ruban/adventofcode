from itertools import combinations

containers = [int(x) for x in open("input").read().splitlines()]
part1, part2 = 0, 0
minimum = float('inf')

for size in range(len(containers) + 1):
    combos = combinations(containers, size)
    for combo in combos:
        if sum(combo) == 150:
            part1 += 1
            minimum = min(minimum, size)
            if size == minimum:
                part2 += 1

print(part1, part2)
