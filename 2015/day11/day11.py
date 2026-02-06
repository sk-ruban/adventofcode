puzzle = "hxbxwxba"

def increment(pw):
    pw = list(pw)
    i = len(pw) - 1

    while i >= 0:
        if pw[i] == 'z':
            pw[i] = 'a'
            i -= 1
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            break

    return "".join(pw)

def check_password(pw):
    pairs = set()

    if any(c in pw for c in "iol"):
        return False
    if not any(ord(pw[i]) == ord(pw[i+1]) - 1  == ord(pw[i+2]) - 2 for i in range(len(pw) - 2)):
        return False
    pairs = {a for a, b in zip(pw, pw[1:]) if a == b}
    return len(pairs) >= 2

def find_next(pw):
    while True:
        pw = increment(pw)
        if check_password(pw):
            break
    return pw

part1 = find_next(puzzle)
part2 = find_next(part1)

print(part1, part2)
