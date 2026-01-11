grid = {complex(i, j): c
    for j, r in enumerate(open("input"))
    for i, c in enumerate(r.strip())
}

def solve(start_pos, start_dir):
    queue = [(start_pos, start_dir)]
    seen = set()

    while queue:
        pos, dir = queue.pop()
        if (pos, dir) in seen or pos not in grid:
           continue
        seen.add((pos, dir))
        match grid[pos]:
            case '|' if dir.real:
                queue.append((pos + 1j, 1j))
                queue.append((pos - 1j, -1j))
            case '-' if dir.imag:
                queue.append((pos + 1, 1))
                queue.append((pos - 1, -1))
            case '\\':
                dir = complex(dir.imag, dir.real)
                queue.append((pos + dir, dir))
            case '/':
                dir = -complex(dir.imag, dir.real)
                queue.append((pos + dir, dir))
            case _:
                queue.append((pos + dir, dir))

    return len(set(pos for pos, dir in seen))

part1 = solve(0, 1)
print(part1)
