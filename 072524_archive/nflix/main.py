import os
import json

from trie import Trie

from typing import Dict, List, Any


"""
Option #1: Dict<genre, code>
codes -> Dict[str, str]


Option #2: List + Code Class
class Code:
    genre
    code

codes = List[Code]
"""

def load_codes(filepath: str):
    codes = {}
    with open(filepath, 'r') as load_file:
        for line in load_file.readlines():
            genre, code = line.split(': ')
            codes[genre] = code.strip()
    # Return inside of with or nah
    return codes


def save_json(data: Dict[str, str], filepath: str):
    with open(filepath, 'w') as save_file:
        json.dump(data, save_file, indent=4)


def display_codes(codes: Dict[str, str]):
    for genre, code in codes.items():
        print(f"{genre}: {code}")


def build_trie(codes: Dict[str, str]):
    t = None
    return t


if __name__ == "__main__":
    c = load_codes("codes.txt")
    
    code_trie = Trie()

    code_line_str = [f"{genre}" for genre in c]

    for line in code_line_str:
        code_trie.insert(line.lower())

    save_json(c, "codes.json")
    
    display_codes(c)

    s1 = code_trie.search("horror")
    s2 = code_trie.starts_with("horr")

    print(s1)
    print(s2)
