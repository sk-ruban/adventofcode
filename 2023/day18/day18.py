plan = open("input").read().splitlines()

vertices = list()
coord = (0, 0)
area = 0
boundary = 0

for line in plan:
    x, y = coord
    dir, dist, color = line.split()
    dist = int(dist)
    match dir:
        case "R": x += dist
        case "L": x -= dist
        case "D": y += dist
        case "U": y -= dist

    coord = (x, y)
    vertices.append(coord)
    boundary += dist

for i in range(len(vertices)):
    x1, y1 = vertices[i]
    x2, y2 = vertices[(i + 1) % len(vertices)]
    area += (x1 * y2 - x2 * y1)

part1 = abs(area) // 2 + boundary // 2 + 1
print(part1)
