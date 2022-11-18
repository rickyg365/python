import os
from typing import List, Dict
from dataclasses import dataclass
""" 
Model: Zoo Keeper

"""

@dataclass
class Keeper:
    name: str

    salary: float = 100_000
    availability: int = 0 # hrs per week

    def __str__(self):
        txt = f"Keeper: {self.name} ~ {self.salary:,}"
        return txt

    def adjust_salary(self, new_salary: float):
        self.salary = new_salary
        return self

    def set_availability(self, new_availability: int):
        self.availability = new_availability
        return self
    
    def export(self):
        return {
            "name": self.name,
            "salary": self.salary,
            "availability": self.availability
        }


def main():
    return

if __name__ == '__main__':
    main()
