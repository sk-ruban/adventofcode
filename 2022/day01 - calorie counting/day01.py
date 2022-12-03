"""
Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""
calories = [x.strip() for x in open('input')]
elves = []
elf = 0
for item in calories:
    try:
        elf += int(item)
    except:
        elves.append(elf)
        elf = 0

# Part One
print(max(elves))
# Part Two
print(sum(sorted(elves, reverse=True)[:3]))

