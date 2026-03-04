best = float('inf')

def tick(boss_hp, mana, shield_t, poison_t, recharge_t):
    armour = 0
    if shield_t > 0: armour = 7; shield_t -= 1
    if poison_t > 0: boss_hp -= 3; poison_t -= 1
    if recharge_t > 0: mana += 101; recharge_t -= 1
    return boss_hp, mana, armour, shield_t, poison_t, recharge_t

spells = [
    (53, 'missile'),
    (73, 'drain'),
    (113, 'shield'),
    (173, 'poison'),
    (229, 'recharge'),
]

def solve(player_hp, mana, boss_hp, shield_t, poison_t, recharge_t, spent, part2):
    global best

    if part2:
        player_hp -= 1
        if player_hp <= 0: return float('inf')

    boss_hp, mana, _, shield_t, poison_t, recharge_t = tick(boss_hp, mana, shield_t, poison_t, recharge_t)
    if boss_hp <= 0: return spent

    for cost, name in spells:
        if spent + cost >= best : continue
        if mana < cost: continue
        if name == 'shield' and shield_t > 0: continue
        if name == 'poison' and poison_t > 0: continue
        if name == 'recharge' and recharge_t > 0: continue

        new_mana, new_boss_hp, new_player_hp = mana - cost, boss_hp, player_hp
        new_shield_t, new_poison_t, new_recharge_t = shield_t, poison_t, recharge_t
        new_spent = spent + cost

        if name == 'missile':  new_boss_hp -= 4
        elif name == 'drain':  new_boss_hp -= 2; new_player_hp += 2
        elif name == 'shield': new_shield_t = 6
        elif name == 'poison': new_poison_t = 6
        elif name == 'recharge': new_recharge_t = 5

        if new_boss_hp <= 0:
            best = min(best, new_spent)
            continue

        new_boss_hp, new_mana, armour, new_shield_t, new_poison_t, new_recharge_t = tick(new_boss_hp, new_mana, new_shield_t, new_poison_t, new_recharge_t)
        if new_boss_hp <= 0:
            best = min(best, new_spent)
            continue

        new_player_hp -= max(9 - armour, 1)
        if new_player_hp <= 0: continue

        solve(new_player_hp, new_mana, new_boss_hp, new_shield_t, new_poison_t, new_recharge_t, new_spent, part2)

    return best

part1 = solve(50, 500, 58, 0, 0, 0, 0, False)
best = float('inf')
part2 = solve(50, 500, 58, 0, 0, 0, 0, True)
print(part1, part2)
