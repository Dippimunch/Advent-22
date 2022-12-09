filename = 'day2_input.txt'
with open(filename) as f:
    content = f.read().splitlines()

score = 0

shape_points = {'ROCK': 1, 'PAPER': 2, 'SCISSORS': 3}
opponent_chart = {'A': {'LOSE': 'SCISSORS', 'DRAW': 'ROCK', 'WIN': 'PAPER'},
            'B': {'LOSE': 'ROCK', 'DRAW': 'PAPER', 'WIN': 'SCISSORS'},
            'C': {'LOSE': 'PAPER', 'DRAW': 'SCISSORS', 'WIN': 'ROCK'}}
result = None

#print(opponent['A']['LOSE'])

def evaluate_round(opponent_choice, outcome, opponent_chart, shape_points):
    """if opponent == 'A' and choice == 'X':
        result = 'LOSE'
    elif opponent == 'A' and choice == 'Y':
        result = 'DRAW'
    elif opponent == 'A' and choice == 'Z':
        result = 'WIN'

    elif opponent == 'B' and choice == 'X':
        result = 'LOSE'
    elif opponent == 'B' and choice == 'Y':
        result = 'DRAW'
    elif opponent == 'B' and choice == 'Z':
        result = 'WIN'

    elif opponent == 'C' and choice == 'X':
        result = 'LOSE'
    elif opponent == 'C' and choice == 'Y':
        result = 'DRAW'
    elif opponent == 'C' and choice == 'Z':
        result = 'WIN'"""

    score = 0

    if outcome == 'X':
        result = 'LOSE'
        score += 0
    elif outcome == 'Y':
        result = 'DRAW'
        score += 3
    elif outcome == 'Z':
        result = 'WIN'
        score += 6

    player_choice = opponent_chart[opponent_choice][result]
    score += shape_points[player_choice]
    #print(opponent_chart[opponent_choice][result], score)


    """if result == 'LOSE':
        
    elif result == 'DRAW':
        
    elif result == 'WIN':"""
        

    return score

def run(content, score, opponent_chart, shape_points):
    for i in range(len(content)):
        score += evaluate_round(content[i][0], content[i][2], opponent_chart, shape_points)
    print(score)

run(content, score, opponent_chart, shape_points)
#evaluate_round('A', 'Y', opponent_chart, shape_points)
