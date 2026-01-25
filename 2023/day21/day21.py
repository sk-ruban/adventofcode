from collections import deque

grid = open("input").read().splitlines()
start = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == 'S')

dist = {start: 0}
queue = deque([start])

while len(queue) > 0:
    r, c = queue.popleft()
    for neighbour in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        nr, nc = neighbour
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != '#' and neighbour not in dist:
            dist[neighbour] = dist[(r, c)] + 1
            queue.append(neighbour)

part1 = 0
for cell in dist:
    if dist[cell] <= 64 and dist[cell] % 2 == 0:
        part1 += 1

print(part1)
