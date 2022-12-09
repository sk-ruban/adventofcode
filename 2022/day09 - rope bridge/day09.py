"""
How many positions does the tail of the rope visit at least once?
"""


def head_move(direction, pos):
    match direction:
        case 'R': pos[0] += 1
        case 'L': pos[0] -= 1
        case 'U': pos[1] += 1
        case 'D': pos[1] -= 1


def tail_move(direction, head, tail):
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
        return tail
    if x_diff == 0:
        tail[1] += 1 if y_diff == 2 else -1
    elif y_diff == 0:
        tail[0] += 1 if x_diff == 2 else -1
    else:
        tail[1] += 1 if y_diff > 0 else -1
        tail[0] += 1 if x_diff > 0 else -1
    return tail


def positions(path, length):
    knots = [[0, 0] for _ in range(length)]
    tail_history = set()
    for direction, steps in path:
        steps = int(steps)
        for step in range(steps):
            head_move(direction, knots[0])
            for x in range(1, length):
                knots[x] = tail_move(direction, knots[x-1], knots[x])
            tail_history.add(tuple(knots[-1]))
    return len(tail_history)


path = [x.split() for x in open('input')]
# silver
print(positions(path, 2))
# gold
print(positions(path, 10))

