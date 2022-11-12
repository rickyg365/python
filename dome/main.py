import os

import json

from typing import List, Dict
from dataclasses import dataclass

from datetime import datetime, date, timedelta


def time_elapsed(start_time: datetime, end_time: datetime) -> timedelta:
    total_s = (end_time - start_time).total_seconds()
    final_data = {
        "seconds": 0,
        "minutes": 0,
        "hours": 0,
        "days": 0
    }

    conversions = {
        "seconds_minutes": 60, 
        "minutes_hours": 60, 
        "hours_days": 24
    }  
    
    leftover = total_s
    next_unit = "seconds"
    for key, conversion_factor in conversions.items():
        # hours, total_min = divmod(total_s, 60)
        previous_unit = next_unit
        curr_unit, next_unit = key.split("_") 

        if previous_unit != curr_unit:
            print("oops")
            continue

        new_unit, leftover = divmod(leftover, conversion_factor)
        final_data[curr_unit] = new_unit
        
    return f"{final_data['days']}d {final_data['hours']:02.0f}:{final_data['minutes']:02.0f}:{final_data['seconds']:02.0f}"



@dataclass
class Task:
    id: int=-1
    details: str=None
    status: bool=False
    created: datetime=datetime.now()

    def __str__(self) -> str:
        f_status = f"✔️" if self.status else f"🔳"
        f_details = f"{self.details:<20}"
        f_time_elapsed = time_elapsed(self.created, datetime.now())
        return f"{self.id}. {f_status} {f_details} {f_time_elapsed}"

    def export(self):
        return {
            "id": self.id,
            "details": self.details,
            "status": self.status,
            "created": self.created.isoformat()
        }

    def unexport(self, data):
        for k, v in data.items():
            match k:
                case "id":
                    self.id = int(v)
                case "details":
                    self.details = v
                case "status":
                    self.status = bool(v)
                case "created":
                    self.created = datetime.fromisoformat(v)
                case _:
                    pass


def main():
    # Create
    # task = Task(1, "My First Task")
    
    # Load
    with open("tasks.json", 'r') as load_file:
        data = json.load(load_file)

    task = Task()
    task.unexport(data)
        
    print(task)

    # Save
    with open("tasks.json", 'w') as save_file:
        json.dump(task.export(), save_file, indent=4)


if __name__ == "__main__":
    main()
