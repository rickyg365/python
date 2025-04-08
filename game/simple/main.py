import os

from character import Character, SAMPLE_CHARACTER_DATA

"""
Screen - Manage Display
Game - Manages State


"""

class Screen:
    EMPTY_CHAR = '|'
    def __init__(self, width: int=40, height: int= 30):
        self.height = height
        self.width = width

        self.data = self.build_data(entry_data=self.EMPTY_CHAR)

    def __str__(self):
        s = self.generate_str()
        return s
    
    def build_data(self, entry_data: str=None):
        return [[entry_data for entry in range(self.width)] for row in range(self.height)]
    
    def generate_str(self):
        # python converts list into str for us!
        return '\n'.join([''.join(r) for r in self.data])


class Game:
    def __init__(self, width: int=40, height: int=30, screen: Screen=None):
        # Game Objects
        self.player = None

        # Status
        self.height = height
        self.width = width

        self.screen = screen if screen is not None else Screen(width=width, height=height-1)

    def __str__(self):
        s = f'{self.screen}'
        return s
    
    def clear_screen(self):
        os.system('cls')
    
    def run(self):
        self.player = Character(**SAMPLE_CHARACTER_DATA)

        while True:
            self.clear_screen()
            print(self)
            user_input = input('>>> ')

            if user_input == 'q':
                break

            if user_input == 'stat':
                print(self.player)
                input()

if __name__ == "__main__":
    GAME_WIDTH, GAME_HEIGHT = os.get_terminal_size()
    
    g = Game(width=GAME_WIDTH, height=GAME_HEIGHT)
    g.run()

