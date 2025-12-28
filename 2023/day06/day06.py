from math import sqrt, ceil, floor, prod

document = open("input").read().splitlines()
time = document[0].split(": ")[1].split()
dist = document[1].split(": ")[1].split()

def ways(t, d):
    d += 1
    b1 = ceil((t - sqrt(t*t - 4*d)) / 2)
    b2 = floor((t + sqrt(t*t - 4*d)) / 2)
    return b2 - b1 + 1

part1 = prod(ways(int(t), int(d)) for t, d in zip(time, dist))
part2 = ways(int("".join(time)), int("".join(dist)))

print(part1, part2)
