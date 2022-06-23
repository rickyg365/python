import os
import random
from rich.console import Console


class ColorCell:
    def __init__(self, color: str="black"):
        self.color = color

    def __str__(self) -> str:
        return f"[default on {self.color}]  "


class ColorGrid:
    def __init__(self, width: int, height: int, default_color: str="white"):
        self.width = width
        self.height = height

        self.color = default_color
        self.data = self.build_grid()

    def __str__(self) -> str:
        txt = f""
        for row in self.data:
            for cell in row:
                txt += f"{cell}"
            txt += "\n"
        return txt
    
    def build_grid(self, custom_color: str=None):
        if custom_color is None:
            custom_color = self.color

        new_grid = []
        for i in range(self.height):
            new_row = []
            for j in range(self.width):
                new_row.append(ColorCell(custom_color))
            new_grid.append(new_row)
        
        return new_grid


class RubixCube:
    def __init__(self):
        # Top, Front, Right, Back, Left, Bottom
        self.faces = ["red", "green", "blue", "yellow", "white", "black"]
        self.current_face = 0
        self.face_data = None

        self.update_face()

    def __str__(self) -> str:
        return f"{self.face_data}"

    def update_face(self, new_face: int=None):
        if new_face is not None:
            self.current_face = new_face
            
        self.face_data = ColorGrid(3, 3, self.faces[self.current_face])


def main():
    console = Console()

    console.rule("Title")

    # c = ColorCell("red")
    # console.print(f"{c}")

    # console.rule("Title")

    # g = ColorGrid(3, 3, 'red')
    # console.print(f"{g}")

    r = RubixCube()
    console.print(f"{r}")

    while True:
        os.system('cls')
        console.print(f"{r}")
        u_in = input(">>> ")
        r.update_face(int(u_in))

if __name__ == '__main__':
    main()
