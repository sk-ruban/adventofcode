from math import prod

games = open("input").read().splitlines()
part1, part2 = 0, 0
limits = {"red" : 12, "green" : 13, "blue" : 14}

for game in games:
    game_id, subgames = game.split(": ")
    id = int(game_id.split()[-1])

    counts = {"red" : 0, "green" : 0, "blue" : 0}
    valid = True

    for grab in subgames.split("; "):
        for cubes in grab.split(", "):
            num, colour = cubes.split()
            count = int(num)
            counts[colour] = max(counts[colour], count)

            if count > limits[colour]:
                valid = False

    if valid:
        part1 += id
    part2 += prod(counts.values())

print(part1, part2)
