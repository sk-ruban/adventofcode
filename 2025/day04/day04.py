grid = [list(x.strip()) for x in open('input')]
part1, part2 = 0, 0

rows, cols = len(grid), len(grid[0])
changed = True

def count(r, c):
    neighbours = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                    neighbours += 1

    return neighbours

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == '@' and count(r, c) < 4:
            part1 += 1

while changed:
    changed = False
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '@' and count(r, c) < 4:
                part2 += 1
                grid[r][c] = 'x'
                changed = True

print(part1, part2)
