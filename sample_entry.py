import os

from typing import List, Dict
from dataclasses import dataclass, field

"""

─	━	│	┃	┄	┅	┆	┇	┈	┉	┊	┋	┌	┍	┎	┏
U+251x	┐	┑	┒	┓	└	┕	┖	┗	┘	┙	┚	┛	├	┝	┞	┟
U+252x	┠	┡	┢	┣	┤	┥	┦	┧	┨	┩	┪	┫	┬	┭	┮	┯
U+253x	┰	┱	┲	┳	┴	┵	┶	┷	┸	┹	┺	┻	┼	┽	┾	┿
U+254x	╀	╁	╂	╃	╄	╅	╆	╇	╈	╉	╊	╋	╌	╍	╎	╏
U+255x	═	║	╒	╓	╔	╕	╖	╗	╘	╙	╚	╛	╜	╝	╞	╟
U+256x	╠	╡	╢	╣	╤	╥	╦	╧	╨	╩	╪	╫	╬	╭	╮	╯
U+257x	╰	╴	╵	╶	╷	╸	╹	╺	╻	╼	╽	╾	╿


┌─┐
│ │
└─┘

╭─╮
│ │
╰─╯

┤ ├ ┼
┴ ┬
╭─┬─┬─╮
├─┼─┼─┤
├─┼─┼─┤
╰─┴─┴─╯


╭───┬───┬───╮
│   │   │   │
├───┼───┼───┤
│   │   │   │
├───┼───┼───┤
│   │   │   │
╰───┴───┴───╯

╭───┬───┬───╮
│ x │ x │ x │
├───┼───┼───┤
│ x │ x │ x │
├───┼───┼───┤
│ x │ x │ x │
╰───┴───┴───╯


Single Row ╭───┬───┬───╮
           │ x │ x │ x │
           ╰───┴───┴───╯

Top Row ╭───┬───┬───╮
        │ x │ x │ x │
Mid ROw ├───┼───┼───┤
        │ x │ x │ x │
Last ROw├───┼───┼───┤
        │ x │ x │ x │
        ╰───┴───┴───╯

"""

def title(raw_text:str):
    cleaned = raw_text.strip()[2:-2]
    return cleaned


def parse_raw_txt(filename="text_input.txt"):

    char_map = {
        '[': title,
    }

    with open(filename, 'r') as in_file:
        for line in in_file:
            first_char = line[0]
            # Apply appropriate parsing
            if first_char in char_map:
                new_line = char_map[first_char](line)
                

            pass


class Entry:
    def __init__(self, input_data: Dict[str, any]):
        self.data = input_data
        
    def __str__(self):
        entry_text = ""
        for section_name, section_data in self.data.items():
            section = f"\n[ {section_name.title()} ]\n{'-'*40}\n"

            for row in section_data:
                section += f"{row}\n"
            
            section += f"{'_'*40}"

            entry_text += f"{section}\n"
        
        return entry_text

    def display(self):
        for section_name, section_data in self.data.items():
            section = f"\n[ {section_name.title()} ]\n{'-'*40}\n"

            for row in section_data:
                section += f"{row}\n"
            
            section += f"{'_'*40}"

            os.system('cls')
            print(section)
            input()


def main():
    raw_text = f"""
[ Raccoons ]
----------------------------------------
A mammal that lives in cities

Fast | Rabies | Common
________________________________________


[ Velociraptor ]
----------------------------------------
a type of dinosaur

Fast | 2 Legs | Tail
________________________________________

[ Pandas ]
----------------------------------------
A type of bear that eats bamboo

Slow | Vege | Bear
________________________________________

[ Raccoons ]
----------------------------------------
A mammal that lives in cities

Fast | Rabies | Common
________________________________________

"""
    test_data = {
        "Velociraptor": ["a type of dinosaur", "", "Fast | 2 Legs | Tail"],
        "Pandas": ["A type of bear that eats bamboo", "","Slow | Vege | Bear"],
        "Raccoons": ["A mammal that lives in cities", "","Fast | Rabies | Common"]
    }
    
    new_entry = Entry(test_data)
    new_entry.display()
    print(new_entry)

    title('test')

if __name__ == '__main__':
    main()













