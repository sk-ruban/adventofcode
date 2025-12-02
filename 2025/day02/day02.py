ranges = [(int(a), int(b))
    for pair in open('input').read().strip().split(",")
    for a, b in [pair.split('-')]]
part1 = 0
part2 = 0

for first, last in ranges:
    for i in range(first, last+1):
        id = str(i)
        if len(id) % 2 == 0 and id[:len(id)//2] == id[len(id)//2:]:
            part1 += i
        if id in (id + id)[1:-1]:
            part2 += i

print(part1, part2)
