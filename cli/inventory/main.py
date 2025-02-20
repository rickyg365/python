import os
from item import Item
from collection import Collection
from utils import save_json, load_json



class App:
    def __init__(self, title: str, collections: Collection=None, items: Collection=None):
        self.title = title
        self.collections = collections  # collection_name: Collection[]
        self.items = items  # item_id: Item

    def __str__(self):
        s = f'{self.title}'
        return s
    
    def initial_load(self):
        return
    
    def create_item(self):
        return
    
    def create_collection(self):
        return
    
    def read_item(self):
        return
    
    def read_collection(self):
        return
    
    def update_item(self):
        return
    
    def update_collection(self):
        return
    
    def delete_item(self):
        return
    
    def delete_collection(self):
        return
    
    def run(self):
        return




if __name__ == "__main__":
    ...
