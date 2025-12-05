ranges, available = open("input").read().split("\n\n")

freshList = [ (int(lo), int(hi))
    for line in ranges.split('\n')
    for lo, hi in [line.split('-')]]

ingredients = [int(a) for a in available.strip().split('\n')]

def fresh(x):
    return any(lo <= x <= hi for lo, hi in freshList)

part1 = sum(fresh(id) for id in ingredients)

freshList.sort()
combined = []

for lo, hi in freshList:
    if combined and lo <= combined[-1][1]:
        combined[-1] = (combined[-1][0], max(combined[-1][1], hi))
    else:
        combined.append((lo, hi))

part2 = sum(hi - lo + 1 for lo, hi in combined)

print(part1, part2)
