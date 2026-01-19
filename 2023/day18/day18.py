plan = open("input").read().splitlines()

def solve(part):
    vertices = list()
    coord = (0, 0)
    area = 0
    boundary = 0

    for line in plan:
        x, y = coord
        dir, dist, color = line.split()
        if part == 2:
            dist = int(color[2:7], 16)
            dir = "RDLU"[int(color[7])]
        else:
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

    return abs(area) // 2 + boundary // 2 + 1

part1 = solve(1)
part2 = solve(2)
print(part1, part2)
