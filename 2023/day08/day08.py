import re

dirs, _, *nodes = open("input").read().strip().split("\n")
network = {}
curr = "AAA"
part1 = 0

for node in nodes:
    match = re.match(r'(\w+) = \((\w+), (\w+)\)', node)
    network[match.group(1)] = (match.group(2), match.group(3))

while curr != "ZZZ":
    dir = dirs[part1 % len(dirs)]
    curr = network[curr][dir == "R"]
    part1 += 1

print(part1)
