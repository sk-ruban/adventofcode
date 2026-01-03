platform = [list(line) for line in open("input").read().splitlines()]
rows, cols = len(platform), len(platform[0])
pos = [0] * rows
part1 = 0

for r in range(rows):
    for c in range(cols):
        if platform[r][c] == 'O':
            platform[r][c] = '.'
            platform[pos[c]][c] = 'O'
            pos[c] += 1
        elif platform[r][c] == '#':
            pos[c] = r + 1

part1 = sum(rows- r for r in range(rows) for c in range(cols) if platform[r][c] == 'O')

print(part1)
