"""
What is the sum of the total sizes of those directories?
"""
# I'm going to be honest, i tried using recursion and failed badly.
# Saw a solution on reddit and tried using it here

from collections import defaultdict
from itertools import accumulate


directory = defaultdict(int)
path = []

for command in open('input'):
    match command.split():
        case '$', 'cd', '/':
            path.append('')
        case '$', 'cd', '..':
            path.pop()
        case '$', 'cd', x:
            path.append(x+'/')
        case '$', 'ls': pass
        case 'dir', _: pass
        case size, _:
            for p in accumulate(path):
                directory[p] += int(size)

silver = sum(s for s in directory.values() if s <= 100_000)
gold = min(s for s in directory.values() if s >= directory[''] - 40_000_000)

print(silver, gold)
