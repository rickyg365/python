import os
import time

from typing import List, Dict, Any, Callable, Optional

""" 

"""

# Type Aliases
iterable = List[Any]
generic_callback = Callable[[Any], Any]


def progress_bar(list_of_items: iterable, callback: generic_callback, custom_width: int=48):
    """ Display a progress bar while applying a callback to a list of elements """
    new_list = []
    total_length = len(list_of_items)
    fixed_custom_width = custom_width - 8

    for _, item in enumerate(list_of_items, start=1):
        ratio = _ / total_length
        flat_ratio = int(ratio * fixed_custom_width)

        current_space = fixed_custom_width - flat_ratio

        # add new element to list
        new_list.append(callback(item))
        print(f"{_:>3}/{total_length:<3} {'■'*flat_ratio}{' '*current_space}", end="\r")

    print()
    return new_list


def test_callback(item: Any):
    # Mutate Data Here
    time.sleep(.1)
    return item


def main():
    terminal_width, terminal_height = os.get_terminal_size()


    my_list = [x for x in range(100)]
    progress_bar(my_list, test_callback, terminal_width)


if __name__ == "__main__":
    main()
