grids = [line.split() for line in open("input").read().split("\n\n")]
part1, part2 = 0, 0

def reflection(grid, smudges):
    for i in range(1, len(grid)):
        mismatches = sum(
            fst != snd
            for above, below in zip(grid[i-1::-1], grid[i:])
            for fst, snd in zip(above, below)
        )
        if mismatches == smudges:
            return i
    return 0

def transpose(grid):
    return ["".join(col) for col in zip(*grid)]

for grid in grids:
    part1 += 100 * reflection(grid, 0) + reflection(transpose(grid), 0)
    part2 += 100 * reflection(grid, 1) + reflection(transpose(grid), 1)

print(part1, part2)
