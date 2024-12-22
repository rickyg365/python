
import os
from typing import List, Dict, Callable

from item import Item, Equipment, Consumable, Inventory
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
        self.inventory = Inventory()
        
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

{self.inventory}
"""
    
    def export(self):
        return

    def apply_buff(self, attribute: str, buff_amount: int):
        attribute_exists = hasattr(self, attribute)
        if not attribute_exists:
            return

        current = getattr(self, attribute)
        setattr(self, attribute, current + buff_amount)
        
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

        
        

if __name__ == "__main__":
    HERO_DATA = {
        'name': 'Hero',
        'health': 20,
        'attack': 20,
        'defense': 20,
        'speed': 20,
    }

    hero = Character(**HERO_DATA)
    print(hero)


    POTION_DATA = {
        'key': 'ttrrppid',
        'name': 'Potion',
        'item_type': 'consumable',
        'description': 'Heals a small amount of health.',
        'attributes': {
            'health': 10
        },
    }

    WOODEN_SWORD = {
        'key': 'ttrrppid',
        'name': 'Wooden Sword',
        'item_type': 'weapon',
        'description': 'A small wooden sword',
        'attributes': {
            'attack': 10,
            'critical_chance': 2
        },   
    }

    WOODEN_SHIELD = {
        'key': 'ttrrppid',
        'name': 'Wooden Shield',
        'item_type': 'equipment',
        'description': 'A small wooden shield',  # be careful not to get a splinter.
        'attributes': {
            'defense': 8,
            'block_chance': 10
        },
    }

    potion = Consumable(**POTION_DATA)
    wood_sword = Equipment(**WOODEN_SWORD)
    wood_shield = Equipment(**WOODEN_SHIELD)
    

    hero.equip('left_arm', wood_shield)
    hero.equip('right_arm', wood_sword)

    hero.consume(potion)

    print()
    print(hero)

