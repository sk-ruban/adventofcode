grid = [list(line) for line in open("input").read().splitlines()]
length = len(grid[0])

def solve(grid, part2):
    if part2:
        grid[0][0] = grid[0][length-1] = grid[length-1][0] = grid[length-1][length-1] = '#'

    for _ in range(100):
        new = [['.' for _ in range(length)] for _ in range(length)]

        for r in range(length):
            for c in range(length):
                neighbours = 0
                for nr in range(r-1, r+2):
                    for nc in range(c-1, c+2):
                        if 0 <= nr < length and 0 <= nc < length and grid[nr][nc] == '#' and (nr, nc) != (r, c):
                            neighbours += 1
                if part2 and ((r, c) == (0, 0) or (r, c) == (0, length-1) or (r, c) == (length-1, length-1) or (r, c) == (length-1, 0)):
                    new[r][c] = '#'
                elif grid[r][c] == '#' and (neighbours == 2 or neighbours == 3):
                    new[r][c] = '#'
                elif grid[r][c] == '.' and (neighbours == 3):
                    new[r][c] = '#'
                else:
                    new[r][c] = '.'

        grid = new

    return grid

part1 = sum(line.count('#') for line in solve(grid, False))
part2 = sum(line.count('#') for line in solve(grid, True))

print(part1, part2)
