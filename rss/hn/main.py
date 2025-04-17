import os
import json

import requests

from typing import List, Dict, Union

from dataclasses import dataclass



"""


URL = https://hacker-news.firebaseio.com/v0/



--------------------------------------------------------
ITEMS
    id
    deleted
    type { job | story | comment | poll | pollopt }
    by
    time
    text
    dead
    parent
    poll
    kids
    url
    score
    title
    parts
    descendants

USERS
    id
    created
    karma
    about
    submitted

LIVE DATA

    Current Largest Item ID(Newest Item): /v0/maxitem

    NEW, TOP, and BEST STORIES  [500]
        /v0/topstories (jobs inc.)
        /v0/newstories
        /v0/beststories
    
    ASK, SHOW, and JOB STORIES  [200]
        /v0/askstories
        /v0/showstories
        /v0/jobstories

        



Create VIEWS

- Stories
- Comments
- Jobs
        
"""

def get_call(url: str):
    # Make Request to API Endpoint
    response = requests.get(url)

    if response.status_code == 200:
        # print("200: Success")
        return response.json()

    return None



class APIWrap:
    def __init__(self):
        self.base_url = "https://hacker-news.firebaseio.com/v0"

    def __str__(self):
        s = f'{self.base_url}'
        return s
    
    def get_item(self, item_id):
        endpoint_url = f"{self.base_url}/item/{item_id}.json"
        return get_call(endpoint_url)

    def get_newest_item_id(self):
        endpoint_url = f"{self.base_url}/maxitem.json"
        return get_call(endpoint_url)
    
    def get_new_stories(self):
        endpoint_url = f"{self.base_url}/newstories.json"
        return get_call(endpoint_url)
    
    def get_top_stories(self):
        endpoint_url = f"{self.base_url}/newstories.json"
        return get_call(endpoint_url)
    
    def get_best_stories(self):
        endpoint_url = f"{self.base_url}/newstories.json"
        return get_call(endpoint_url)
    
    def get_job_stories(self):
        endpoint_url = f"{self.base_url}/jobstories.json"
        return get_call(endpoint_url)


@dataclass
class Item:
    # Meta
    item_id: int=None
    item_type: str=None
    by: str=None
    time: int=None
    
    # Data
    url: str=None
    title: str=None
    text: str=None
    
    # Metrics
    score: int=None
    dead: bool=False
    
    # Relation
    parent: int=None
    kids: List[int]=None
    descendants: int=None    

    def __str__(self):
        # Basic View
        if self.title is None:
            return f'[{self.id}]'
        
        # Story View
        s = f"""{self.item_id} | {self.item_type}
[{self.score}] {self.title}
{self.url}
"""
        return s
    
    def update(self, raw_data):
        # Update internal data if present
        self.item_type = raw_data.get('type')
        self.by = raw_data.get('by', None)
        self.time = raw_data.get('time', None)
        self.url = raw_data.get('url', None)
        self.title = raw_data.get('title', None)
        self.text = raw_data.get('text', None)
        self.score = raw_data.get('score', None)
        self.dead = raw_data.get('dead', None)
        self.parent = raw_data.get('parent', None)
        self.kids = raw_data.get('kids', None)
        self.descendants = raw_data.get('descendants', None) 


def main():
    # Make Request to API Endpoint
    api = APIWrap()

    best_stories_data = api.get_best_stories()

    for item_id in best_stories_data[:5]:
        # Get Item data
        new_item_data = api.get_item(item_id)
        
        # Create New Item
        new_item = Item(item_id=item_id)
        new_item.update(new_item_data)

        print(new_item)


if __name__ == "__main__":
    main()
