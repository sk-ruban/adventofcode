"""
What is the sum of these six signal strengths?
"""


def check_cycle():
    global cycle, x, strength
    cycle += 1
    match cycle:
        case 20 | 60 | 100 | 140 | 180 | 220:
            strength += (x * cycle)
    if abs((cycle - 1) % 40 - x) < 2:
        crt[(cycle - 1) // 40][(cycle - 1) % 40] = "#"


cpu = [x.split() for x in open('input')]
cycle = 0
x = 1
crt = [[" " for _ in range(40)] for _ in range(6)]
strength = 0
for instruction in cpu:
    if instruction[0] == 'noop':
        check_cycle()
    else:
        check_cycle()
        check_cycle()
        x += int(instruction[1])

# silver
print(strength)
# gold
for line in crt:
    print("".join(line))