doc = open("input").read().splitlines()
part1, part2 = 0, 0

for line in doc:
    replacements = [
        ("one","o1e"), ("two","t2o"), ("three","th3ee"),
        ("four","fo4r"), ("five","fi5e"), ("six","s6x"),
        ("seven","se7en"), ("eight","ei8ht"), ("nine","ni9e")
    ]

    digits = [char for char in line if char.isdigit()]
    part1 += int(digits[0] + digits[-1])

    for word, digit in replacements:
        line = line.replace(word, digit)

    digits = [char for char in line if char.isdigit()]
    part2 += int(digits[0] + digits[-1])

print(part1, part2)
