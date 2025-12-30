import re
from math import lcm
from functools import reduce

dirs, _, *nodes = open("input").read().strip().split("\n")
network = {}
curr = "AAA"
part1, part2 = 0, 0

for node in nodes:
    match = re.match(r'(\w+) = \((\w+), (\w+)\)', node)
    network[match.group(1)] = (match.group(2), match.group(3))

while curr != "ZZZ":
    dir = dirs[part1 % len(dirs)]
    curr = network[curr][dir == "R"]
    part1 += 1

def find_length(node):
    curr = node
    steps = 0
    while not curr.endswith("Z"):
        dir = dirs[steps % len(dirs)]
        curr = network[curr][dir == "R"]
        steps += 1
    return steps

start_nodes = [node for node in network if node.endswith("A")]
cycle_len = [find_length(node) for node in start_nodes]
part2 = reduce(lcm, cycle_len)

print(part1, part2)
