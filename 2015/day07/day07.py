from functools import cache

circuit = open("input").read().splitlines()

rules = {}
for line in circuit:
    lhs, out = line.split(" -> ")
    rules[out] = lhs.split()

@cache
def get(x):
    if x.isdigit(): return int(x)
    tokens = rules[x]

    match tokens:
        case [val]: return get(val)
        case ['NOT', a]: return ~get(a)
        case [a, 'AND', b]: return get(a) & get(b)
        case [a, 'OR', b]: return get(a) | get(b)
        case [a, 'LSHIFT', val]: return get(a) << int(val)
        case [a, 'RSHIFT', val]: return get(a) >> int(val)

part1 = get('a')

get.cache_clear()
rules['b'] = [str(part1)]
part2 = get('a')

print(part1, part2)
