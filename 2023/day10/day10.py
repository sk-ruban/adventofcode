sketch = open("input").read().splitlines()
pipes = [(-1,0,"|7F"), (1,0,"|LJ"), (0,-1,"-LF"), (0,1,"-J7")]

for i in range(len(sketch)):
    idx = sketch[i].find('S')
    if idx != -1:
        start = (i,idx)

r, c = start
for dr, dc, valid in pipes:
    nr, nc = r + dr, c + dc
    if sketch[nr][nc] in valid:
        coord = (nr, nc)
        prev = start
        break

steps = 1
while coord != start:
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
print(part1)
