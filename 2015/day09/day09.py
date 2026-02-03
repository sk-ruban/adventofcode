from collections import defaultdict
from itertools import permutations

locations = open("input").read().splitlines()
routes = defaultdict(dict)

for loc in locations:
    cities, dist = loc.split(" = ")
    a, b = cities.split(" to ")
    routes[a][b] = int(dist)
    routes[b][a] = int(dist)

part1 = min(sum(routes[a][b] for a, b in zip(p, p[1:])) for p in permutations(routes.keys()))
part2 = max(sum(routes[a][b] for a, b in zip(p, p[1:])) for p in permutations(routes.keys()))
print(part1, part2)
