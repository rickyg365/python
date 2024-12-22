from typing import List, Dict, Callable

from menu import Menu, MenuOption

from character import Character
from item import Item, Consumable, Equipment, Inventory

'''


'''

class Game:
    STARTING_HERO_DATA = {
        'name': 'Hero',
        'health': 20,
        'attack': 20,
        'defense': 20,
        'speed': 20,
    }
    def __init__(self, filename: str='default_appdata.json'):
        self.filename = filename
        self.player = Character(**self.STARTING_HERO_DATA)
        self.enemies = []
    
    def __str__(self):
        s = f'{self.filename}'
        return s
    
    def attack_menu(self):
        return
    
    def skill_menu(self):
        return
    
    def item_menu(self):
        return
    
    def explore_skill_menu(self):
        return
    
    def overworld_skill_menu(self):
        return
    
    def travel_menu(self):
        return
    
    def status(self):
        print(self.player)
    
    def scout(self):
        return    
    
    def battle(self, enemies: List[Character]):
        '''
        Attack
        Skill
        Item
        '''
        menu_options = [
            MenuOption(
                key='a',
                display_text='Attack',
                action=self.attack_menu
            ),
            MenuOption(
                key='s',
                display_text='Skill',
                action=self.skill_menu
            ),
            MenuOption(
                key='i',
                display_text='Item',
                action=self.item_menu
            ),
        ]

        battle_menu = Menu(menu_options)
        battle_menu.run()
        return    

    def explore_menu(self):
        '''
        Battle
        Scout
        Item
        Skill
        Status
        '''
        enemies = [None]
        battle_wrapper = lambda : self.battle(enemies)
        menu_options = [
            MenuOption(
                key='b',
                display_text='Battle',
                action=battle_wrapper
            ),
            MenuOption(
                key='s',
                display_text='Scout',
                action=self.scout
            ),
            MenuOption(
                key='i',
                display_text='Item',
                action=self.item_menu
            ),
            MenuOption(
                key='s',
                display_text='Skill',
                action=self.explore_skill_menu
            ),
            MenuOption(
                key='stat',
                display_text='Status',
                action=self.status
            ),
        ]

        explore_menu = Menu(menu_options)
        explore_menu.run()
        return
    
    def overworld_menu(self):
        '''
        Explore
        Item
        Skill
        Travel
        '''
        menu_options = [
            MenuOption(
                key='e',
                display_text='Explore',
                action=self.explore_menu
            ),
            MenuOption(
                key='i',
                display_text='Item',
                action=self.item_menu
            ),
            MenuOption(
                key='s',
                display_text='Skill',
                action=self.overworld_skill_menu
            ),
            MenuOption(
                key='t',
                display_text='Travel',
                action=self.travel_menu
            ),
        ]

        over_menu = Menu(menu_options)
        over_menu.run()

        return
    
    def load_menu(self):
        return
    
    def run(self):
        input("Press Enter to start game >>> ")
        
        while True:
            options = f"""
Start Game
Load Game
Quit
>>> """
            u_in = input(options)

            match u_in:
                case 'q':
                    break
                case 's':
                    self.overworld_menu()
                case 'l':
                    self.load_menu()
                case _:
                    pass
    


if __name__ == "__main__":

    g = Game()
    g.run()


