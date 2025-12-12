summary = open("input").read().split("\n")[:-1]
part1 = 0

shape = 0
shapes = []

for line in summary:
    if 'x' in line:
        region, shapeCount = line.split(':')
        x, y = map(int, region.split('x'))
        counts = list(map(int, shapeCount.split()))
        area = sum(count * area for count, area in zip(counts, shapes))
        if x * y > area:
            part1 += 1
            print(area, region)
    elif '#' in line:
        shape += line.count('#')
    elif line == '':
        shapes.append(shape)
        shape = 0

print(part1)
