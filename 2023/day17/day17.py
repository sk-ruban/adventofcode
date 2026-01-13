import heapq
from itertools import count

grid = {complex(i, j): int(c)
    for j, r in enumerate(open("input").read().splitlines())
    for i, c in enumerate(r)
}

tiebreaker = count()
pq = [(0, next(tiebreaker), 0, 1, 0), (0, next(tiebreaker), 0, 1j, 0)]
seen = set()

def find_heat_loss():
    while pq:
        cost, _, pos, d, steps = heapq.heappop(pq)
        if (pos, d, steps) in seen:
            continue
        seen.add((pos, d, steps))
        if pos == [*grid][-1]:
            return cost
        for new_d in [d, d * 1j, d * -1j]:
            new_pos = pos + new_d
            if new_pos not in grid:
                continue

            if new_d == d and steps < 3:
                new_steps = steps + 1
            elif new_d != d:
                new_steps = 1
            else:
                continue

            heapq.heappush(pq, (cost + grid[new_pos], next(tiebreaker), pos + new_d, new_d, new_steps))

part1 = find_heat_loss()
print(part1)
