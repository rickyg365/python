import os
import random

from typing import List

from rich import print

from database import load_wordbank


class ReferenceWord:
    def __init__(self, reference_word: str):
        self.reference = reference_word
        self.reference_length = len(reference_word)

        self.blank_status = ["not in" for _ in range(self.reference_length)]

    def compare(self, new_word: str):
        new_status = [*self.blank_status]
        if len(new_word) != self.reference_length:
            # Invalid Entry
            return self.blank_status
        
        for _ in range(self.reference_length):
            if new_word[_] in self.reference:
                new_status[_] = "in"

            if self.reference[_] == new_word[_]:
                new_status[_] = "match"
        
        return new_status
    
    def display_comparison(self, word, status):
        final_report = ""

        for _, letter in enumerate(word):
            match = f'[green]{letter}[/green]'
            in_word = f"[yellow]{letter}[/yellow]"
            not_in = f'[red]{letter}[/red]'

            match status[_]:
                case "match":
                    final_report += f"{match} "
                case "in":
                    final_report += f"{in_word} "
                case "not in":
                    final_report += f"{not_in} "

        return final_report


class WordleMatch:
    def __init__(self, custom_path: str="default_wordbank.txt"):
        self.path = custom_path
        self.word_bank = load_wordbank(custom_path)
        
        self.length = len(self.word_bank)
        self.max_guesses = 6

        self.guesses = []
        self.win_status = False


    def __repr__(self) -> str:
        items = f"Length of word list: {self.length}\n"
        for item in self.word_bank:
            items += f" - {item}\n"
        return items
    
    def check_win(self, status):
        for indv in status:
            if indv != "match":
                return False
        return True

    

    def start(self):
        # Choose random word
        r = random.randint(0, self.length-1)
        chosen_word = ReferenceWord(self.word_bank[r])

        current_display = ""
        self.win_status = False
        
        # Intro
        print("Guess the Word!")

        # Let player Guess
        for _ in range(self.max_guesses):
            
            user_input = input("\n>>> ")
            
            current_status = chosen_word.compare(user_input)

            current_display += f"\n{chosen_word.display_comparison(user_input, current_status)}"
            
            self.guesses.append( f"{chosen_word.display_comparison(user_input, current_status)}")
            
            print(current_display)

            guessed = self.check_win(current_status)
            if guessed:
                break

        if not guessed:
            print(f"\nFailed! Word was {chosen_word.reference}")
            return
        
        # Default is Win
        print(f"\nYou Won! Word was {chosen_word.reference}")


if __name__ == "__main__":
    cols, rows = os.get_terminal_size()

    filepath = "sample_word_bank.txt"
    new_round = WordleMatch(filepath)

    while True:
        new_round.start()
        
        cont = input("\nContinue?: ")

        quit_conditions = ['n', 'q']

        if cont.lower() in quit_conditions:
            break
        
        print(f"{cols*'-'}")
