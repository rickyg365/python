import os
import json

from typing import List, Dict
from dataclasses import dataclass, Field


"""

"""

@dataclass
class Data:
    ref: str
    ref_type: str='file'
    data=None

    def __post_init__(self):
        data = None
        match self.ref_type:
            case 'file':
                # Extract file data
                data = None
            case 'url':
                # Extract url data
                data = None
            case _:
                pass
        
        self.data = data
    
    def __str__(self) -> str:
        return f"""[{self.ref_type}] {self.ref}"""
    
    def export(self):
        return {
            'ref': self.ref,
            'ref_type': self.ref_type
        }


@dataclass
class Item:
    name: str=None
    data: Data=None
    tag: str=None

    def __str__(self) -> str:
        return f"""{self.name} | {self.tag}
{self.data}
"""
    
    def model_map(self):
        return f"""
name: str
data: Data(file|url)
tag: str
"""
    
    def generate(self):
        n = input("Name: ")
        d = input("Data(file or url): ")
        t = input("Tag: ")

        self.name = n
        self.data = Data(d) if d != '' else None
        self.tag = t if t != '' else None

        return self
    
    def update(self):
        u_in = input("Fix which value? [ name | data | tag ]: ")

        match u_in:
            case 'n' | 'name':
                new_name = input('Name: ')
                self.name = new_name
            case 'd' | 'data':
                new_data = input('Data(file or url): ')
                self.data = new_data
            case 't' | 'tag':
                new_tag = input('Tags: ')
                self.tag = new_tag
            case _:
                pass

    def export(self):
        return {
            'name': self.name,
            'data': self.data.export(),
            'tag': self.tag
        }


class App:
    def __init__(self, prog_text: str="Program Info"):
        self.prog_text = prog_text
        self.data = []
        self.filename = "default_save.json"

    def __str__(self) -> str:
        items = '\n'.join(f"{d}" for d in self.data)
        txt = f"""{self.prog_text}
{items}
"""
        return txt
    
    def check_idx(self, idx: int):
        mx = len(self.data)

        # Early exit
        if mx == 0 and idx != 0:
            return False

        # Min Bound  
        if idx <= 0:
            return False

        # Max Bound
        if idx >= mx:
            return False
        
        return True

        
    def create(self) -> Item:
        new_item = Item()
        new_item.generate()

        print(new_item)

        # Add Item to Data
        u_in = input("Keep item?: ")
        if u_in == 'y':
            self.data.append(new_item)

        return new_item
    
    def read(self, idx: int=0) -> Item:
        # Check if idx valid
        if not self.check_idx(idx):
            return None

        return self.data[idx]
    
    def update(self, idx: int) -> None:
        # Check if idx valid
        if not self.check_idx(idx):
            return None

        updated_item = self.data[idx].update()
        print(updated_item)


    def delete(self, idx: int):
        # Check if idx valid
        if not self.check_idx(idx):
            return None
        
        removed_item = self.data.pop(idx)
        print(removed_item)

    def run(self):
        while True:
            print(self)
            u_input = input(f"""CRUD
c reate
r ead
u pdate
d elete
>>> """)
            match u_input:
                case _:
                    pass




if __name__ == "__main__":
    new_crud = App("New Sample App")
    new_crud.run()

















