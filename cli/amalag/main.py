from typing import List, Dict, Callable
from character import Character
from item import Item, Consumable, Equipment


'''
Menu

___________________________________
Name

a] Option #1
b] Option #2
c] Option #3

>>> 
___________________________________

    Data
    [
        {
            'key': '?',
            'display_text': 'Option #?',
            'action': method 
        },
        ... 
    ]

'''


class MenuOption:
    def __init__(self, key: str, display_text: str, action: Callable):
        self.key = key 
        self.display_text = display_text 
        self.action = action

    def __str__(self):
        return f"{self.key}] {self.display_text}"
    
    def export(self):
        return {
            'key': self.key,
            'display_text': self.display_text,
            'action': self.action
        }


class Menu:
    def __init__(self, menu_data: List[MenuOption]):
        self.data = menu_data
        self.map = dict()
        
        for option in menu_data:
            if not isinstance(option, MenuOption):
                continue
            k = option.key
            a = option.action
            self.map[k] = a

    def __str__(self):
        menu_txt = '\n'.join([f'{mo}' for mo in self.data])
        return f"{menu_txt}"
    
    def export(self):
        return [m.export() for m in self.data]
    
    def run(self):
        while True:
            u_in = input(f"{self}\n>>> ")

            match u_in:
                case 'q':
                    break
                case _:
                    func = self.map.get(u_in, None)

                    if func is None:
                        continue

                    func()
                    
        
        return
    


class Game:
    def __init__(self, filename: str='default_appdata.json'):
        self.filename = filename
        self.player = None
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
    
    def scout(self):
        return    
    
    def battle(self, enemies: List):
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
    HERO_DATA = {
        'name': 'Hero',
        'health': 20,
        'attack': 20,
        'defense': 20,
        'speed': 20,
    }
        
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


    # hero = Character(**HERO_DATA)

    # print(hero)

    # potion = Consumable(**POTION_DATA)
    # wood_sword = Equipment(**WOODEN_SWORD)
    # wood_shield = Equipment(**WOODEN_SHIELD)
    

    # hero.equip('left_arm', wood_shield)
    # hero.equip('right_arm', wood_sword)

    # hero.consume(potion)

    # print()
    # print(hero)
    p, e = None, None
    def battle(player, enemies):
        print(player, enemies)
        return
    
    def battle_wrapper():
        return battle(p, e)

    def use_item():
        # Show item choices
        # Parse Choice
        # Use Item
        print('i')
        
    
    def use_skill():
        print('s')


    # Menu
    MENU_DATA = [
        {
            'key': 'a',
            'display_text': 'Attack',
            'action': battle_wrapper 
        },
        {
            'key': 's',
            'display_text': 'Skills/Spells',
            'action': use_skill
        },
        {
            'key': 'i',
            'display_text': 'Item',
            'action': use_item
        },
    ]

    # menu_data = [MenuOption(**m) for m in MENU_DATA]
    # m = Menu(menu_data)

    # m.run()


    g = Game()

    g.run()


