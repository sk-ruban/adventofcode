file = open('2024/day05/input').read()
rulesText, updatesText = file.strip().split('\n\n')

part1 = 0
part2 = 0

rules = {tuple(map(int, r.split('|'))) for r in rulesText.splitlines()}
updates = [list(map(int, u.split(','))) for u in updatesText.splitlines()]

for update in updates:
    pages = set(update)
    valid = True

    for before, after in rules:
        if before in pages and after in pages:
            b = update.index(before)
            a = update.index(after)
            if b > a:
                valid = False
                break
    
    if valid: 
        part1 += update[len(update) // 2]
    else:
        swap = True
        nums = update.copy()
        while swap:
            swap = False
            for i in range(len(nums) - 1):
                for j in range(i+1, len(nums)):
                    if (nums[j], nums[i]) in rules:
                        nums[i], nums[j] = nums[j], nums[i]
                        swap = True
        part2 += nums[len(nums) // 2]

print(part1)
print(part2)