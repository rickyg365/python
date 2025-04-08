import os

from dataclasses import dataclass

@dataclass
class StatusbarConfig:
    fill: str='*'
    empty: str=' '
    left: str='['
    right: str=']'

def status_bar(current_value: int, max_value: int, bar_length: int=20, config: StatusbarConfig=None):
    if config is None:
        config = StatusbarConfig()  # Default

    # Process Data
    working_length = bar_length - 2
    ratio = current_value/max_value
    
    fill_length = int(ratio * working_length)

    # Special case
    trigger_special = fill_length == 0 and current_value != 0

    if trigger_special:
        fill_length = 1

    empty_length = working_length - fill_length
    
    return f"{config.left}{fill_length*config.fill}{empty_length*config.empty}{config.right}"


if __name__ == "__main__":
    custom_config = {
        'fill': '*',
        'empty': ' ',
        'left': '[',
        'right': ']'
    }

    new_bar = status_bar(20, 30, config=StatusbarConfig(**custom_config))
    print(new_bar)
