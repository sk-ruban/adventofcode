"""
What would your total score be if everything goes exactly according to your strategy guide?
"""

# Part 1
shapes = {'rock': ['A', 'X'], 'paper': ['B', 'Y'],'scissors': ['C', 'Z']}
wins = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
score_outcome = {'win': 6, 'draw': 3, 'lose': 0}
score_shape = {'rock': 1, 'paper': 2, 'scissors': 3}


def game(selection):
    global score
    x, y = selection
    opponent_choice = [key for key, value in shapes.items() if x in value].pop()
    player_choice = [key for key, value in shapes.items() if y in value].pop()
    score += score_shape[player_choice]
    if player_choice == opponent_choice:
        score += score_outcome['draw']
    elif player_choice == wins[opponent_choice]:
        score += score_outcome['lose']
    else:
        score += score_outcome['win']
    return score


score = 0
strategy = [x.strip() for x in open('input')]
for line in strategy:
    game(tuple(line.replace(" ", "")))
print(score)

# Part 2
results = {'lose': ['X'], 'draw': ['Y'],'win': ['Z']}


def game2(selection):
    global score2
    player_choice = ''
    x, y = selection
    opponent_choice = [key for key, value in shapes.items() if x in value].pop()
    result = [key for key, value in results.items() if y in value].pop()
    if result == 'draw':
        player_choice = opponent_choice
        score2 += score_outcome['draw']
    elif result == 'win':
        player_choice = [key for key, value in wins.items() if opponent_choice in value].pop()
        score2 += score_outcome['win']
    else:
        player_choice = [value for key, value in wins.items() if opponent_choice in key].pop()
        score2 += score_outcome['lose']
    score2 += score_shape[player_choice]

score2 = 0
for line in strategy:
    game2(tuple(line.replace(" ", "")))
print(score2)
