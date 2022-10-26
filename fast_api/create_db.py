import os
import json
from typing import Dict, List, Any

from dataclasses import dataclass


@dataclass
class Entry:
    id: int
    name: str
    post_id: int = None
    path: str = None

    def __call__(self, default: bool=False) -> Any:
        if default:       
            return {
                "id": int,
                "name": str,
                "post_id": int,
                "path": str
            }
        
        return {
            "id": self.id,
            "name": self.name,
            "post_id": self.post_id,
            "path": self.path
        }
    


raw_data = {
    "id": 1,
    "name": "Fake Name", 
    "post_id": 3
}

new_entry = Entry(**raw_data)


print(new_entry())
print(new_entry(True))



def create_fake_data(entry_type: Any, amount: int=5):
    final_data = []

    for _ in range(amount):
        new_data = {}
        for f_name, f_type in fields_types.items():
            new_value = None

            match f_type:
                case int:
                    print("int")
                

                case _:
                    pass



            new_data[f"{f_name}"] = f_type()
        final_data.append(new_data)
    
    print(final_data)


# if __name__ == '__main__':
    
#     # sample_data = [
#     #     {
#     #         "id": 1,
#     #         "name": "Fake Name",
#     #         "post_id": 5,
#     #         "path": "fake/path/1"
#     #     },
#     #     {
#     #         "id": 2,
#     #         "name": "Fake Name",
#     #         "post_id": 3,
#     #         "path": "fake/path/2"
#     #     },
#     #     {
#     #         "id": 3,
#     #         "name": "Fake Name",
#     #         "post_id": 2,
#     #         "path": "fake/path/3"
#     #     }
#     # ]

#     fields = ["id", "name", "post_id", "path"]

#     sample_data = create_fake_data(fields) 

#     with open("data/test/test_data.json", 'w') as save_data:
#         json.dump(sample_data, save_data, indent=4)

