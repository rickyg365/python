import os


class Menu:
    def __init__(self, title: str, config=None):
        self.title = title
        self.config = config
        self.menu = None 
        self.build_from_config()

    def __str__(self):
        s = f'{self.title}'
        return s
    
    def build_from_config(self):
        if self.config is None:
            return
        new = {}
        for _, item in enumerate(self.config):
            k = item.get('key', f'{_}')
            func = item.get('function', lambda x: None)

            new[k] = func
        self.menu = new
    
    def run(self):
        # Game Variables
        G_RUNNING = True

        while G_RUNNING:
            current_display = "Display Empty"
            options = '\n'.join([i.get('display', '') for i in self.config])
            main_menu = f"""{self.title}
{current_display}
__________________________
{options}
"""

            u_in = input(f"{main_menu}>>> ")


            self.menu[u_in]()
            

if __name__ == "__main__":
    def create():
        print("Create")
    def read():
        print("Rreate")
    def update():
        print("Ureate")
    def delete():
        print("Dreate")
    MENU_CONFIG = [
        {
            'display': "(C)reate",
            'function': create,
            'key': 'c'
        },
        {
            'display': "(R)ead",
            'function': read,
            'key': 'r'
        },
        {
            'display': "(U)pdate",
            'function': update,
            'key': 'u'
        },
        {
            'display': "(D)elete",
            'function': delete,
            'key': 'd'
        }
    ]

    m = Menu("New Menu", config=MENU_CONFIG)
    m.run()
