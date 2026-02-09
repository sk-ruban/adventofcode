from collections import defaultdict
from itertools import permutations

invited = open("input").read().splitlines()
happiness = defaultdict(dict)

for line in invited:
    words = line.split(" ")
    p1, p2, val = words[0], words[-1][:-1], words[3]
    happiness[p1][p2] = int(val) if words[2] == 'gain' else -int(val)

def max_happiness():
    optimal = 0
    for p in permutations(happiness.keys()):
        total = sum(happiness[p1][p2] + happiness[p2][p1] for p1, p2 in zip(p, p[1:] + p[:1]))
        optimal = max(optimal, total)
    return optimal

part1 = max_happiness()

for person in list(happiness.keys()):
    happiness["Me"][person] = 0
    happiness[person]["Me"] = 0

part2 = max_happiness()
print(part1, part2)
