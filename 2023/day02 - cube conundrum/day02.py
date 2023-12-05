def check_possible_game(game_id, content):
    for subset in content.split(";"):
        storage = [0, 0, 0]  # rgb
        for cubes in subset.split(","):
            num, colour = cubes.split()
            match colour:
                case "red": storage[0] += int(num)
                case "green": storage[1] += int(num)
                case "blue": storage[2] += int(num)
        if check_lists(storage, max_cubes) is False:
            return 0

    return game_id


def fewest_cubes_of_each_color(content):
    min_cubes = [0, 0, 0]
    for subset in content.split(";"):
        storage = [0, 0, 0]  # rgb
        for cubes in subset.split(","):
            num, colour = cubes.split()
            match colour:
                case "red": storage[0] = max(storage[0], int(num))
                case "green": storage[1] = max(storage[1], int(num))
                case "blue": storage[2] = max(storage[2], int(num))

        min_cubes = [max(min_cubes[i], storage[i]) for i in range(3)]

    return multiply(min_cubes)


def check_lists(list1, list2):
    if len(list1) != len(list2):
        return False
    for num1, num2 in zip(list1, list2):
        if num1 > num2:
            return False
    return True


def multiply(array):
    product = 1
    for ele in array:
        product *= ele
    return product


p1_sum = 0
p2_sum = 0
max_cubes = [12, 13, 14]

with open('input') as file:
    for line in file:
        game, content = line.split(":")
        game_id = int(game[5:])
        p1_sum += check_possible_game(game_id, content)
        p2_sum += fewest_cubes_of_each_color(content)

print(p1_sum)
print(p2_sum)

