import json
from utils.task import Task

class Player:
    def __init__(self, name: str="", level: int=1, total_tasks: int=0, completed_tasks: int=0, gold: int=0, current_experience: int=0, experience_needed: int=35, tags=None, tasks=None):
        if tags is None:
            tags = ["ALL"]
        if tasks is None:
            tasks = []
        self.level = level
        self.name = name
        self.total_tasks = total_tasks
        self.completed_tasks = completed_tasks
        self.gold = gold
        self.current_experience = current_experience
        self.experience_needed = experience_needed
        self.tags = tags
        self.tasks = tasks

    def __str__(self) -> str:
        l = ' '.join([f"[{x}]" for x in self.tags])
        return f"lvl.{self.level} | {self.name} | {self.completed_tasks}/{self.total_tasks} Tasks Completed | {self.gold} Gold | {self.current_experience}/{self.experience_needed} EXP\n{l}"

    def add_tag(self, new_tag:str):
        self.tags.append(new_tag)

    def add_task(self, new_task: Task):
        self.total_tasks += 1
        self.tasks.append(new_task)

    def complete_task(self, task: Task):
        self.completed_tasks += 1
        self.gold += task.gold
        self.current_experience += task.experience

        if self.current_experience >= self.experience_needed:
            self.level += 1
            self.current_experience = self.current_experience%self.experience_needed

    def display_tasks(self):
        for task in self.tasks:
            print(task)

    def save_data(self, file: str="player_save.json"):
        # Create Player
        player_data = {
                "level": self.level,
                "name": self.name,
                "total_tasks": self.total_tasks,
                "completed_tasks": self.completed_tasks,
                "gold": self.gold,
                "current_experience": self.current_experience,
                "experience_needed": self.experience_needed,
                "tags": self.tags,
                "tasks": [task.export() for task in self.tasks]
        }

        with open(file, 'w') as save_buffer:
            json.dump(player_data, save_buffer, indent=4)

    def load_data(self, file: str="player_save.json"):
        raw_data = None
        with open(file, 'r') as load_buffer:
            raw_data = json.load(load_buffer)
        
        self.level = raw_data.get("level", None)
        self.name = raw_data.get("name", None)
        self.total_tasks = raw_data.get("total_tasks", None)
        self.completed_tasks = raw_data.get("completed_tasks", None)
        self.gold = raw_data.get("gold", None)
        self.current_experience = raw_data.get("current_experience", None)
        self.experience_needed = raw_data.get("experience_needed", None)
        self.tags = raw_data.get("tags", None)
        self.tasks = [Task(**task) for task in raw_data.get("tasks", None)]

