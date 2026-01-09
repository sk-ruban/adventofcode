from functools import reduce

sequence = open("input").read().strip().split(",")

def run_hash(word):
    return reduce(lambda curr, c: (curr + ord(c)) * 17 % 256 , word, 0)

part1 = sum(run_hash(step) for step in sequence)
print(part1)
