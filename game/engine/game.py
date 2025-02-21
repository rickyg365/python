import os

from screen import Screen
from menu import Menu, MenuOption

class Game:
    def __init__(self, name: str, width: int=12, height: int=24):
        self.name = name
        self.main_screen = Screen(name, width, height)

    def __str__(self):
        s = f'{self}'
        return s
    
    def build_menus(self):
        # New Game
        # Continue
        # Options/Settings
        ...
    
    def run(self):

        main_menu = Menu("Main Menu", [{
            'key': 'n',
            'display_txt': 'New Game',
            'func': Menu('New Game').run
        }])
        processes = []
        while True:
            pass


if __name__ == "__main__":
    ...
