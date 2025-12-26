cards = open("input").read().splitlines()
part1, part2 = 0, 0
copies = [1] * len(cards)

for idx, card in enumerate(cards):
    _, nums = card.split(": ")
    win, own = map(str.split, nums.split("| "))

    common = len(set(win) & set(own))
    part1 += 2 ** (common - 1) if common > 0 else 0

    for i in range(idx + 1, min(idx + common + 1, len(cards))):
        copies[i] += copies[idx]

part2 = sum(copies)
print(part1, part2)
