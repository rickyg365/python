import os
import requests

from dotenv import load_dotenv

'''
# Load env
load_dotenv('sum.env')

# Create Connection
token = os.getenv('ACCESS_TOKEN')

data = {
    "type": "note",
    "title": "Sample Title",
    "body": "This is the main content of the message"
}

HEADERS = {
    'Access-Token': token,
    'Content-Type': 'application/json',
}
r = requests.post('https://api.pushbullet.com/v2/pushes', headers=HEADERS, json=data)
'''

class PushBulletNotifier:
    def __init__(self, filename: str):
        load_dotenv(filename)
        self.filename = filename

        self.headers = {
            'Access-Token': os.getenv('ACCESS_TOKEN'),
            'Content-Type': 'application/json'
        }

        self.push_url = 'https://api.pushbullet.com/v2/pushes'
        self.last_response = None
    
    def __str__(self) -> str:
        return f"{self.last_response}"
    
    def push_note(self, title: str, body: str):
        data = {
            "type": "note",
            "title": title,
            "body": body
        }

        self.last_response = requests.post(self.push_url, json=data, headers=self.headers)

    def show_last_response(self):
        if self.last_response is None:
            # Create response ?
            return
        
        print(self.last_response)
        print(self.last_response.json())



if __name__ == "__main__":
    notifier = PushBulletNotifier('sum.env')
    notifier.push_note('Note 1', "Sample of note body 1")
    notifier.push_note('Note 2', "Sample of note body 2")

