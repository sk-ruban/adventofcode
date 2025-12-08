from collections import Counter
from math import prod

positions = open("input").read().splitlines()
n = len(positions)

boxes = [tuple(map(int, p.split(","))) for p in positions]
parent = list(range(n))

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

def union(x, y):
    nx, ny = find(x), find(y)
    if nx != ny:
        parent[nx] = ny

distances = []
for i in range(n):
    for j in range(i+1, n):
        dist = sum((a - b) ** 2 for a, b in zip(boxes[i], boxes[j]))
        distances.append((dist, i, j))

distances.sort()

for _, i, j in distances[:1000]:
    union(i, j)

sizes = Counter(find(i) for i in range(n))
part1 = prod(count for root, count in sizes.most_common(3))

print(part1)
