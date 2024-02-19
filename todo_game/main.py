import os
import json
from enum import Enum

from utils.player import Player
from utils.task import Task

"""
Sample FLow


Main Screen
>>> Input Commands
- Help
- Complete
- Cancel
- Postpone

- Update Task
- Create Task
- Delete Task
- Read/Expand Task Details




Task
- name
- progress bar
    - status
    - current
    - total
- reward
    - gold
    - exp
- tag
- status


Player
- Name
- Level
- Current EXP
- EXP to level up
- Tasks completed
- Total Tasks
- Tasks Lists/Tags
- Current Gold

------ to be added -------
- Class (Mage, Weapon Master, Martial Artist, Sharpshooter)
- Job (Paladin, Theif, Knight, Magic Knight, Alchemist, Pirate)
- Stats
    - HP
    - MP
    - ATK
    - DEF
    - INT
    - DEX
    - SP. DEF
    - SPD
    - LCK


Enemies
- Name
- Level
- Stats
    - HP
    - MP
    - ATK
    - DEF
    - INT
    - DEX
    - SP. DEF
    - SPD
    - LCK
- Moves




"""



sample_view = f"""
lvl.1 | RG | 2/4 Tasks Completed | 0 Gold | 12/35 EXP
[ALL] [WORK] [SELF]

[ ] (WORK) Read Chapter 1 of Cracking the Coding Interview 
    15/34 [**********___________]
    REWARD: 20 EXP + 5G

[*] (WORK) Work on resume
    REWARD: 20 EXP + 5G

[*] (WORK) Work on side project
    REWARD: 20 EXP + 5G

[ ] (WORK) Leet Code Problem
    REWARD: 20 EXP + 5G

*  Completed
   Incomplete
X  Canceled
@  Backlog
"""

#rint(sample_view)



# Create Player
player_data = {
        "name": "Billy Bob",
}


# p1 = Player(**player_data)
p1 = Player()
p1.load_data()


# Create Tasks
# task_data = {
#         "name": "Read 15 pages",
#         "gold": 20,
#         "experience": 25,
#         "tag": "READING",
#         "progress_bar": True,
#         "status": TaskStatus.COMPLETED
# }

# t1 = Task(**task_data)
# t2 = Task("Organize physical space")

# p1.add_tag("READING")
# p1.add_task(t1)
# p1.add_task(t2)


print(p1)
print()
p1.display_tasks()
#rint(t1)
p1.save_data()





