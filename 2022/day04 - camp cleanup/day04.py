"""
In how many assignment pairs does one range fully contain the other?
"""


def splitter(pair, split):
    x, y = tuple(pair.split(split))
    return x, y


def full_range_overlap(first, second):
    x1, x2 = map(int, splitter(first, '-'))
    y1, y2 = map(int, splitter(second, '-'))
    return (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2)


def part_range_overlap(first, second):
    x1, x2 = map(int, splitter(first, '-'))
    y1, y2 = map(int, splitter(second, '-'))
    return (x1 <= y2 and y1 <= x2) or (y1 <= x2 and x1 <= y2)


assignments = [x.strip() for x in open('input')]
count1 = 0
count2 = 0
for pair in assignments:
    first, second = splitter(pair, ',')
    # Part 1
    if full_range_overlap(first, second):
        count1 += 1
    # Part 2
    if part_range_overlap(first, second):
        count2 += 1

print(count1)
print(count2)
