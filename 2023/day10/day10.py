sketch = open("input").read().splitlines()

for i, line in enumerate(sketch):
    if 'S' in line:
        start = (i, line.index('S'))
        break

loop = {start}
coord, prev = start, None
pipes = [(-1,0,"|7F"), (1,0,"|LJ"), (0,-1,"-LF"), (0,1,"-J7")]

r, c = start
for dr, dc, valid in pipes:
    nr, nc = r + dr, c + dc
    if sketch[nr][nc] in valid:
        coord = (nr, nc)
        prev = start
        break

steps = 1
while coord != start:
    loop.add(coord)
    r, c = coord
    tile = sketch[r][c]

    match tile:
        case '|': exits = [(r-1,c), (r+1,c)]
        case '-': exits = [(r,c-1), (r,c+1)]
        case 'L': exits = [(r-1,c), (r,c+1)]
        case 'J': exits = [(r-1,c), (r,c-1)]
        case '7': exits = [(r+1,c), (r,c-1)]
        case 'F': exits = [(r+1,c), (r,c+1)]

    coord = exits[0] if exits[1] == prev else exits[1]
    prev = (r, c)
    steps += 1

part1 = steps // 2
part2 = 0

for r in range(len(sketch)):
    crossings = 0
    for c in range(len(sketch[r])):
        if (r, c) in loop:
            tile = sketch[r][c]
            if tile == '|':
                crossings += 1
            elif tile in 'FL':
                cc = c + 1
                while sketch[r][cc] == '-':
                    cc += 1
                closing = sketch[r][cc]
                if (tile == 'F' and closing == 'J') or (tile == 'L' and closing == '7'):
                    crossings += 1
        elif crossings % 2 == 1:
            part2 += 1

print(part1, part2)
