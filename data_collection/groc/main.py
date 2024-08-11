import os
import json

from typing import Dict


def flatten_dict(s):
    if type(s) is dict:
        for k, v in s.items():
            ...
    
    if type(s) is list:
        for i in s:
            flatten_dict(i)
    
    return s


class DataWrapper:
    def __init__(self, properties: Dict):
        self.properties = properties
        self.filename = "default_save.json"
    
    def __str__(self):
        s = f'{flatten_dict(self.properties)}'
        return s
    
    def save(self, filename: str=None):
        if filename is not None:
            self.filename = filename
        
        with open(self.filename, 'w') as save_buf:
            json.dump(self.properties, save_buf, indent=4)
        
    def load(self, filename: str=None):
        if filename is not None:
            self.filename = filename
        data = None
        with open(filename, 'r') as load_buf:
            data = json.load(load_buf)

        # Overwrite?
        # self.properties = data

        return data


if __name__ == "__main__":
    ...