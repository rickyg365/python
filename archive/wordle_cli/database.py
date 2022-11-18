import imp
import os
import sqlite3

from typing import List


def load_wordbank(file_path: str) -> List[str]:
    # Load file in read mode
    with open(file_path, 'r') as in_file:
        word_bank = in_file.read().strip().split("\n")

    return word_bank


class WordDatabase:
    def __init__(self, filepath="four_letter.db") -> None:
        self.conn = sqlite3.connect(filepath)
        self.cursor = self.conn.cursor()

    


