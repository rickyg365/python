import os
from rich import print as rprint

import rich


class GameBoard:
    def __init__(self, target_word=None, max_num_guesses: int=6):
        self.word_length = len(target_word) if target_word is not None else 0
        self.num_guesses = max_num_guesses
        self.target_word = target_word
        self.guesses = {}  # Key=Guess_#: Value=Guess
        self.game_board = self.blank_game_board()
            
    def __str__(self) -> str:
        """ Uses Current state to return a string containing all data """
        final_board = "\n"
        for _, row in enumerate(self.game_board):
            for char in row:
                final_board += f"{char} "
            
            if _ == self.word_length:
                break

            final_board += f"\n\n"
        
        return final_board
    
    def blank_game_board(self):
        new_game_board = [[f'[#F47983]text[/]' for i in range(self.word_length)] for j in range(self.num_guesses)]
        return new_game_board
    
    def cache_game_board_state(self):
        """ Uses Current state to return a string containing all data """
        final_board = "\n"
        for _, row in enumerate(self.game_board):
            for char in row:
                final_board += f"{char} "
            
            if _ == self.word_length:
                break

            final_board += f"\n\n"
        
        return final_board
    
    def update(self, row, col, new_value):
        return

    def reset(self):
        return

    def undo(self):
        """ Undo the last move TBI """
        return
    
    def redo(self):
        """ Redo the last move """
        return
    


def main():
    new_game_board = GameBoard("test", 3)
    rprint(new_game_board)
    

if __name__ == '__main__':
    main()
