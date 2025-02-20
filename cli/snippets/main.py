import os

from typing import List, Dict, Union
 



"""

"""
# Raw Data
ITEM = {
    'name': 'Item 1',
    'item_id': 'reg01'
}

COLLECTION = [
    {
        'name': 'Item 1',
        'item_id': 'reg01'
    },
    {
        'name': 'Item 2',
        'item_id': 'reg02'
    },
    {
        'name': 'Item 3',
        'item_id': 'reg03'
    }  
]

# Models
class Item:
    def __init__(self, name, item_id):
        self.id = item_id
        self.name = name

    def __str__(self):
        s = f'{self.name}'
        return s

class Collection:
    def __init__(self, data=None):
        self.data = data


    def __str__(self):
        return f""


# Data
def generate_data(config):
    data = {

    }
    
    return data

# Analysis
def analyze_data(data):
    for k, v in data.items():
        print(k, v)
    return

# Visualizations
def visualize_data(data):
    return
  

if __name__ == "__main__":
    # Data
    CONFIG = {

    }
    DATA = generate_data(config=CONFIG)

    # Analysis
    analyzed_data = analyze_data(data=DATA)

    # Visualizations
    visualize_data(analyzed_data)

