grids = [line.split() for line in open("input").read().split("\n\n")]
part1 = 0

def reflection(grid):
    for i in range(1, len(grid)):
        mismatch = 0
        for above, below in zip(grid[i-1::-1], grid[i:]):
            if above != below:
                mismatch += 1
        if mismatch == 0:
            return i
    return 0

def transpose(grid):
    return ["".join(col) for col in zip(*grid)]

for grid in grids:
    part1 += 100 * reflection(grid) + reflection(transpose(grid))

print(part1)
