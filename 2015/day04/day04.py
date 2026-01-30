import hashlib

secret = "yzbqklnj"
part1, part2 = None, None

for n in range(1, 100000000):
    hash = secret + str(n)
    key = hashlib.md5(hash.encode())
    digest = key.hexdigest()

    if digest.startswith("00000") and part1 is None:
        part1 = n

    if digest.startswith("000000"):
        part2 = n
        break

print(part1, part2)
