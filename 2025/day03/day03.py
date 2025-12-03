banks = open("input").read().strip().split("\n")
part1 = part2 = 0

for bank in banks:
    joltage = 0

    for i in range(len(bank)-1):
        for j in range(i+1, len(bank)):
            joltage = max(joltage, int(bank[i] +bank[j]))

    part1 += joltage

print(part1, part2)
