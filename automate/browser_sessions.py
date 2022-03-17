import os
import time
import json

from typing import List
from utils.automate_browser import open_app_by_name, open_urls


"""
Notes:

"""

class Session:
    def __init__(self, file_path: str="data/session_data.json"):
        self.file_path = file_path
        self.urls = None
        self.apps = None

        self.delay = 2
        self.enabled = False

        # Load inital data to enable start
        self.load_session_data()

    def check_data(self):
        no_urls = type(self.urls) is not list
        no_apps = type(self.apps) is not list

        if no_urls and no_apps:
            return False

        return True

    def save_session_data(self):
        """ Save json data with list of urls and apps to open """
        if not self.check_data():
            return

        save_data = {
            'urls': self.urls,
            'apps': self.apps
        }

        with open(self.file_path, 'w') as out_data:
            json.dump(save_data, out_data, indent=4)

    def load_session_data(self):
        """ Load json data with list of urls and apps to open """
        try:
            with open(self.file_path, 'r') as in_data:
                new_data = json.load(in_data)
            
            self.urls = new_data.get('urls', None)
            self.apps = new_data.get('apps', None)

            if self.check_data():
                self.enabled = True

        except FileNotFoundError:
            self.enabled = False
        
    def start(self):
        """ Opens urls in a seperate window and launches Discord """
        if not self.enabled:
            print("[ No Data ]")
            return

        # Open Browser and URLs
        open_urls(self.urls)
        
        # Open Apps
        for app in self.apps:
            time.sleep(self.delay)
            open_app_by_name(app)


if __name__ == '__main__':
    default_filepath = "data/session_data.json"
    work_filepath = 'data/work_data.json'
    broken_filepath = "data/fake_data.json"

    new_session = Session()
    new_session.save_session_data()
    new_session.start()
