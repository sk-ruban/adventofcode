file = open('2024/day03/input').read()

part1 = 0
part2 = 0
enabled = True

i = 0 
while i < len(file):
    if file[i:i+4] == "do()":
        enabled = True
    elif file[i:i+7] == "don't()":
        enabled = False
    elif file[i:i+4] == "mul(":
        if (end := file.find(')', i)) != -1:
            try: 
                x, y = map(int, file[i+4:end].split(','))
                if 1 <= len(str(x)) <= 3 and 1 <= len(str(y)) <= 3:  
                    part1 += x * y
                    if enabled:
                        part2 += x * y
            except:
                pass
    i += 1

print(part1)
print(part2)