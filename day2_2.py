filename = 'day2_input.txt'
with open(filename) as f:
    content = f.read().splitlines()

score = 0

shape = {'X': 1, 'Y': 2, 'Z': 3}
result = None

def evaluate_round(opponent, choice, score):
    if opponent == 'A' and choice == 'X':
        result = 'DRAW'
    elif opponent == 'A' and choice == 'Y':
        result = 'WIN'
    elif opponent == 'A' and choice == 'Z':
        result = 'LOSE'

    elif opponent == 'B' and choice == 'X':
        result = 'LOSE'
    elif opponent == 'B' and choice == 'Y':
        result = 'DRAW'
    elif opponent == 'B' and choice == 'Z':
        result = 'WIN'

    elif opponent == 'C' and choice == 'X':
        result = 'WIN'
    elif opponent == 'C' and choice == 'Y':
        result = 'LOSE'
    elif opponent == 'C' and choice == 'Z':
        result = 'DRAW'

    if choice == 'X':
        score += 1
    elif choice == 'Y':
        score += 2
    elif choice == 'Z':
        score += 3

    if result == 'LOSE':
        score += 0
    elif result == 'DRAW':
        score += 3
    elif result == 'WIN':
        score += 6

    return score

def run(content, score):
    for i in range(len(content)):
        score = evaluate_round(content[i][0],content[i][2], score)
    print(score)

run(content, score)
