cards = open("input").read().splitlines()
part1 = 0

for card in cards:
    id, nums = card.split(": ")
    winning, own = nums.split("| ")

    winning = winning.split()
    own = own.split()

    common = len(set(winning) & set(own))
    part1 += 2 ** (common - 1) if common > 0 else 0

print(part1)
