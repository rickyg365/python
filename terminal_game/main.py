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
        self.data = [[self.default_char for y in range(self.width)] for x in range(self.height)]


class Object:
    def __init__(self, starting_x: int=0, starting_y: int=0):
        self.default_char = '@'

        self.x = starting_x
        self.y = starting_y

        self.speed = 1

    def draw(self, screen_object: Screen):
        screen_object.data[self.y%(screen_object.height)][self.x%(screen_object.width)] = self.default_char



def game(screen_width, screen_height):
    # Screen
    s = Screen(screen_width, screen_height)

    print(s)

    # Player Object
    player = Object(screen_width//2, screen_height//2)
    
    STATUS_TEXT = ">>> "
    
    while True:
        s.refresh()
        player.draw(s)
        print(s)

        action = input(STATUS_TEXT)
        STATUS_TEXT = ">>> "
        speed = player.speed

        if action == 'q':
            break
        elif action == 'w':
            player.y-=speed
        elif action == 's':
            player.y+=speed
        elif action == 'a':
            player.x-=speed
        elif action == 'd':
            player.x+=speed
        elif action == 'speed':
            new_speed = None
            
            while new_speed is None:
                try:
                    user_in = int(input("Select new speed: "))
                    new_speed = user_in
                except ValueError as e:
                    pass
            player.speed = new_speed
        else:
            STATUS_TEXT = "Invalid Option >>> "


if __name__ == "__main__":
    TERMINAL_WIDTH, TERMINAL_HEIGHT = os.get_terminal_size()
    # print(TERMINAL_WIDTH, TERMINAL_HEIGHT)
    game(TERMINAL_WIDTH, TERMINAL_HEIGHT - 2)

