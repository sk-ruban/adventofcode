tiles = [tuple(map(int, line.split(','))) for line in open("input")]
part1 = 0

for i, (x, y) in enumerate(tiles):
    for a, b in tiles[i+1:]:
        part1 = max(part1, (abs(x - a) + 1) * (abs(y - b) + 1))

print(part1)
