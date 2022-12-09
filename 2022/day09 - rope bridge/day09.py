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
    x_diff = abs(head[0] - tail[0])
    y_diff = abs(head[1] - tail[1])
    if (x_diff or y_diff) == 2 and (x_diff or y_diff) == 1:
        tail = [head[0], head[1]]
    elif x_diff == 2 or y_diff == 2:
        match direction:
            case 'R': tail = [head[0] - 1, head[1]]
            case 'L': tail = [head[0] + 1, head[1]]
            case 'U': tail = [head[0], head[1] - 1]
            case 'D': tail = [head[0], head[1] + 1]
    elif x_diff > 0 and y_diff > 0:
        print("LOL")
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


path = [x.split() for x in open('test_input.txt')]
print(positions(path, 2))
print(positions(path, 10))

