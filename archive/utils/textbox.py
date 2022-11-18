import os

"""
sample
╭
╮
╯
╰ 
─
│
"""

def format_paragraph(raw_string: str, max_width: int=20):
    """ Create a fixed width paragraph """
    return

def create_textbox(raw_string: str, max_width: int=25):
    """ Create a textbox from a string """
    word_list = raw_string.strip().split(" ")
    final_output = f"╭{max_width*'─'}╮\n"

    current_max = 0
    current_line = ""
    
    for word in word_list:
        new_max = current_max + len(word) + 1
        if new_max > max_width:
            final_output += f"│{current_line:{max_width}}│\n"
            current_max = 0
            current_line = ""
        current_max += len(word) + 1
        current_line += f" {word}"

        if word == word_list[-1]:
            final_output += f"│{current_line:{max_width}}│"
    final_output += f"\n╰{max_width*'─'}╯"

    return final_output

def main():
    sample_string = "This is just a random string to show that the function is working!"
    formatted_string = create_textbox(sample_string)
    print(sample_string)
    print(formatted_string)

if __name__ == '__main__':
    main()




