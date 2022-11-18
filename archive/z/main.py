import os
import random

from typing import List, Dict


class Model:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __str__(self) -> str:
        txt = f"[{self.id:02}] {self.name}"
        return txt


class ModelList:
    def __init__(self, starting_data: List[any]=None):
        if starting_data is None:
            starting_data = []

        self.length = len(starting_data)
        self.data = starting_data

    def __str__(self) -> str:
        txt = "\n".join([f"{d}" for d in self.data])
        return f"Length: {self.length}\n{txt}"
    
    def create_item(self, id: int, name: str):
        new_item = Model(id, name)

        self.data.append(new_item)
        self.length += 1
        
        return new_item  # For Chaining

    def add(self, new_item: Model):
        self.data.append(new_item)
        self.length += 1

    def remove(self, chosen_id: int):
        self.data = [x for x in self.data if x.id != chosen_id]
        self.length -= 1  # might not remove edit

    def get(self, chosen_id: int):
        for item in self.data:
            if item.id == chosen_id:
                return item
        return None


def generate_raw_data():
    name_list = [
        "bob",
        "rob",
        "john",
        "hob",
        "bill",
        "will",
        "tim",
        "jim",
    ]

    i = random.randint(0, 99)
    n = random.randint(0, len(name_list)-1)

    return {
        "id": i,
        "name": name_list[n].title()
    }


def main():
    raw_data_list = [generate_raw_data() for _ in range(10)]

    raw_model_list = [Model(**rd) for rd in raw_data_list]

    model_list = ModelList(raw_model_list)

    # Edit Model List
    print(model_list)
    model_list.data[0].id = 111
    chosen = model_list.get(111)
    chosen.name = "Chosen Name"

    output = f""" 
{raw_data_list}

{raw_model_list}

{model_list}    
"""

    print(output)


if __name__ == '__main__':
    main()
