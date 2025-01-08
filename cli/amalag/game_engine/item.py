import os

from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:  # Only imports the below statements during type checking
    from game_engine.character import Character


from enum import Enum
from typing import Union

"""


"""

class ItemType(Enum):
    key = "key"
    consumable = "consumable"
    equipment = "equipment"


class Item:
    ABBRV = {
        'item': '???',
        'weapon': 'WPN',
        'equipment': 'EQP',
        'consumable': 'CON',
    }
    def __init__(self, name: str, item_type: Union[ItemType, str]=ItemType.consumable, hp: int=0, mp: int=0, attack: int=0, defense: int=0, speed: int=0, special: int=0, luck: int=0):
        self.name = name
        self.item_type = item_type if isinstance(item_type, ItemType) else ItemType(item_type)
        self._hp = hp
        self._mp = mp
        self._attack = attack
        self._defense = defense
        self._speed = speed
        self._special = special
        self._luck = luck


    def __str__(self):
        s = f'[{self.item_type.value}] {self.name}'
        return s
    
    def show_details(self):
        hp = f"+{self._hp} hp"
        mp = f"+{self._mp} mp"
        atk = f"+{self._attack} atk"
        defense = f"+{self._defense} def"
        speed = f"+{self._speed} spd"
        special = f"+{self._special} spl"
        luck = f"+{self._luck} lck"

        print(f"""[{self.item_type}] {self.name}
{hp}
{mp}
{atk}
{defense}
{speed}
{special}
{luck}
""")
    
    def export(self):
        return {
            "name": self.name,
            "item_type": self.item_type.value,
            "hp": self._hp,
            "mp": self._mp,
            "attack": self._attack,
            "defense": self._defense,
            "speed": self._speed,
            "special": self._special,
            "luck": self._luck,
        }
    


class Consumable(Item):
    def __init__(self, key: str, name: str, description: str, attributes: Dict, **kwargs):
        super().__init__(item_type='consumable', key=key, name=name, description=description)
        self.attributes = attributes

    def __str__(self):
        s = f'{self.name}'
        return s

    def use(self, target: Character):
        for key, value in self.attributes.items():
            target.apply_buff(key, value)
    
    def export(self):
        return {
            **super().export(),
            'attributes': self.attributes
        }


class Equipment(Item):
    def __init__(self, name: str="Item", item_type: Union[ItemType, str]=ItemType.equipment, hp: int=0, mp: int=0, attack: int=0, defense: int=0, speed: int=0, special: int=0, luck: int=0, equipment=None):
        super().__init__(name=name, item_type=item_type, hp=hp, mp=mp, attack=attack, defense=defense, speed=speed, special=special, luck=luck)
        self.equipment = list() if equipment is None else equipment

    def __str__(self):
        s = f'{self.name}'
        return s
    
    
    def show_details(self):
        hp = f"+{self._hp} hp"
        mp = f"+{self._mp} mp"
        atk = f"+{self._attack} atk"
        defense = f"+{self._defense} def"
        speed = f"+{self._speed} spd"
        special = f"+{self._special} spl"
        luck = f"+{self._luck} lck"

        print(f"""[{self.item_type.value}] {self.name} - {self.equipment}
{hp}
{mp}
{atk}
{defense}
{speed}
{special}
{luck}
""")
    
    def export(self):
        return {
            "name": self.name,
            "item_type": self.item_type.value,
            "hp": self._hp,
            "mp": self._mp,
            "attack": self._attack,
            "defense": self._defense,
            "speed": self._speed,
            "special": self._special,
            "luck": self._luck,
            'equipment': self.equipment
        }
    
    def apply(self, target):
        return
    
    def remove(self, target):
        return
    


def item_creator(raw_data: Dict):
    i_type = raw_data.get('item_type', 'item')  # default: item
    obj_class = lambda **x: None

    match i_type:
        case 'item':
            obj_class = Item
        case 'equipment':
            obj_class = Equipment
        case 'consumable':
            obj_class = Consumable
        case _:
            pass

    return obj_class(**raw_data)



class EquipmentLoadout:
    def __init__(self, head: Equipment=None, body: Equipment=None, legs: Equipment=None, right_arm: Equipment=None, left_arm: Equipment=None):
        self.head = head, 
        self.body = body, 
        self.legs = legs, 
        self.right_arm = right_arm, 
        self.left_arm = left_arm
    
    def __str__(self):
        print(self.head)
        print(self.right_arm)
        print(self.left_arm)
        s = f'''Equipment Loadout
Head: {self.head}
Right Arm: {self.right_arm}
Left Arm: {self.left_arm}
Body: {self.body}
Legs: {self.legs}
'''
        return s
    
    def load_from_raw(self, head=None, body=None, legs=None, right_arm=None, left_arm=None):
        # Removed form init, 
        # self.head = head if isinstance(head, Equipment) else Equipment(**head), 
        # self.body = body if isinstance(body, Equipment) else Equipment(**body), 
        # self.legs = legs if isinstance(legs, Equipment) else Equipment(**legs), 
        # self.right_arm = right_arm if isinstance(right_arm, Equipment) else Equipment(**right_arm), 
        # self.left_arm = left_arm if isinstance(left_arm, Equipment) else Equipment(**left_arm)
        
        self.head = Equipment(**head)
        self.body = Equipment(**body)
        self.legs = Equipment(**legs)
        self.right_arm = Equipment(**right_arm)
        self.left_arm = Equipment(**left_arm)
    
    
        return self
    
    def export(self):
        return {
            "head": self.head.export(),
            "right_arm": self.right_arm.export(),
            "left_arm": self.left_arm.export(),
            "body": self.body.export(),
            "legs": self.legs.export(),
        }


if __name__ == "__main__":
    ITEM_DATA = {}
    EQUIPMENT_DATA = {}

    i = Item(**ITEM_DATA)
    e = Equipment(**EQUIPMENT_DATA)

    print(i)

    print(e)


    e.show_details()

