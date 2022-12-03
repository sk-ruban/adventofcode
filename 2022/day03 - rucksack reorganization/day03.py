"""
What is the sum of the priorities of those item types?
"""


# Part 1
# Convert from Char to ASCII
def priority(items):
    priorities = 0
    for item in items:
        if item.islower():
            priorities += ord(item) - 96
        else:
            priorities += ord(item) - 64 + 26
    print(priorities)


contents = [x.strip() for x in open('input')]
common = []
for rucksack in contents:
    firsts = rucksack[0:int(len(rucksack)/2)]
    seconds = rucksack[int(len(rucksack)/2):len(rucksack)]
    compartments = [firsts, seconds]
    common.extend(set.intersection(*map(set, compartments)))

    """
    Another less elegant method for Part 1
        try:
        for each in firsts:
            for letter in seconds:
                if each == letter:
                    common.append(each)
                    raise each
    except:
        pass
    """

priority(common)

# Part 2
common = []
start = 0
end = 3
while end <= len(contents):
    group = contents[start:end]
    start += 3
    end += 3
    common.extend(set.intersection(*map(set, group)))

priority(common)


