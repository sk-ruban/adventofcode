"""
How many trees are visible from outside the grid?
"""
# Unwashed af


def max_height(tree, top, bottom, left, right):
    max_top = int(max(top, default=0))
    max_bottom = int(max(bottom, default=0))
    max_left = int(max(left, default=0))
    max_right = int(max(right, default=0))
    if (int(tree) > max_top) or (int(tree) > max_bottom) or (int(tree) > max_right) or (int(tree) > max_left):
        return 1
    elif int(tree) == 0 and (len(top) == 0 or len(bottom) == 0 or len(left) == 0 or len(right) == 0):
        return 1
    else:
        return 0


def scenic(tree, top, bottom, left, right):
    top_points = 0
    bottom_points = 0
    left_points = 0
    right_points = 0
    tree = int(tree)
    for each in reversed(top):
        if tree <= int(each):
            top_points += 1
            break
        else:
            top_points += 1
    for each in bottom:
        if tree <= int(each):
            bottom_points += 1
            break
        else:
            bottom_points += 1
    for each in reversed(left):
        if tree <= int(each):
            left_points += 1
            break
        else:
            left_points += 1
    for each in right:
        if tree <= int(each):
            right_points += 1
            break
        else:
            right_points += 1
    scenic_score = top_points * bottom_points * right_points * left_points
    return scenic_score


grid = [x.strip() for x in open('input')]
length = len(grid)
silver = 0
gold = 0
for row, trees in enumerate(grid):
    for col, tree in enumerate(trees):
        top = [x[col] for x in grid[0:row]]
        bottom = [x[col] for x in grid[row+1:length]]
        left = [x for x in grid[row]][0:col]
        right = [x for x in grid[row]][col+1:length]
        silver += max_height(tree, top, bottom, left, right)
        gold = max(gold, scenic(tree, top, bottom, left, right))

print(silver)
print(gold)


