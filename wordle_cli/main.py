import os
import random

from dataclasses import dataclass
from typing import List


""" 
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
        word_length = len(guess)

        for i in range(word_length):
            if guess[i] == chosen_word[i]:
                status[guess[i]] = True
                continue
        
        print(self.final_status(status))

        return status
    
    def check_win(self, status):
        for letter, is_guessed in status.items():
            if not is_guessed:
                return False
        return True

    def final_status(self, status):
        final_report = "\n"
        for letter, val in status.items():
            stat_symbol = " " if val else "X"
            final_report += f"[{stat_symbol}] "
        return final_report

    def start(self):
        # Choose random word
        r = random.randint(0, self.length-1)
        chosen_word = self.word_bank[r]
        
        blank_status = dict.fromkeys(chosen_word, False)
        current_status = dict.fromkeys(chosen_word, False)

        guessed = False
        max_turn_limit = 6
        
        # Let player Guess
        for i in range(max_turn_limit):
            print(self.final_status(current_status))
            user_input = input(">>> ")

            current_status = self.check_guess(user_input, chosen_word, blank_status)
            guessed = self.check_win(current_status)

            if guessed:
                break
        # Print Results

        if not guessed:
            print(f"Failed!: Word was {chosen_word}")
        else:
            print(f"You Won! {chosen_word}")
        
        print(self.final_status(current_status))


if __name__ == "__main__":
    filepath = "sample_word_bank.txt"
    new_round = Round(filepath)
    new_round.start()

    # print(new_round)













