import re

import numpy as np

grid1 = np.zeros((1000, 1000), dtype=int)
grid2 = np.zeros((1000, 1000), dtype=int)

for line in open("input"):
    x1, y1, x2, y2 = map(int, re.findall(r'\d+', line))
    s = np.s_[x1:x2+1, y1:y2+1]

    if "on" in line:
        grid1[s] = 1
        grid2[s] += 1
    elif "off" in line:
        grid1[s] = 0
        grid2[s] = np.maximum(grid2[s] - 1, 0)
    else:
        grid1[s] ^= 1
        grid2[s] += 2

part1 = sum(c for line in grid1 for c in line)
part2 = sum(c for line in grid2 for c in line)
print(part1, part2)
