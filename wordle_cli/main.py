import os
import random

from typing import List

from rich import print

from database import load_wordbank



"""
?----------------------------------------------?
* Program: Wordle Clone                        *
* Author: Rickyg3                              *
* Version: 2.0                                 *
?----------------------------------------------?


? [ Version History ]:
?-----------------------------------------------
* - V 2.0 -> Re Design
  - V 1.1 -> Refactor
  - V 1.0 -> Added Rich for console colors
  - V 0.0 -> Base Code
?-----------------------------------------------


? [ Features ]:
?-----------------------------------------------
Todo: Validate User Input
Todo: Decouple Main Game Loop from other code
?-----------------------------------------------
"""


class WordleGame:
    def __init__(self, new_filepath="data/four_letter_wb.txt"):
        self.filepath = new_filepath
        self.word_bank = None
        self.word_length = None
        
        self.load_data()
        self.game_board = self.blank_game_board()

    def __str__(self) -> str:
        txt = f"{self.filepath} Loaded!"
        txt += f"{self.word_length} long"
        return txt

    def blank_game_board(self):
        new_game_board = [['[black on white] [/]' for i in range(self.word_length)] for j in range(6)]
        print(new_game_board)
        return new_game_board
    
    def display_game_board(self):
        final_board = "\n"
        for _, row in enumerate(self.game_board):
            
            for char in row:
                final_board += f"{char} "
            
            if _ == self.word_length:
                break

            final_board += f"\n\n"
        
        print(final_board)
        return final_board
    
    def load_data(self):
        self.word_bank = []
        with open(self.filepath, 'r') as in_words:
            for line in in_words:
                # Parse line if needed
                cleaned_line = line.strip()
                # Add to word bank
                self.word_bank.append(cleaned_line)
                # Record length if not already recorded
                if self.word_length is None:
                    self.word_length = len(cleaned_line)

        return True

    def start_round(self):
        # Num of Guesses = 6
        for _ in range(6):
            self.display_game_board()
            u_input = input("\n>>> ")

            match u_input:
                case 'q':
                    print("\n[ Quit Program ]\n")
                    break
        return   


if __name__ == "__main__":
    cols, rows = os.get_terminal_size()

    filepath = "data/sample_word_bank.txt"
    new_game = WordleGame()

    new_game.start_round()

    print(new_game)
