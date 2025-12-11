input = open("input").read().splitlines()
devices = {}

def paths(node):
    if node == "out":
        return 1
    return sum(paths(i) for i in devices[node])

for line in input:
    parts = line.split()
    source = parts[0][:-1]
    targets = parts[1:]
    devices[source] = targets

part1 = paths("you")
print(part1)
