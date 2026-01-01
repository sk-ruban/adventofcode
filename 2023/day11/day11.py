image = open("input").read().splitlines()
part1 = 0

galaxies = [(r,c) for r, row in enumerate(image) for c, char in enumerate(row) if char == '#']

galaxy_rows = {r for (r,c) in galaxies}
empty_rows = {r for r in range(len(image)) if r not in galaxy_rows}

galaxy_cols = {c for (r,c) in galaxies}
empty_cols = {c for c in range(len(image[0])) if c not in galaxy_cols}

for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        fst, snd = galaxies[i], galaxies[j]
        r1, c1 = fst
        r2, c2 = snd
        count = abs(r2 - r1) + abs(c2 - c1)

        for r in range(min(r1,r2)+1, max(r1,r2)):
            if r in empty_rows:
                count += 1

        for c in range(min(c1,c2)+1, max(c1,c2)):
            if c in empty_cols:
                count += 1

        part1 += count

print(part1)
