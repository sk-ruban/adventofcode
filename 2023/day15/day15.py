from functools import reduce

sequence = open("input").read().strip().split(",")

def hash(word):
    return reduce(lambda curr, c: (curr + ord(c)) * 17 % 256 , word, 0)

part1 = sum(map(hash, sequence))
print(part1)

boxes = [dict() for _ in range(256)]

for step in sequence:
    match step.strip('-').split('='):
        case [label, focal]: boxes[hash(label)][label] = int(focal)
        case [label]       : boxes[hash(label)].pop(label, None)

part2 = sum(box * idx * slots[slot] for box, slots in enumerate(boxes, 1) for idx, slot in enumerate(slots, 1))
print(part2)
