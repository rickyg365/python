import os
import random

from typing import List
from dataclasses import dataclass

from rich import print

""" 
Bugs:
   Cant use dict because the same letter cant be used as an index


Plan:

4 letter word

[ ] [ ] [ ] [ ] 
>>> {user_guess}

Next Guess:

[ ] [ ] [ ] [ ] 
[ ] [ ] [X] [X]  # Got last 2 letter 
>>> {user_guess}


Next Guess:

[ ] [ ] [ ] [ ] 
[ ] [ ] [X] [X]  # Got last 2 letter 
[X] [ ] [ ] [ ]  # Got first letter
>>> {user_guess}

.
.
.


Final Report:


[ ] [ ] [X] [X] 
[X] [ ] [ ] [ ] 
[X] [ ] [X] [X] 
[X] [ ] [X] [X] 
[X] [X] [X] [X] 

Guessed in 5/6 Trys

"""


def load_wordbank(file_path: str) -> List[str]:
    # Load file in read mode
    with open(file_path, 'r') as in_file:
        word_bank = in_file.read().strip().split("\n")

    return word_bank


class Round:
    def __init__(self, wordbank_path: str):
        self.path = wordbank_path
        self.word_bank = load_wordbank(wordbank_path)
        
        self.length = len(self.word_bank)


    def __repr__(self) -> str:
        items = ""
        for item in self.word_bank:
            items += f" - {item}\n"

        return f"Length of word list: {self.length}\n{items}"
    
    def check_guess(self, guess, chosen_word, status):
        """ Check status of each letter and update the status object """
        new_status = dict.fromkeys(guess, False)
        word_length = len(guess)

        more_than = word_length > 4
        less_than = word_length < 4

        if more_than or less_than:
            return False

        for i in range(word_length):
            if guess[i] == chosen_word[i]:
                status[guess[i]] = True
                new_status[guess[i]] = True
                
                continue

        return status, new_status
    
    def check_win(self, status):
        for letter, is_guessed in status.items():
            if not is_guessed:
                return False
        return True

    def final_status(self, status):
        final_report = ""

        for letter, val in status.items():

            in_word = f'[green]{letter}[/green]'
            not_in_word = f'[red]{letter}[/red]'
            final_report += f"{in_word if val else not_in_word} "

        return final_report

    def start(self):
        # Starting Variables
        # Choose random word
        r = random.randint(0, self.length-1)
        chosen_word = self.word_bank[r]
        
        blank_status = dict.fromkeys(chosen_word, False)
        current_status = dict.fromkeys(chosen_word, False)

        report = ""

        guessed = False
        max_turn_limit = 6
        
        # Intro
        print("Guess the Word!")

        # Let player Guess
        for _ in range(max_turn_limit):
            # Reset Status
            current_status = {**blank_status}


            user_input = input("\n>>> ")
            
            current_status, new_status = self.check_guess(user_input, chosen_word, current_status)
            report += f"\n{self.final_status(new_status)}"
            
            guessed = self.check_win(current_status)

            print(report)
            if guessed:
                break

        if not guessed:
            print(f"\nFailed! Word was {chosen_word}")
            return
        
        # Default is Win
        print(f"\nYou Won! Word was {chosen_word}")


if __name__ == "__main__":
    cols, rows = os.get_terminal_size()

    filepath = "sample_word_bank.txt"
    new_round = Round(filepath)

    while True:
        new_round.start()
        
        cont = input("\nContinue?: ")

        if cont.lower() == 'n':
            break
        
        print(f"{cols*'-'}")
