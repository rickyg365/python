import os
import datetime

from utils.task import Task, TaskTracker, DATETIME_FORMAT
from utils.exp_system import ExperienceSystem
from utils.file_handler import load_json, save_json

"""

Should levels unlock features?
- Longer list
- Different Task types
- utilities(pomodoro timer, ...)
- Flexible end time

Pet
- grows as task are finished
- rogue like rpg adv mode

"""


class Program:
    def __init__(self, filename: str=None):
        self.filename = filename
        self.exp = ExperienceSystem()
        self.task_tracker = TaskTracker('backup_task.json')

        self.load()

    def __str__(self) -> str:
        txt = f'''
{self.exp}
{self.task_tracker}
'''
        return txt
    
    def load(self):
        if self.filename is None or not os.path.exists(self.filename):
            return None
        
        data = load_json(self.filename)
        self.task_tracker.tasks = [Task(**item) for item in data]

    def index_selector(self):
        chosen_idx = input("Choose Index: ")
        
        if chosen_idx == '':
            chosen_idx = 0

        return int(chosen_idx)

    def run(self):
        while True:
            print(self)
            user_input = input(">>> ")

            match user_input:
                case 'c':
                    name = input("Name: ")
                    description = input("Description: ")
                    target_date = input(f"Target Date{DATETIME_FORMAT}: ")

                    self.task_tracker.create(name, description, target_date)
                
                case 'r':
                    idx = self.index_selector()

                    chosen = self.task_tracker.read(idx)
                    input(chosen.details())
                
                case 'u':
                    # Choose Task Index
                    idx = self.index_selector()
                    
                    # Choose Target field and data

                    # Update Object
                    self.task_tracker.update(idx)
                
                case 'd':
                    idx = self.index_selector()
                    
                    self.task_tracker.delete(idx)
                
                case 's':
                    d = self.export()

                    save_json(self.filename, d)

                case 'q':
                    break
                
                case _:
                    pass

    def export(self):
        """ Experience System Export

        Returns::

            exp_system : Dict -> ExperienceSystem.export()
            tasks : List -> TaskTracker.export()
        """
        return {
            'exp_system': self.exp.export(),
            'tasks': self.task_tracker.export(),
        }
    


if __name__ == "__main__":
#     sample_task = {
#         'name': "Task #1",
#         'description': "This is the main content of task 1"
#     }

#     sample_raw_list = [
#     {
#         "name": "Task #1",
#         "description": "This is the main content of task 1",
#         "completed": True,
#         "start_date": "2024-11-13 13:33:53",
#         "target_date": None
#     },
#     {
#         "name": "Task #2",
#         "description": "This is the main conent of task 2",
#         "completed": False,
#         "start_date": "2024-11-13 13:34:01",
#         "target_date": None
#     }
# ]


    FILENAME = 'database.json'
    prog = Program(FILENAME)
#     # prog.create(**sample_task)
  
    prog.run()
    # prog.export()


  