import os
from engine.game import Game
from models.character import Character, Item, Skill

from utils.ui_elements import text_box
from utils.file_handle import load_json, save_json


"""
Goals:
- Item exp
- Skill exp
- Elemental Attribute exp
- Spell exp


UI

Version 1
____________________________________________________________________
lvl.01 Goblin
HP  15/15  [********************]


lvl.03 Hero
HP  20/20  [********************]
MP   0/0   [                    ]

-----------------------------------------------
| a)ttack | d)efend | e)vade | s)kill | i)tem |
-----------------------------------------------
>>> 
____________________________________________________________________


Version 2
____________________________________________________________________
lvl.01 Goblin
HP  15/15  (--------------------)


lvl.11 Hero
HP  50/50  (--------------------)
MP  15/15  (--------------------)

(a)ttack | (d)efend | (e)vade | (s)kill | (i)tem
>>>
____________________________________________________________________

OVERWORLD
purpose: 
- farming materials to craft better/stronger items
- find battles
- mining ''
- crafting items/equipment to help with battle
- find skills/paths
- Train to boost attributes
- find recipes for crafting


____________________________________________________________________
Name lvl. 00 | 000G | 
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________
____________________________________________________________________



Square
[###############]
[>>>>>>>>>>>>>>>]
[+++++++++++++++]
[===============]


Rounded
(***************)
(@@@@@@@@@@@@@@@)
(###############)
(+++++++++++++++)
(===============)
(---------------)
(---------------)


Action Bar?
[>>>>>>>>>>>>>>>]


"""


def generate_sample_data(save_dir: str=""):
    ITEMS = []
    SKILLS = []

    for _ in range(5):
        new_item = Item(name=f'Item #{_}')
        ITEMS.append(new_item)

    for _ in range(5):
        new_skill = Skill(name=f'Skill #{_}', description=f'This is the description of skill #{_}')
        SKILLS.append(new_skill)

    # Create dir if doesnt exist

    save_json([i.export() for i in ITEMS], f'{save_dir + "/"}items.json')
    save_json([s.export() for s in SKILLS], f'{save_dir + "/"}skills.json')


if __name__ == "__main__":

    generate_sample_data('data')

    g = Game('new_save.json')
    g.run()

        
    # Overworld (Exploration/Farming/)
    # Use items
    # Check status
    # Choose path


    # Start with rogue like make into full rpg
