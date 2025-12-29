import math
from collections import Counter

ORDER = "AKQJT98765432"
JOKERS = "AKQT98765432J"

def entropy(hand):
    prob = [freq / 5 for freq in Counter(hand).values()]
    return -sum(p * math.log(p) for p in prob)

def entropy_jokers(hand):
    if hand == "JJJJJ" or 'J' not in hand:
        return entropy(hand)

    new_hand = hand.replace('J', '')
    common = Counter(new_hand).most_common(1)[0][0]
    return entropy(hand.replace('J', common))

def sort_key(hand, jokers):
    if jokers:
        return (entropy(hand), *[ORDER.index(c) for c in hand])
    else:
        return (entropy_jokers(hand), *[JOKERS.index(c) for c in hand])

input = open("input").read().splitlines()
hands = [(hand, int(bid)) for line in input for hand, bid in [line.split()]]

sorted_hands = sorted(hands, key=lambda h: sort_key(h[0], True), reverse = True)
part1 = sum(bid * (idx + 1) for idx, (_, bid) in enumerate(sorted_hands))

sorted_hands = sorted(hands, key=lambda h: sort_key(h[0], False), reverse = True)
part2 = sum(bid * (idx + 1) for idx, (_, bid) in enumerate(sorted_hands))

print(part1, part2)
