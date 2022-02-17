import os
import sqlite3


class WordDatabase:
    def __init__(self, filepath="four_letter.db") -> None:
        self.conn = sqlite3.connect(filepath)
        self.cursor = self.conn.cursor()

    


