from typing import List, Dict, Callable

from utils.menu import Menu, MenuOption
from utils.screen import clear_screen

from game_engine.character import Character
from game_engine.item import Item, Consumable, Equipment, Inventory

'''


'''


POTION_DATA = {
    'key': 'ttrrppid',
    'name': 'Potion',
    'item_type': 'consumable',
    'description': 'Heals a small amount of health.',
    'attributes': {
        'health': 10
    },
}

WOODEN_SWORD = {
    'key': 'ttrrppid',
    'name': 'Wooden Sword',
    'item_type': 'weapon',
    'description': 'A small wooden sword',
    'attributes': {
        'attack': 10,
        'critical_chance': 2
    },   
}

WOODEN_SHIELD = {
    'key': 'ttrrppid',
    'name': 'Wooden Shield',
    'item_type': 'equipment',
    'description': 'A small wooden shield',  # be careful not to get a splinter.
    'attributes': {
        'defense': 8,
        'block_chance': 10
    },
}




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

        # Add starting items
        self.player.equip('left_arm', Equipment(**WOODEN_SWORD))
        self.player.equip('right_arm', Equipment(**WOODEN_SHIELD))

        self.player.inventory.add_multiple(Consumable(**POTION_DATA), 5)


    def __str__(self):
        s = f'{self.filename}'
        return s
    
    def attack_menu(self):
        input("attack")
        return
    
    def skill_menu(self):
        input("use skill")
        return
    
    def item_menu(self):
        items = []

        for _, i in enumerate(self.player.inventory.data):
            k = _
            txt = i.name
            action = lambda : i.use(self.player)

            new_option = MenuOption(
                key=k,
                display_text=txt,
                action=action
            )
            items.append(new_option)
        
        i_menu = Menu('Item Menu', items)
        i_menu.run()
        
        return
    
    def status(self):
        input(self.player)
    
    def scout(self):
        input('scouting...')
        return
    
    def explore_skill_menu(self):
        
        explore_skills_menu = Menu('Explore Skills')
        explore_skills_menu.run()
    
    def overworld_skill_menu(self):
        
        overworld_skill_menu = Menu('Overworld Skills')
        overworld_skill_menu.run()
    
        return
    
    def travel_menu(self):
        
        travel_menu = Menu('Travel Menu')
        travel_menu.run()
    
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

        battle_menu = Menu('Battle', menu_options)
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
                key='sc',
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

        explore_menu = Menu('Exploration', menu_options)
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

        over_menu = Menu('Overworld', menu_options)
        over_menu.run()

        return
    
    def load_menu(self):
        # Read save files
        # Make each save file into menu option
        # Create menu
        # run
        return
    
    def run(self):
        clear_screen()
        title_screen = f"""Press Enter to start game"""
        input(title_screen)
        
        while True:
            clear_screen()
            options = f"""Title Screen
___________________
s)tart Game
l)oad Game
q)uit

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


