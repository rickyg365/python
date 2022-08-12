import os


# class Display:
#     def __init__(self) -> None:
#         pass

#     def __str__(self) -> str:
#         txt = ""
#         return txt


"""
. . .
. . .
. . .

X X O
. O .
X O .

a b c
d e f
g h i


"""

class Display:
    def __init__(self, width: int, height: int, default_character: str="."):
        self.w = width
        self.h = height
        self.default_char = default_character
        self.data = self.build_blank()

    def __str__(self) -> str:
        txt = ""
        # Build Screen
        for i in range(self.h):
            for j in range(self.w):
                # self.data[i][j]
                txt += f"{self.data[i][j]} "
            txt += "\n"
        return txt
    
    def build_blank(self):
        # new_blank = []
        # for i in range(self.h):
        #     row = []
        #     for j in range(self.w):
        #         row.append(self.default_char)
        #     new_blank.append(row)

        new_blank = [[self.default_char for c in range(self.w)] for r in range(self.h)]
        return new_blank

    def edit_cell(self, new_value, row: int, col: int):
        self.data[row][col] = new_value
        


def main():
    new_display = Display(3, 3)
    print(new_display)

    new_display.edit_cell("X", 1, 1)
    print(new_display)
    #

    players = {
        0: "O",
        1: "X",
    }

    custom_map = {
        "a": [0, 0],
        "b": [0, 1],
        "c": [0, 2],
        "d": [1, 0],
        "e": [1, 1],
        "f": [1, 2],
        "g": [2, 0],
        "h": [2, 1],
        "i": [2, 2],
    }
    current_player = 0
    while True:
        print(new_display)
        u_in = input(">>> ")

        match u_in:
            case "q":
                break
            case _:
                if u_in not in custom_map.keys():
                    continue
                r, c = custom_map[u_in]
                if current_player > 0:
                    current_player -= 1
                else:
                    current_player += 1

                new_display.edit_cell(players[current_player], r, c)


    return

if __name__ == '__main__':
    
    new_display = Display(10, 8)
    print(new_display)
    # main()