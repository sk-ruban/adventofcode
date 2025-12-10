from itertools import combinations, starmap, compress
from shapely.geometry import Polygon, box

tiles = [tuple(map(int, line.split(','))) for line in open("input")]
rects = []
areas = []

for (x, y), (a, b) in combinations(tiles, 2):
    size = (abs(x - a) + 1) * (abs(y - b) + 1)
    rects.append((min(x, a), min(y, b), max(x, a), max(y, b)))
    areas.append(size)

part1 = max(areas)

poly = Polygon(tiles)
part2 = max(compress(areas, map(poly.contains, starmap(box, rects))))

print(part1, part2)
