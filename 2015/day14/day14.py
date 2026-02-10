lines = open("input").read().splitlines()
reindeers = []
limit = 2503

def distance(speed, period, rest, t):
    cycles, rem = divmod(t, period + rest)
    dist = cycles * speed * period + speed * min(rem, period)

    return dist
    
for line in lines:
    words = line.split(" ")
    speed, period, rest = int(words[3]), int(words[6]), int(words[13])
    reindeers.append((speed, period, rest))

scores = [0] * len(reindeers)
for t in range(1, limit+1):
    dists = [distance(*r, t) for r in reindeers]
    highscore = max(dists)
    for i, r in enumerate(dists):
        if r == highscore:
            scores[i] += 1

part1 = max(distance(*r, limit) for r in reindeers)
part2 = max(scores)
print(part1, part2)       
        
