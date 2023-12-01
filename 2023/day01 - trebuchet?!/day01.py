total = 0

file = [x.strip() for x in open('input')]

for line in file:

    digitised = line.replace("one", "o1e")\
        .replace("two", "t2o")\
        .replace("three", "th3ee")\
        .replace("four", "fo4r")\
        .replace("five", "fi5e")\
        .replace("six", "s6x")\
        .replace("seven", "se7en")\
        .replace("eight", "ei8ht")\
        .replace("nine", "ni9e")\

    digits = [char for char in digitised if char.isdigit()]

    if len(digits) == 0:
        continue
    elif len(digits) == 1:
        total += int(digits[0] * 2)
    else:
        total += int(digits[0] + digits[-1])

print(total)
