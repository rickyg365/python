from typing import List, Dict, Callable
from utils.screen import clear_screen


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
        return f"{self.key}) {self.display_text}"
    
    def export(self):
        return {
            'key': self.key,
            'display_text': self.display_text,
            'action': self.action
        }


class Menu:
    def __init__(self, menu_name: str='Menu', menu_data: List[MenuOption]=None):
        self.data = menu_data
        self.map = dict()
        self.menu_name = menu_name
        if menu_data is not None:
            for option in menu_data:
                if not isinstance(option, MenuOption):
                    continue
                k = option.key
                a = option.action
                self.map[k] = a

    def __str__(self):
        menu_txt = ""
        if self.data is not None:
            menu_txt = '\n'.join([f'{mo}' for mo in self.data])
        
        return f"""{self.menu_name}
_________________________
{menu_txt}
"""
    
    def export(self):
        return [m.export() for m in self.data]
    
    def run(self):
        while True:
            clear_screen()
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
    
if __name__ == "__main__":
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

    menu_data = [MenuOption(**m) for m in MENU_DATA]
    m = Menu(menu_data)

    m.run()
