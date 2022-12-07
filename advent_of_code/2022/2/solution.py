import os

"""
Strategy Guide Key
-----------
A Rock
B Paper
C Scissors

X Rock
Y Paper
Z Scissors
-----------


SCORE Key
---------------
Rock        1
Paper       2
Scissors    3

Lose        0
Draw        3
Win         6
---------------
"""
def read_input(filepath: str) -> str:
    with open(filepath, 'r') as load_file:
        return load_file.read()

def check_win(move, opponent_move):
    win_key = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }

    if move == win_key[opponent_move]:
        return True
    return False


def main():
    #################
    ##  Variables  ##
    #################
    guide_key = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors",
    }
    score_key = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
        "loss": 0,
        "draw": 3,
        "win": 6,
    }

    part_two_key = {
        "X": 0,
        "Y": "draw",
        "Z": 1
    }

    win_key = {
        'rock': 'paper',
        'paper': 'scissors',
        'scissors': 'rock'
    }
    loss_key = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }

    # 0 for loss, 1 for win
    move_key = {
        'rock': ('scissors', 'paper'),
        'paper': ('rock', 'scissors'),
        'scissors': ('paper', 'rock')
    }


    sample_input = """A Y
B X
C Z"""
    ###############
    ##  Part I  ##
    ###############
    # final_input = read_input("input.txt")
    # total_score = 0

    # # Parse Input
    # for line in final_input.split("\n"):
    #     opponent_move, suggested_move = line.split(' ')
    #     opponent_move, suggested_move = guide_key[opponent_move], guide_key[suggested_move] 
    #     print(f"Opponent: {opponent_move}")
    #     print(f"Suggested Move: {suggested_move}")

    #     # Calculate Score
    #     current_score = 0
    #     won = check_win(suggested_move, opponent_move)

    #     if won:
    #         current_score += score_key.get('win', 6)
        
    #     if opponent_move == suggested_move:
    #         current_score += score_key.get('draw', 3)
        
    #     current_score += score_key[suggested_move]
    #     print(current_score)

    #     # Add to Total Score
    #     total_score += current_score

    # print(total_score)

    ###############
    ##  Part II  ##
    ###############
    final_input = read_input("input.txt")
    total_score = 0

    # Parse Input
    for line in final_input.split("\n"):
        opponent_move, outcome = line.split(' ')
        opponent_move, outcome = guide_key[opponent_move], part_two_key[outcome] 
        # print(f"Opponent: {opponent_move}")
        # print(f"Suggested Outcome: {outcome}")

        # Calculate MOve
        if outcome is int:
            suggested_move = move_key[opponent_move][outcome]
        else:
            suggested_move = opponent_move

        # match outcome:
        #     case 'win':
        #         suggested_move = win_key[opponent_move]
        #     case 'draw':
        #         suggested_move = opponent_move
        #     case 'loss':
        #         suggested_move = loss_key[opponent_move]

        # Calculate Score
        current_score = 0

        # Add Outcome
        current_score += score_key.get(outcome, 0)

        # Add Move
        current_score += score_key.get(suggested_move, 0)

        print(current_score)

        # Add to Total Score
        total_score += current_score

    print(total_score)


if __name__ == "__main__":
    main()