from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:  # Only imports the below statements during type checking
    from item import Item, Equipment, Consumable

import os
from typing import List, Dict, Callable

'''
Goals:
- save/load data
- basic crud operations

Items
- Key
- Consumable
- Equipment

'''
class Character:
    def __init__(self, name: str, health: int=0, attack: int=0, defense: int=0, speed: int=0, critical_chance: int=0, block_chance: int=0, equipment: Dict=None):
        self.name = name
        self.health = 20
        self.attack = 10
        self.defense = 8
        self.speed = 10
        self.critical_chance = 0
        self.block_chance = 0
        self.equipment = {
            'head': None,
            'body': None,
            'right_arm': None,
            'left_arm': None,
            'legs': None,
            'accessory_1': None,
            'accessory_2': None
        }
        
    def __str__(self):
        return f"""
{self.name}
HP: {self.health}
Attack: {self.attack}
Defense: {self.defense}
Speed: {self.speed}
Critical Chance: {self.critical_chance}%
Block Chance: {self.block_chance}%

Equipment:
    Head: {self.equipment['head']}
    Body: {self.equipment['body']}
    Left Arm: {self.equipment['left_arm']}
    Right Arm: {self.equipment['right_arm']}
    Legs: {self.equipment['legs']}
    Accessory 1: {self.equipment['accessory_1']}
    Accessory 2: {self.equipment['accessory_2']}

"""

    def apply_buff(self, attribute: str, buff_amount: int):
        attribute_exists = hasattr(self, attribute)
        if not attribute_exists:
            return

        current = getattr(self, attribute)
        setattr(self, attribute, current + buff_amount)

        # match attribute:
        #     case 'health':
        #         self.health += buff_amount
        #     case 'defense':
        #         self.defense += buff_amount
        #     case 'attack':
        #         self.attack += buff_amount
        #     case 'speed':
        #         self.speed += buff_amount
        #     case 'critical_chance':
        #         self.critical_chance += buff_amount
        #     case 'block_chance':
        #         self.block_chance += buff_amount
        #     case _:
        #         pass
        
        return

    def consume(self, item: Consumable):
        item.use(self)

        # Remove item from inventory


    def equip(self, part: str, equipment: Equipment):
        # Check if valid part
        if part not in self.equipment.keys():
            return
        
        # Check if something is equipped
        current = self.equipment.get(part, None)

        if current is not None:
            current.remove(self)
        
        # Equip new
        self.equipment[part] = equipment
        equipment.apply(self)
        
        
