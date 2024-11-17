import os
import datetime

from dataclasses import dataclass, field



DATETIME_FORMAT = "%Y-%m-%d %I:%M:%S"

@dataclass
class Task:
    name: str
    description: str=""
    completed: bool=False
    start_date: datetime.datetime=field(default_factory=datetime.datetime.now)
    target_date: datetime.datetime=None
    last_updated: datetime.datetime=None

    def __post_init__(self):
        self.parse()

    def __str__(self) -> str:
        status = '*' if self.completed else ' '
        return f"({status}) {self.name}: {self.description}"

    def details(self):
        status = '*' if self.completed else ' '
        return f"""({status}) {self.name}: {self.description}
start date: {self.start_date}
target date: {self.target_date}
last updated: {self.last_updated}
"""

    def parse(self):
        conv_dt = lambda x: datetime.datetime.strptime(x, DATETIME_FORMAT) if x is not None else None

        if isinstance(self.completed, str):
            self.completed = bool(self.completed)

        if isinstance(self.start_date, str):
            self.start_date = conv_dt(self.start_date)

        if isinstance(self.target_date, str):
            self.target_date = conv_dt(self.target_date)

        return
    
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



class TaskTracker:
    def __init__(self, filename: str):
        self.filename = filename
        self.tasks = []
            
    def __str__(self) -> str:
        txt = ''
        for _, task in enumerate(self.tasks, start=1):
            txt += f"{_}. {task}\n"
        
        # '\n'.join([f'{t}' for t in self.tasks])
        return txt
    
    def is_valid_idx(self, idx: int):
        # Conditions
        under_lower_bound = idx < 0
        above_upper_bound = idx >= len(self.tasks)
        
        # Fail
        if under_lower_bound or above_upper_bound:
            return False
        
        # Pass
        return True

    def create(self, name: str, description: str, target_date: str) -> Task:
        """ Create a new task
        name: str
        description: str
        target_date: datetime.datetime
        """
        new = Task(name=name, description=description, target_date=target_date)
        self.tasks.append(new)
        return new
    
    def read(self, index: int) -> Task:
        if not self.is_valid_idx(index):
            return None
        
        return self.tasks[index]

    def update(self, index: int) -> Task:
        if not self.is_valid_idx(index):
            return None
        
        task = self.tasks[index]

        # Toggle completed
        task.update('completed', not task.completed)

        return task

    def delete(self, index: int):
        if not self.is_valid_idx(index):
            return None
        
        removed_task = self.tasks.pop(index)
    
        return removed_task
    
    # def save(self):
    #     if self.filename is None:
    #         return
        
    #     save_json(self.filename, [f.export() for f in self.tasks])    
    #     return

    # def load(self):
    #     if self.filename is None or not os.path.exists(self.filename):
    #         return None
        
    #     data = load_json(self.filename)
        
    #     self.tasks = [Task(**item) for item in data]
    #     return self.tasks
    def export(self):
        """ Task Tracker Export

        Returns::

            List -> [Task.export() for Task in self.tasks]
        """
        return [f.export() for f in self.tasks]
