import os

from utils.create_sample_data import generate_sample_data
from engine.game import Game



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


Data Map (LAPI Calls)
hero = data/character.json


enemies = data/enemies.json
items = data/enemies.json
skills = data/skills.json
"""


if __name__ == "__main__":

    # generate_sample_data('data/sample_data')

    g = Game('save_config.json')
    g.run()

        
    # Overworld (Exploration/Farming/)
    # Use items
    # Check status
    # Choose path


    # Start with rogue like make into full rpg
