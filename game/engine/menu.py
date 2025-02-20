import os

from typing import Callable, List, Dict, Union

"""
_____________________________

Main Menu
_____________________________

A) Option #1    => Action #1
B) Option #2    => Action #2
C) Option #3    => Action #3
D) Option #4    => Action #4

>>> 

"""

class MenuOption:
    def __init__(self, key: str, display_txt: str, func: Callable):
        self.key = key if isinstance(key, str) else f"{key}"
        self.display_txt = display_txt
        self.function = func

    def run(self):
        self.function()

class Menu:
    def __init__(self, name, data: List[Union[MenuOption, Dict]]=None):
        self.name = name
        self.options = None
        
        if data is not None:    
            is_prebuilt = isinstance(data[0], MenuOption)
            self.options = {i.key: i for i in data} if is_prebuilt else {i['key']: MenuOption(**i) for i in data}

    def __str__(self):
        s = f'{self.name}'
        return s
    
    def run(self):
        console_width = 25
        header = f"""
{'_'*(console_width)}
{self.name:^{console_width}}
{'_'*(console_width)}
"""
        option_txt = "\n".join([f"{k}) {opt.display_txt}" for k, opt in self.options.items()])
        
        while True:
            print(f"""{header}
{option_txt}

""")
            user_input = input(">>> ")

            if user_input == 'q':
                break

            chosen = self.options[user_input]
            chosen.run()


def test():
    def fn1():
        print("fn1 ran!")
    def fn2():
        print("fn2 ran!")
    def fn3():
        print("fn3 ran!")

    # Build Data
    SAMPLE_DATA = []
    functinos = [fn1, fn2, fn3]
    keys = ['a', 'b', 'c']
    for _ in range(3):
        SAMPLE_DATA.append({
            'key': keys[_],
            'display_txt': f"Option #{_}",
            'func': functinos[_]
        })


    # Menu from Raw
    m = Menu("Test Menu 1", data=SAMPLE_DATA)
    m.run()
    

    # Menu from prebuilt
    pb = [MenuOption(**i) for i in SAMPLE_DATA]
    m2 = Menu("Test Menu 2", data=pb)
    m2.run()



if __name__ == "__main__":
    test()
