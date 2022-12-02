from enum import Enum

class ColumnOne(Enum):
    A = 1
    B = 2
    C = 3

class ColumnTwo(Enum): 
    X = 'Loss'
    Y = 'Draw'
    Z = 'Win'

class Result(Enum):
    Win = 6
    Draw = 3
    Loss = 0


def read_file(filepath):

    current_round = []
    round_score = 0
    total_score = 0

    with open(filepath) as f:
        for line in f:
            # Use strip() to remove new line character at the end of each line
            line = line.strip()
            # Split each round into the individual choices 
            current_round = line.split(" ")
            # Find the desired result of the round
            desired_result = ColumnTwo[current_round[1]].value
            # Figure out what option the player should select
            player_choice = make_result(desired_result, current_round[0])
            # Calculate the round score using the dictated result and the player's choice to meet that result
            round_score += Result[desired_result].value
            round_score += ColumnOne[player_choice].value
            # Add round score to total score, and reset round score 
            total_score += round_score
            round_score = 0
    return total_score

def make_result(result, ColumnOne):
    match result:
        case 'Win':
            if ColumnOne == 'A':
                return 'B'
            else:
                if ColumnOne == 'B':
                    return 'C'
                else:
                    return 'A'
        case 'Draw':
            return ColumnOne
        case 'Loss':
            if ColumnOne == 'A':
                return 'C'
            else:
                if ColumnOne == 'B':
                    return 'A'
                else:
                    return 'B'
        case _:
            return

print(read_file('input1.txt'))