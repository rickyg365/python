import os
import datetime

from dataclasses import dataclass, field

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

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


@dataclass
class Task:
    name: str
    description: str=""
    completed: bool=False
    start_date: datetime.datetime=field(default_factory=datetime.datetime.now)
    target_date: datetime.datetime=None
    last_updated: datetime.datetime=None

    def __str__(self) -> str:
        return f''

    def update(self, target, data):
        self.last_updated = datetime.datetime.now()

        match target:
            case 'name':
                self.name = data
            
            case 'description':
                self.description = data
            
            case 'target_date':
                self.target_date = data
            
            case 'completed':
                self.completed = data
            
            case _:
                pass

    def export(self):
        return {
            'name': self.name,
            'description': self.description,
            'completed': self.completed,
            'start_date': datetime.datetime.strftime(self.start_date, DATETIME_FORMAT),
            'target_date': datetime.datetime.strftime(self.target_date, DATETIME_FORMAT) if self.target_date is not None else None
        }


class Program:
    def __init__(self, filename: str=None):
        self.level = 0
        self.experience = 0

        #
        self.filename = filename
        self.tasks = []

        if filename is not None:
            _, ext = filename.split('.')
            self.load(ext)

    def __str__(self) -> str:
        txt = ''
        for task in self.tasks:
            status = '*' if task.completed else ' '
            txt += f"[{status}] {task.name}: {task.description}\n"
        return txt

    def save(self, format: str='json'):
        if self.filename is None:
            return
        
        match format:
            case 'json':
                save_json(self.filename, [f.export() for f in self.tasks])
            
            case 'db':
                pass
            case _:
                pass
        return

    def load(self, format: str='json'):
        if self.filename is None or not os.path.exists(self.filename):
            return
        
        data = None
        
        match format:
            case 'json':
                data = load_json(self.filename)
            case 'db':
                pass
            case _:
                pass
        
        conv_dt = lambda x: datetime.datetime.strptime(x, DATETIME_FORMAT) if x is not None else None

        final = []
        for item in data:
            n = item.get('name')
            d = item.get('description')
            c = item.get('completed')
            sd = item.get('start_date')
            td = item.get('target_date')

            final.append(Task(n, d, bool(c), conv_dt(sd), conv_dt(td)))

        self.tasks = final
        return final
    
    def create(self):
        """ Create a new task
        name: str
        description: str
        target_date: datetime.datetime
        """
        name = input("Task name: ")
        description = input("Task description: ")
        t_date = input(f"Choose target date({DATETIME_FORMAT}): ")
        t_date = None if t_date == "" else datetime.datetime.strptime(t_date, DATETIME_FORMAT)

        # Sanitize Inputs
        new_task = Task(name, description=description, target_date=t_date)
        self.tasks.append(new_task)

    def is_valid_idx(self, idx: int):
        under_lower_bound = idx < 0
        above_upper_bound = idx >= len(self.tasks)
        
        if under_lower_bound or above_upper_bound:
            return False
        
        return True
    
    def read(self, idx: int):
        if not self.is_valid_idx(idx):
            return None

        return self.tasks[idx]
    
    def update(self):
        idx = int(input("Choose idx: "))
        
        if not self.is_valid_idx(idx):
            return
        # Validate data?
        task = self.tasks[idx]
        task.update('completed', not task.completed)
    
    def delete(self, idx):        
        if not self.is_valid_idx(idx):
            return None

        self.tasks.pop(idx)

    def run(self):
        while True:
            print(self)
            user_input = input(">>> ")

            match user_input:
                case 'c':
                    self.create()

                case 'u':
                    self.update()

                case 'r':
                    pass
                case 'd':
                    pass
                case 's':
                    self.save()
                case 'q':
                    break
                case _:
                    pass


if __name__ == "__main__":
    sample_task = {
        'name': "Task #1",
        'description': "This is the main content of task 1"
    }

    sample_raw_list = [
        {
            'name': "Task #1",
            'description': "This is the main content of task 1."
        },
        {
            'name': "Task #2",
            'description': "This is the main content of task 2."
        },
        {
            'name': "Task #3",
            'description': "This is the main content of task 3."
        }   
    ]


    # Add 2 loading options json and sqlite
    # FILENAME = 'database.db'
    FILENAME = 'database.json'
    prog = Program(FILENAME)
    # prog.create(**sample_task)

    prog.run()
  