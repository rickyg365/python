import os


"""
─	━	│	┃	┄	┅	┆	┇	┈	┉	┊	┋	┌	┍	┎	┏
┐	┑	┒	┓	└	┕	┖	┗	┘	┙	┚	┛	├	┝	┞	┟
┠	┡	┢	┣	┤	┥	┦	┧	┨	┩	┪	┫	┬	┭	┮	┯
┰	┱	┲	┳	┴	┵	┶	┷	┸	┹	┺	┻	┼	┽	┾	┿
╀	╁	╂	╃	╄	╅	╆	╇	╈	╉	╊	╋	╌	╍	╎	╏
═	║	╒	╓	╔	╕	╖	╗	╘	╙	╚	╛	╜	╝	╞	╟
╠	╡	╢	╣	╤	╥	╦	╧	╨	╩	╪	╫	╬		


"""


class Box:
    STYLE = {
        "square": {
            "vertical": "│",
            "horizontal": "─",
            "top_left": "┌",
            "top_right": "┐",
            "bot_left": "└",
            "bot_right": "┘"
        },
        "bold": {
            "vertical": "┃",
            "horizontal": "━",
            "top_left": "┏",
            "top_right": "┓",
            "bot_left": "┗",
            "bot_right": "┛"
        },
        "round": {
            "vertical": "│",
            "horizontal": "─",
            "top_left": "╭",
            "top_right": "╮",
            "bot_left": "╰",
            "bot_right": "╯"
        }
    }
    def __init__(self, length: int, width: int, style="square"):
        # Does size include corners?
        self.length = length
        self.width = width

        self.style = self.STYLE[style]

    def __str__(self) -> str:
        output = f"{self.style['top_left']}{self.style['horizontal']*self.width}{self.style['top_right']}"

        for i in range(self.length):
            output += f"\n{self.style['vertical']}{' '*self.width}{self.style['vertical']}"
        
        output += f"\n{self.style['bot_left']}{self.style['horizontal']*self.width}{self.style['bot_right']}"
        return output


def main():
    new_box = Box(0, 0, "round")

    print(new_box)

if __name__ == '__main__':
    main()
