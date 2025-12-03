banks = open("input").read().strip().split("\n")

def solve(length):
    joltage = 0

    for bank in banks:
        best = []
        remainder = bank

        for i in range(length):
            window = len(remainder) - length + i + 1
            best_digit = max(remainder[:window])
            remainder = remainder[remainder.index(best_digit) + 1:]
            best.append(best_digit)

        joltage += int("".join(best))

    return joltage

print(solve(2), solve(12))
