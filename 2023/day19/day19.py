import re
from collections import defaultdict

workflow_list, part_list = open("input").read().split("\n\n")
workflows = defaultdict(list)
parts = []

for line in workflow_list.splitlines():
    name, rest = line.split('{')
    rules = rest[:-1].split(',')
    for rule in rules:
        m = re.match(r'([xmas])([<>])(\d+):(\w+)', rule)
        if m:
            var, op, limit, dest = m.groups()
            workflows[name].append((var, op, int(limit), dest))
        else:
            workflows[name].append((None, None, None, rule))

for line in part_list.splitlines():
    part = {}
    for item in line[1:-1].split(','):
        p, r = item.split('=')
        part[p] = int(r)
    parts.append(part)

part1 = 0
for part in parts:
    dest = 'in'
    while dest not in ('A', 'R'):
        for var, op, limit, dest in workflows[dest]:
            if var is None:
                break
            elif op == '<' and part[var] < limit:
                break
            elif op == '>' and part[var] > limit:
                break
        if dest == 'A':
            part1 += sum(part.values())

print(part1)
