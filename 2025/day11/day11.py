from functools import cache

input = open("input").read().splitlines()
devices = {}

@cache
def paths(node, dac, fft):
    match node:
        case "out":
            return dac and fft
        case "dac":
            dac = 1
        case "fft":
            fft = 1

    return sum(paths(i, dac, fft) for i in devices[node])

for line in input:
    parts = line.split()
    source = parts[0][:-1]
    targets = parts[1:]
    devices[source] = targets

part1 = paths("you", 1, 1)
part2 = paths("svr", 0, 0)

print(part1, part2)
