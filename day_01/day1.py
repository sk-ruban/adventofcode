# int strips the line breaks
measurements = [int(x) for x in open('input')]
print(measurements)

# Counters
part1 = 0
part2 = 0

# Part1
for ind, val in enumerate(measurements):
    if ind == 0:
        continue
    if measurements[ind] > measurements[ind - 1]: part1 += 1

# Part2
for ind, val in enumerate(measurements):
    if len(measurements) - ind < 3:
        break
    new_window = measurements[ind] + measurements[ind + 1] + measurements[ind + 2]
    if ind == 0:
        old_window = new_window
        continue
    if new_window > old_window:
        part2 += 1
    old_window = new_window

print(part1)
print(part2)
