from dataclasses import dataclass, Field

from utils.exp_system import ExperienceSystem
from utils.items import Item
from utils.skills import Skill

from typing import List, Dict


@dataclass
class Character:
    name: str
    inventory: List[Item]=Field(default_factory=list)
    skills: List[Skill]=Field(default_factory=list)
    exp: ExperienceSystem=Field(default_factory=ExperienceSystem)

    def __str__(self):
        return f""

    def load_data(self, filename: str):
        return
    
    def use_item(self):
        return
    
    def use_skill(self):
        return
    
    def attack(self):
        return
    
    def defend(self):
        return
    
    def evade(self):
        return
    
    def export(self):
        return {
            'name': self.name,
            'inventory': [i.export() for i in self.inventory],
            'skills': [s.export() for s in self.skills],
            'exp': self.exp.export()
        }

