diagram = open("input").read().splitlines()

part1 = 0
rows, cols = len(diagram), len(diagram[-1])
beams = [0] * cols
beams[(cols // 2)] = 1

for r in range(rows):
    for c in range(cols):
        if diagram[r][c] == '^' and beams[c] and 0 < c < cols:
            beams[c+1] += beams[c]
            beams[c-1] += beams[c]
            beams[c] = 0
            part1 += 1

part2 = sum(beams)
print(part1, part2)
