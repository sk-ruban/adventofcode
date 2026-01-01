from itertools import combinations

image = open("input").read().splitlines()
galaxies = [(r,c) for r, row in enumerate(image) for c, char in enumerate(row) if char == '#']

galaxy_rows = {r for r, c in galaxies}
empty_rows = {r for r in range(len(image)) if r not in galaxy_rows}

galaxy_cols = {c for r, c in galaxies}
empty_cols = {c for c in range(len(image[0])) if c not in galaxy_cols}

def dist(expansion):
    total = 0
    for (r1, c1), (r2, c2) in combinations(galaxies, 2):
        base = abs(r2 - r1) + abs(c2 - c1)
        extra = sum(1 for r in range(min(r1,r2)+1, max(r1,r2)) if r in empty_rows)
        extra += sum(1 for c in range(min(c1,c2)+1, max(c1,c2)) if c in empty_cols)
        total += base + extra * (expansion - 1)

    return total

part1 = dist(2)
part2 = dist(1000000)

print(part1, part2)
