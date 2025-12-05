ranges, available = open("input").read().split("\n\n")

freshList = [ (int(lo), int(hi))
    for line in ranges.split('\n')
    for lo, hi in [line.split('-')]]

ingredients = [int(a) for a in available.strip().split('\n')]

def fresh(x):
    return any(lo <= x <= hi for lo, hi in freshList)

part1 = sum(fresh(id) for id in ingredients)

print(part1)
