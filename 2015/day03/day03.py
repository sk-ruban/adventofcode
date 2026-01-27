from itertools import accumulate

dirs = { '>': 1, '<': -1, '^': 1j, 'v': -1j }
steps = [dirs.get(d, 0) for d in open("input").read()]

part1 = len(set(accumulate(steps, initial=0)))

santa = set(accumulate(steps[0::2], initial=0))
robo_santa = set(accumulate(steps[1::2], initial=0))
part2 = len(santa | robo_santa)

print(part1, part2)
