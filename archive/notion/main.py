import os

import json
import requests

from dotenv import load_dotenv

# Load in ENV
load_dotenv()

# Load in ENV File
# load_dotenv()

class NotionClient:
    def __init__(self):
        self.base_url = 'https://api.notion.com/v1'

        
        self.database_ids = None
        self.int_key = None

        self.headers = {
            'Content-Type': 'application/json',
            'Notion-Version': '2022-02-22'
        }

        # Load in 
        self.load()

    def __str__(self) -> str:
        txt = ""
        return txt

    def load(self):
        # Test to make sure it loaded
        env_load_test = os.environ.get('TEST_ENV_CHECK', 0)
        if env_load_test == 0:
            return
        
        # Load in Data
        self.int_key = os.environ.get('INTEGRATION_KEY', 'Not Found')

        with open('secret.json', 'r') as in_json:
            self.database_ids = json.load(in_json)

        # Setup Header
        self.headers['Authorization'] = f"Bearer {self.int_key}"
    
    def search(self):
        url = f"{self.base_url}/search"
        query_data = {
            "query": "",
            "sort": {
                "direction": "ascending",
                "timestamp": "last_edited_time"
            }
        }
        response = requests.post(url, headers=self.headers, json=query_data)
        print(response.json())

    def add_to_database(self, database_key: str, content_data=None):
        url = f"{self.base_url}/pages"
        new_data = {
            "parent": { "database_id": self.database_ids[database_key] },
            "properties": {
                "title": {
                    "title": [
                        {
                            "text": {
                                "content": "Yurts in Big Sur, California"
                            },
                        },
                    ]
                }
            }
        }

        # Check Request
        response = requests.post(url, headers=self.headers, json=new_data)
        print(response.json())
            

    def retrieve_database(self, database_key: str):
        url = f'{self.base_url}/pages/{self.database_ids[database_key]}'
        response = requests.get(url, self.headers)
        print(response.json())


def main():
    # env_load_test = os.environ.get('TEST_ENV_CHECK', 0)

    # if env_load_test == 0:
    #     return
    
    # # Load in Data
    # int_key = os.environ.get('INTEGRATION_KEY', 'Not Found')

    # with open('secret.json', 'r') as in_json:
    #     database_ids = json.load(in_json)

    # url = 'https://api.notion.com/v1/pages'

    # headers = {
    #     'Authorization': f"Bearer {int_key}",
    #     'Content-Type': 'application/json',
    #     'Notion-Version': '2022-02-22'
    # }

    # Data to Add
    # new_data = {
    #     "parent": { "database_id": f"{database_ids['new_projects']}" },
    #     "properties": {
    #         "title": {
    #             "title": [
    #                 {
    #                     "text": {
    #                         "content": "Yurts in Big Sur, California"
    #                     },
    #                 },
    #             ]
    #         }
    #     }
    # }

    # # Check Request
    # response = requests.post(url, headers=headers, json=new_data)
    # print(response.json())
    # new_data = {
    #     "parent": { "database_id": f"{self.database_ids['new_projects']}" },
    #     "properties": {
    #         "title": {
    #             "title": [
    #                 {
    #                     "text": {
    #                         "content": "Yurts in Big Sur, California"
    #                     },
    #                 },
    #             ]
    #         }
    #     }
    # }
    notion = NotionClient()
    notion.retrieve_database('new_projects')
    notion.search()
    # notion.add_to_database('new_projects')


if __name__ == '__main__':
    main()

