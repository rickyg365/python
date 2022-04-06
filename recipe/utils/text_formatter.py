import os

from typing import List, Dict

# Do another one where it returns a list instead incase we want custom spacing
def parse_paragraph(raw_input:str, line_size=40) -> str:
    """ Take in a raw string and split w/ new lines of the chosen size """
    # Split input into Words
    word_list = raw_input.strip().split(" ")
    last_index = len(word_list) - 1

    # Init Final string
    output_string = ""

    # Init Line Variables
    current_line_text = ""
    current_line_length = 0

    for _, word in enumerate(word_list):
        current_word_length = len(word) + 1

        new_total = current_line_length + current_word_length

        if new_total > line_size:
            output_string += f"{current_line_text}\n"

            # Reset current line
            current_line_text = ""
            current_line_length = 0

        current_line_text += f"{word} "
        current_line_length += current_word_length

        if _ == last_index:
            output_string += f"{current_line_text}"

    return output_string



if __name__ == '__main__':
    test_string = "This is an example of a long string, This is an example of a long string, This is an example of a long string, This is an example of a long string"
    test_length = len(test_string)

    fixed_value = 15
    fixed_string = parse_paragraph(test_string, fixed_value)

    print(f"\nTest String:\n{test_length*'-'}\n{test_string}\n")

    print(f"Fixed String:\n{fixed_value*'-'}\n{fixed_string}\n")
