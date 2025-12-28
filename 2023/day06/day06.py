from math import sqrt, ceil, floor

document = open("input").read().splitlines()
part1 = 1

time = [int(t) for t in document[0].split(": ")[1].split()]
dist = [int(d) for d in document[1].split(": ")[1].split()]

for i in range(len(time)):
    t = time[i]
    d = dist[i] + 1

    b1 = ceil((t - sqrt(t*t - 4*d)) / 2)
    b2 = floor((t + sqrt(t*t - 4*d)) / 2)

    part1 *= (b2 - b1 + 1)

print(part1)
