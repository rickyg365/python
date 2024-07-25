import os
import random

"""
╭───────╮
│       │
│   ▪️   │
│       │
╰───────╯
╭───────╮
│ ▪️     │
│       │
│     ▪️ │
╰───────╯
╭───────╮
│ ▪️     │
│   ▪️   │
│     ▪️ │
╰───────╯
╭───────╮
│ ▪️   ▪ │
│       │
│ ▪   ▪️ │
╰───────╯

╭───────╮
│ ▪️   ▪ │
│   ▪   │
│ ▪   ▪️ │
╰───────╯

╭───────╮
│ ▪️   ▪ │
│ ▪   ▪ │
│ ▪   ▪️ │
╰───────╯

╭───────╮
│ ▪️ ▪ ▪ │
│   ▪   │
│ ▪ ▪ ▪️ │
╰───────╯

╭───────╮
│ ▪️ ▪ ▪ │
│ ▪   ▪ │
│ ▪ ▪ ▪️ │
╰───────╯

╭───────╮
│ ▪️ ▪ ▪ │
│ ▪ ▪ ▪ │
│ ▪ ▪ ▪️ │
╰───────╯
"""

"""
  1  2  3
╭───────╮
│ {} {} {} │  1
│ {} {} {} │  2
│ {} {} {} │  3
╰───────╯

#1
(2, 2)

#2
(1, 1)(3, 3)

#3
(1, 1)(2, 2)(3, 3)

#4
(1,1)(3, 1)(1, 3)(3, 3)

#5
(1,1)(3, 1)(2, 2)(1, 3)(3, 3)

#6
(1,1)(1, 2)(1, 2)(3, 1)(3, 2)(3, 3)



  1  2  3
╭───────╮
│ {1} {2} {3} │  1
│ {4} {5} {6} │  2
│ {7} {8} {9} │  3
╰───────╯

#1
(5)

#2
(1)(9)

#3
(1)(5)(9)

#4
(1)(3)(7)(9)

#5
(1)(3)(5)(7)(9)

#6
(1)(4)(7)(3)(6)(9)



7 positions to keep track of
1_1 -> 1
3_1 -> 3
1_2 -> 4
2_2 -> 5
3_2 -> 6
1_3 -> 7
3_3 -> 9
"""


def unify_multiline_string(string1: str, string2: str):
    """ Join two multi line strings w/ same number of lines """
    # Split into lines
    lined_s1 = string1.strip().split("\n")
    lined_s2 = string2.strip().split("\n")

    # Can optionally clean up lines here

    # Check to make sure they have same number of lines
    if len(lined_s1) != len(lined_s2):
        print("Line Length Mismatch: Fuck Off!")
        return  # Raise error lmao

    new_string = ""
    spacing = "   "
    for _, val in enumerate(lined_s1):
        new_string += f"{val}{spacing}{lined_s2[_]}\n"

    return new_string


class Dice:
    def __init__(self, number: int=0):
        self.number = number

        # Initial Data
        self.data = [0 for i in range(9)]
        self.state = {
            "1": " ",
            "2": " ",
            "3": " ",
            "4": " ",
            "5": " ",
            "6": " ",
            "7": " ",
            "8": " ",
            "9": " "
        }
        self.key = None
        self.cache = None

        # Update State using number
        self.update_by_key(self.key_from_number(number))

    def __str__(self) -> str:
        return self.build_dice()

    def key_from_data(self):
        # key = ""
        # for pos, state in enumerate(self.data):
        #     if state:
        #         key += f"{pos+1}"
        # return key

        return "".join([f"{pos+1}" for pos, state in enumerate(self.data) if state])

    def key_from_number(self, number: int):
        num_map = {
            1: "5",
            2: "19",
            3: "159",
            4: "1379",
            5: "13579",
            6: "147369",
        }
        return num_map.get(number, 1)

    def build_dice(self):
        """ Build Dice using curent data """
        current_key = self.key_from_data()
        
        for pos in list(current_key):
            self.state[pos] = "▪"
            
        self.cache = f"""        
╭───────╮
│ {self.state["1"]} {self.state["2"]} {self.state["3"]} │
│ {self.state["4"]} {self.state["5"]} {self.state["6"]} │
│ {self.state["7"]} {self.state["8"]} {self.state["9"]} │
╰───────╯
"""
        return self.cache

    def update_by_key(self, new_key: str):
        """ Update data, key, cache based on new key """
        nums = [int(x) for x in list(new_key)]  # Use this in that other spot in build_dice method

        for _, num in enumerate(self.data):
            if _+1 in nums:
                self.data[_] = 1
                continue

            self.data[_] = 0
        
        self.key = new_key
        self.build_dice()



if __name__ == "__main__":
    NUM_DICE = 5
    dice = []
    
    for i in range(NUM_DICE):
        r = random.randint(1, 6)

        dice.append(Dice(r))

    combined_str = None
    for d in dice:
        if combined_str is None:
            combined_str = d.cache
            continue

        combined_str = unify_multiline_string(combined_str, d.cache)
    print(combined_str)
