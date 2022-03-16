import os
import random

import json

from typing import List, Dict

from utils.progress_bar import progress_bar


class API:
    def __init__(self, data_path: str = "data/sample_data.json"):
        self.file_path = data_path
        self.data = list()
        self.length = 0

        # I finally get to use the walrus operator x_x, jk just rewrote it and added it to init
        if os.path.isfile(self.file_path):
            self.load_data(self.file_path)

    def __str__(self) -> str:
        output_txt = f"Using {self.file_path}"
        return output_txt

    def load_data(self, new_data_path: str = None):
        if new_data_path is None:
            new_data_path = self.file_path
        else:
            self.file_path = new_data_path

        with open(new_data_path, "r") as input_data:
            self.data = json.load(input_data)
        self.length = len(self.data)

        # print(f"{new_data_path} Loaded")

    def save_data(self):
        """rewrites save file with new data"""
        with open(self.file_path, "w") as output_data:
            json.dump(self.data, output_data, indent=4)

        # print(f"{self.file_path} Saved")

    def no_data(self):
        if len(self.data) == 0:
            return True
        return False

    def get_random_data_point(self):
        r = random.randint(1, self.length - 1)
        return self.data[r]

    def get_data_point(self, entry_id: int):
        return self.data[entry_id - 1]

    def show_all_data(self):
        for id, entry in enumerate(self.data, start=1):
            print(f"{id}: {entry}")


if __name__ == "__main__":
    test_api()
