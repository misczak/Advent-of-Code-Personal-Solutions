from enum import Enum

class ColumnOne(Enum):
    A = 1
    B = 2
    C = 3

class ColumnTwo(Enum): 
    X = 1
    Y = 2
    Z = 3

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
            # Add the value of the player's choice to the round score
            round_score += ColumnTwo[current_round[1]].value
            # Figure out the result of the round
            round_result = get_result(ColumnOne[current_round[0]].value, ColumnTwo[current_round[1]].value)
            # Add the numeric value of the result of the round to the round score
            round_score += round_result.value
            # Add the round score to the total running score, then reset the round score
            total_score += round_score
            round_score = 0
    return total_score


def get_result(ColumnOne, ColumnTwo):
    match ColumnTwo-ColumnOne:
        case 0:
            return Result.Draw
        case 1:
            return Result.Win
        case 2: 
            return Result.Loss
        case -1:
            return Result.Loss
        case -2:
            return Result.Win
        case _:
            return

print(read_file('input1.txt'))