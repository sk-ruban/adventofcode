manual = open("input").read().splitlines()
part1 = 0

def solve(target, buttons):
    n = len(target)
    target = tuple(target)
    queue = [(tuple([0] * n), 0)]
    visited = {tuple([0] * n)}

    while queue:
        state, presses = queue.pop(0)

        if state == target:
            return presses

        for button in buttons:
            new = list(state)
            for i in button:
                new[i] ^= 1
            new = tuple(new)

            if new not in visited:
                visited.add(new)
                queue.append((new, presses + 1))

for line in manual:
    comp = line.split()
    lights = [c == '#' for c in comp[0][1:-1]]
    buttons = [list(map(int, c[1:-1].split(','))) for c in comp[1:-1]]

    part1 += solve(lights, buttons)

print(part1)
