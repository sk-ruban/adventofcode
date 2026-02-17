import operator

tape = {}
for line in open("tape"):
    item, count = line.split(": ")
    tape[item] = int(count)

comparators = {
    "cats": operator.gt,
    "trees": operator.gt,
    "pomeranians": operator.lt,
    "goldfish": operator.lt,
}

for line in open("input"):
    part1, part2 = True, True
    name, rest = line.split(": ", 1)
    num = name.split(" ")[1]
    props = {item: int(count) for item, count in (p.split(": ") for p in rest.split(", "))}

    if all(props[item] == tape[item] for item in props):
        print(f"Part 1: {num}")

    if all(comparators.get(item, operator.eq)(props[item], tape[item]) for item in props):
        print(f"Part 2: {num}")
