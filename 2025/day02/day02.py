ranges = [(int(a), int(b))
    for pair in open('input').read().strip().split(",")
    for a, b in [pair.split('-')]]
part1 = 0

for id in ranges:
    first, last = id[0], id[1]
    for i in range(first, last+1):
        id = str(i)
        if len(id) % 2 == 0 and id[:len(id)//2] == id[len(id)//2:]:
            part1 += i

print(part1)
