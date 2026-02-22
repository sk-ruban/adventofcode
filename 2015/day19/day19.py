import re

lines, molecule = open("input").read().split("\n\n")
rules = []
molecules = set()

for line in lines.splitlines():
    fst, snd = line.split("=>")
    rules.append((fst.strip(), snd.strip()))

for key, val in rules:
    i = molecule.find(key, 0)
    while i != -1:
        molecules.add(molecule[:i] + val + molecule[i + len(key):])
        i = molecule.find(key, i + 1)

tokens = re.findall(r'[A-Z][a-z]?', molecule)

part1 = len(molecules)
part2 = len(tokens) - 1 - 2 * tokens.count("Rn") - 2 * tokens.count("Y")
print(part1, part2)
