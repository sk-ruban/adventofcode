import heapq
from itertools import count

grid = {complex(i, j): int(c)
    for j, r in enumerate(open("input").read().splitlines())
    for i, c in enumerate(r)
}
goal = [*grid][-1]

def find_heat_loss(min, max):
    tiebreaker = count()
    pq = [(0, next(tiebreaker), 0, 1, 0), (0, next(tiebreaker), 0, 1j, 0)]
    seen = set()

    while pq:
        cost, _, pos, d, steps = heapq.heappop(pq)
        if (pos, d, steps) in seen:
            continue
        seen.add((pos, d, steps))
        if pos == goal and steps >= min:
            return cost
        for new_d in [d, d * 1j, d * -1j]:
            new_pos = pos + new_d
            if new_pos not in grid:
                continue

            if new_d == d and steps < max:
                new_steps = steps + 1
            elif new_d != d and min <= steps:
                new_steps = 1
            else:
                continue

            heapq.heappush(pq, (cost + grid[new_pos], next(tiebreaker), pos + new_d, new_d, new_steps))

part1 = find_heat_loss(1, 3)
part2 = find_heat_loss(4, 10)
print(part1, part2)
