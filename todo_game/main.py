import os
from enum import Enum


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

class TaskStatus(Enum):
    COMPLETED = '*'
    INCOMPLETE = ' '
    CANCELED = 'X'
    POSTPONED = '@'


class Task:
    def __init__(self, name: str, tag: str="ALL", gold: int=15, experience: int=20, progress_bar: bool=False, status: TaskStatus=TaskStatus.INCOMPLETE):
        self.name = name
        self.tag = tag
        self.gold_value = gold
        self.experience_value = experience
        self.progress_bar = progress_bar
        self.progress = 0
        self.total_progress = 20
        self.status = status  # Enum: COMPLETED | INCOMPLETE | CANCELED | POSTPONED

    def __str__(self) -> str:
        p = ""
        if self.progress_bar:
            diff = self.total_progress - self.progress
            p = f"\n    {self.progress}/{self.total_progress} [{self.progress * '*'}{diff * ' '}]"
        return f"[{self.status.value}] ({self.tag}) {self.name}{p}\n    REWARD: {self.experience_value} EXP + {self.gold_value}G\n"


class Player:
    def __init__(self, name: str):
        self.level = 1
        self.name = name
        self.total_tasks = 0
        self.completed_tasks = 0
        self.gold = 0
        self.current_experience = 0
        self.experience_needed = 35
        self.tags = ["ALL"]
        self.tasks = []

    def __str__(self) -> str:
        l = ' '.join([f"[{x}]" for x in self.tags])
        return f"lvl.{self.level} | {self.name} | {self.completed_tasks}/{self.total_tasks} Tasks Completed | {self.gold} Gold | {self.current_experience}/{self.experience_needed} EXP\n{l}"

    def add_tag(self, new_tag:str):
        self.tags.append(new_tag)

    def add_task(self, new_task: Task):
        self.tasks.append(new_task)

    def complete_task(self, task: Task):
        self.gold += task.gold_value
        self.current_experience += task.experience_value

        if self.current_experience >= self.experience_needed:
            self.level += 1
            self.current_experience = self.current_experience%self.experience_needed

    def display_tasks(self):
        for task in self.tasks:
            print(task)



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
        "name": "Wreck it Ralph"
}


p1 = Player(**player_data)


# Create Tasks
task_data = {
        "name": "Read 15 pages",
        "gold": 20,
        "experience": 25,
        "tag": "READING",
        "progress_bar": True,
        "status": TaskStatus.POSTPONED
}

t1 = Task(**task_data)
t2 = Task("Organize physical space")

p1.add_tag("READING")
p1.add_task(t1)
p1.add_task(t2)


print(p1)
print()
p1.display_tasks()
#rint(t1)






