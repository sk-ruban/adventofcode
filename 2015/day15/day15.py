from itertools import combinations
from math import prod
import re

input = open("input").read().splitlines()
ings = [[int(x) for x in re.findall(r'-?\d+', line)] for line in open("input")]

part1, part2 = 0, 0
for i, j, k in combinations(range(103), 3):
    amts = [i, j-i-1, k-j-1, 102-k]
    props = [max(sum(a * ing[p] for a, ing in zip(amts, ings)), 0) for p in range(4)]
    part1 = max(part1, prod(props))
    calories = sum(a * ing[4] for a, ing in zip(amts, ings))
    if calories == 500:
        part2 = max(part2, prod(props))

print(part1, part2)
