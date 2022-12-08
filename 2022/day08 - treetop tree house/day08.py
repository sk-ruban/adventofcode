"""
How many trees are visible from outside the grid?
"""


def max_height(tree_height, t, b, l, r):
    max_top = int(max(t, default=0))
    max_bottom = int(max(b, default=0))
    max_left = int(max(l, default=0))
    max_right = int(max(r, default=0))
    if any(tree_height > max for max in [max_top, max_bottom, max_left, max_right]):
        return 1
    elif tree == 0 and 0 in (len(t), len(b), len(l), len(r)):
        return 1
    else:
        return 0


def direction_points(tree, direction):
    points = 0
    for each in direction:
        if tree <= int(each):
            points += 1
            break
        else:
            points += 1
    return points


def scenic(tree, t, b, l, r):
    top_points = direction_points(tree, reversed(t))
    bottom_points = direction_points(tree, b)
    left_points = direction_points(tree, reversed(l))
    right_points = direction_points(tree, r)
    return top_points * bottom_points * right_points * left_points


grid = [x.strip() for x in open('input')]
silver = 0
gold = 0
for row, trees in enumerate(grid):
    for col, tree in enumerate(trees):
        top = [x[col] for x in grid[0:row]]
        bottom = [x[col] for x in grid[row+1:len(grid)]]
        left = [x for x in grid[row]][0:col]
        right = [x for x in grid[row]][col+1:len(grid)]
        silver += max_height(int(tree), top, bottom, left, right)
        gold = max(gold, scenic(int(tree), top, bottom, left, right))

print(f"silver: {silver}")
print(f"gold: {gold}")


