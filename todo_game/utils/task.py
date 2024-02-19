from enum import Enum


class TaskStatus(Enum):
    COMPLETED = '*'
    INCOMPLETE = ' '
    CANCELED = 'X'
    POSTPONED = '@'


class Task:
    def __init__(self, name: str, tag: str="ALL", gold: int=15, experience: int=20, progress_bar: bool=False, progress: int=0, total_progress: int=20, status: str="INCOMPLETE"):
        self.name = name
        self.tag = tag
        self.gold = gold
        self.experience = experience
        self.progress_bar = progress_bar
        self.progress = progress
        self.total_progress = total_progress
        self.status = TaskStatus[status]  # Enum: COMPLETED | INCOMPLETE | CANCELED | POSTPONED

    def __str__(self) -> str:
        p = ""
        if self.progress_bar:
            diff = self.total_progress - self.progress
            p = f"\n    {self.progress}/{self.total_progress} [{self.progress * '*'}{diff * ' '}]"
        return f"[{self.status.value}] ({self.tag}) {self.name}{p}\n    REWARD: {self.experience} EXP + {self.gold}G\n"
    
    def export(self):
        # Data
        data = {
            "name": self.name,
            "tag": self.tag,
            "gold": self.gold,
            "experience": self.experience,
            "progress_bar": self.progress_bar,
            "progress": self.progress,
            "total_progress": self.total_progress,
            "status": self.status.name
        }
        return data
    
    # def rehydrate(self, new_data):
    #     self.name = new_data.get("name", None)
    #     self.tag = new_data.get("tag", None)
    #     self.gold = new_data.get("gold", None)
    #     self.experience = new_data.get("experience", None)
    #     self.progress_bar = new_data.get("progress_bar", None)
    #     self.progress = new_data.get("progress", None)
    #     self.total_progress = new_data.get("total_progress", None)
    #     self.status = TaskStatus[new_data.get("status", "INCOMPLETE")]  # Enum: COMPLETED | INCOMPLETE | CANCELED | POSTPONED


