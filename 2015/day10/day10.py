def look_and_say(times):
    input = "1113222113"

    for _ in range(times):
        out = ""
        prev, count = input[0], 1
        for c in input[1:]:
            if c == prev:
                count += 1
            else:
                out += str(count) + prev
                count = 1
                prev = c

        out += str(count) + prev
        input = out
    return input

part1 = len(look_and_say(40))
part2 = len(look_and_say(50))
print(part1, part2)
