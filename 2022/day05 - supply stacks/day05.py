"""
After the rearrangement procedure completes, what crate ends up on top of each stack?
"""


def last_order(crates):
    top_crates = ''
    for each in crates:
        top_crates += each[0]
    print(top_crates)


def parsing():
    # Change stackSize to the number of stacks there are
    stackSize = 9
    with open("input") as input:
        stacks, lines = input.read().split("\n\n")
    instructions = []
    crates = [[] for _ in range(stackSize)]

    for line in lines.splitlines():
        _, crate, _, origin, _, dest = line.split()
        instructions.append(tuple(map(int, (crate, origin, dest))))

    for stack in stacks.splitlines()[:-1]:
        for i, n in enumerate(stack[1::4]):
            if n != " ":
                crates[i].append(n)
    return crates, instructions


# Silver
crates, instructions = parsing()
for crate, origin, dest in instructions:
    i = 0
    while i < crate:
        crates[dest-1].insert(0,crates[origin-1].pop(0))
        i += 1
last_order(crates)

# Gold
crates, instructions = parsing()
for crate, origin, dest in instructions:
    crane = crates[origin-1][0:crate]
    del crates[origin-1][0:crate]
    crates[dest - 1][0:0] = crane
last_order(crates)