import os

class Screen():
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.default_char = " "
        self.data = None

        self.refresh()

    def __str__(self) -> str:
        return "\n".join(["".join(row) for row in self.data])

    def refresh(self):
        pass


class Object:
    def __init__(self, starting_x: int=0, starting_y: int=0):
        self.default_char = '@'

        self.x = starting_x
        self.y = starting_y

        self.speed = 1

    def draw(self, screen_object: Screen):
        pass





def game(screen_width, screen_height):
    # Screen
    s = Screen(screen_width, screen_height)

    print(s)


if __name__ == "__main__":
    game()

