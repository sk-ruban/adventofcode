from itertools import combinations
from math import ceil

boss_hp, boss_dmg, boss_arm = [int(line.split(": ")[1]) for line in open("input")]

weapons = [(8,4,0), (10,5,0), (25,6,0), (40,7,0), (74,8,0)]
armours = [(0,0,0), (13,0,1), (31,0,2), (53,0,3), (75,0,4), (102,0,5)]
rings = [(25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]
rings_combos = [c for n in range(0, 3) for c in combinations(rings, n)]

part1, part2 = float('inf'), 0
for w in weapons:
    for a in armours:
        for r in rings_combos:
            cost, dmg, arm = (sum(x) for x in zip(w, a, *r))
            boss_death = ceil(boss_hp /max(dmg - boss_arm, 1))
            player_death = ceil(100 / max(boss_dmg - arm, 1))

            if player_death >= boss_death:
                part1 = min(part1, cost)
            else:
                part2 = max(part2, cost)

print(part1, part2)
