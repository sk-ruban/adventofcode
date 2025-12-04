grid = [x.strip() for x in open('input')]
part1 = 0

rows, cols = len(grid), len(grid[0])

for x in range(cols):
    for y in range(rows):
        if grid[x][y] != '@':
            continue

        neighbours = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dy == 0 and dx == 0:
                    continue
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols and grid[nx][ny] == '@':
                        neighbours += 1

        if neighbours < 4:
            part1 += 1

print(part1)
