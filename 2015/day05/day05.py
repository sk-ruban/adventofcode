strings = open("input").read().splitlines()

def is_nice(s):
    vowels = sum(c in "aeiou" for c in s)
    doubles = any(a == b for a, b in zip(s, s[1:]))
    excluded = any(x in s for x in ["ab", "cd", "pq", "xy"])

    return vowels >= 3 and doubles and not excluded

def is_nice2(s):
    doubles = any(a == b for a, b in zip(s, s[2:]))
    pairs = any(s.find(a + b, i + 2) >= 1 for i, (a, b) in enumerate(zip(s, s[1:])))

    return doubles and pairs

part1 = sum(map(is_nice, strings))
part2 = sum(map(is_nice2, strings))

print(part1, part2)
