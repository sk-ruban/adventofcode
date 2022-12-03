measurements = [x.strip() for x in open('input2')]

# Part 1 Counters
part1_length = 0
part1_depth = 0

for each in measurements:
    if each.startswith('forward'):
        x = each.split(" ")
        for_displacement = int(x[1])
        part1_length += for_displacement
    if each.startswith('up'):
        x = each.split(" ")
        up_displacement = int(x[1])
        part1_depth -= up_displacement
    if each.startswith('down'):
        x = each.split(" ")
        down_displacement = int(x[1])
        part1_depth += down_displacement

part1 = part1_length * part1_depth
print(part1)

# Part 2 Counters
part2_length = 0
part2_depth = 0
aim = 0

for each in measurements:
    if each.startswith('forward'):
        x = each.split(" ")
        for_displacement = int(x[1])
        part2_length += for_displacement
        part2_depth += (aim * for_displacement)
    if each.startswith('up'):
        x = each.split(" ")
        up_displacement = int(x[1])
        aim -= up_displacement
    if each.startswith('down'):
        x = each.split(" ")
        down_displacement = int(x[1])
        aim += down_displacement

part2 = part2_length * part2_depth
print(part2)