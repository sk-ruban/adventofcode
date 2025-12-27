from functools import reduce

almanac = open("input").read().split("\n\n")
seeds = [int(x) for x in almanac[0].split(":")[1].split()]
maps = []

def mapping(num, mapping):
    for dest, source, length in mapping:
        if source <= num < source + length:
            return num + dest - source
    return num

for section in almanac[1:]:
    lines = section.strip().split("\n")[1:]
    tups = []

    for line in lines:
        nums = [int(x) for x in line.split()]
        tups.append(tuple(nums))

    maps.append(tups)

part1 = min(reduce(mapping, maps, seed) for seed in seeds)
print(part1)
