import os
import json

from typing import List, Dict, Union
from dataclasses import dataclass


def save_json(data: Union[Dict, List], filepath: str):
    # Create dir if not exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    with open(filepath, 'w') as save_buf:
        json.dump(data, save_buf, indent=4)

    return

def load_json(filepath: str):
    data = None
    with open(filepath, 'r') as load_buf:
        data = json.load(load_buf)

    return data

def load_data_if_exists(filepath: str):
    """
    Return data if exists else returns none
    """
    # Try Loading Data
    data_exists = os.path.isfile(filepath)
    
    if data_exists:
        return load_json(filepath)

    return None



@dataclass
class ProgressBarConfig:
    fill: str='*'
    empty: str=' '
    left_end: str='['
    right_end: str=']'


def progress_bar(current: int, max: int, width: int=20, config: ProgressBarConfig=None):
    if config is None:
        config = ProgressBarConfig()
    
    f = config.fill
    e = config.empty
    l_e = config.left_end
    r_e = config.right_end

    ratio = current/max

    fill_amount = int(width * ratio)

    if fill_amount == 0 and current > 0:
        fill_amount = 1
    
    empty_amount = width - fill_amount

    return f"{l_e}{fill_amount * f}{empty_amount * e}{r_e}"



def test_progress_bar():
    CUSTOM_CONFIG = ProgressBarConfig(fill='*', empty=' ', left_end='(', right_end=')')

    CURRENT = 100
    MAX = 100
    WIDTH = 25

    while CURRENT + 1:
        current_bar = progress_bar(current=CURRENT, max=MAX, width=WIDTH, config=CUSTOM_CONFIG)
        input(current_bar)

        CURRENT -= 1

    
if __name__ == "__main__":
    TESTS = [
        test_progress_bar,
    ]

    for test in TESTS:
        # Run Test
        test()
    
    # (t() for t in TESTS)


