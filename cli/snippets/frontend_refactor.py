import os

from typing import List, Dict, Union, Callable

"""

Want

menu = Menu()
menu.add_option("(C)reate", create)  # display_txt: str, func: Callable


"""
class MenuOption:
    def __init__(self, display_txt: str, func: callable, idx: str=None):
        self.idx = idx
        self.display = display_txt
        self.func = func

    def __str__(self):
        return f"{self.idx} {self.display} | {self.func}"
    
    def export(self):
        # Can export func but can only pickle anyways
        return {
            'idx': self.idx,
            'display_txt': self.display,
            'func': self.func
        }


class MenuStatic:
    DEFAULT_QUIT_OPTION = {'display_txt': 'Quit', 'idx': 'q'}
    def __init__(self, options: List[Union[MenuOption, Dict]]=None):
        self.options = options
        self.cache = None

        if options is not None:
            # If given built menu but need to build cache
            if isinstance(options[0], MenuOption):
                self.build_cache()
            
            # when given raw data
            elif isinstance(options[0], Dict):
                self.cache = {}
                rebuilt_options = []
                for _, item in enumerate(self.options):
                    # Grab or default data
                    new_idx = item.get('idx', f"{_}")  # if no idx use number
                    dt = item.get('display_text', "???")
                    f = item.get('func', lambda x: print("function lost"))

                    # Build Object
                    new_item = MenuOption(display_txt=dt, func=f, idx=new_idx)
                    
                    # build cachhe and Rebuild options
                    rebuilt_options.append(new_item)
                    self.cache[new_idx] = new_item

                # Update option to new built
                self.options = rebuilt_options


        # Add Quit Option after initialization
        self.add_option(**self.DEFAULT_QUIT_OPTION)

    def __str__(self):
        # Rebuild cache
 
        # Build Text
        opt_txt = "\n".join([f"{idx}) {option.display}" for idx, option in self.cache.items()])

        s = f'{opt_txt}'
        return s
    
    def build_cache(self, num_entries: int=None, start: int=0):
        if num_entries is None:
            num_entries = len(self.options)

        end_cond = min(start+num_entries, num_entries)
        self.cache = {(f'{_}' if i.idx is None else i.idx): i for _, i in enumerate(self.options[start:end_cond])}
    
    def show_entries(self, num_entries: int, start: int=0):
        self.build_cache(num_entries=num_entries, start=start)
        print(self)

    def show_all(self):
        self.build_cache()
        print(self)
    
    def add_option(self, display_txt: str, func: callable=None, idx: str=None):
        new_idx = f"{len(self.cache) - 1}" if idx is None else idx
        new_item = MenuOption(display_txt, func=func, idx=new_idx)
        self.options.append(new_item)
        self.cache[new_idx] = new_item

    def remove_option(self, idx: str):
        return
    
    def run(self):
        run = True
        
        while run:
            display = f"""Menu
{self}

>>> """
            user_input = input(display)

            # Handle User Input
            chosen_option = self.cache.get(user_input, None)
            
            # Invalid Input
            if chosen_option is None:
                print("Invalid Input")
                continue

            # Quitting also needs to be included default    
            if chosen_option.idx == self.DEFAULT_QUIT_OPTION['idx']:
                print("Quitting")
                run = False
                break
            
            # Success
            chosen_option.func()

    
def main():
    MENU_OPTIONS_RAW = [
        {
            'display_text': "Option 1",
            'func': lambda : print("ran #1"),
        },
        {
            'display_text': "Option 2",
            'func': lambda : print("ran #2"),
        },
        {
            'display_text': "Option 3",
            'func': lambda : print("ran #3")
        },
    ]

    MENU_OPTIONS = [
        MenuOption("Option 1", lambda : print("ran #1")),
        MenuOption("Option 2", lambda : print("ran #2")),
        MenuOption("Option 3", lambda : print("ran #3"))
    ]

    m = MenuStatic(options=MENU_OPTIONS_RAW)
    m.run()


if __name__ == "__main__":
    main()

