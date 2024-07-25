from utils.screen import Screen

def test(screen: Screen):
     for _ in range(screen.height):
        starting_cell_value = screen.get_cell_value(_, _)

        # Draw Cell
        screen.update_cell(_, _, "@")

        # Display Screen
        os.system("cls")
        print(screen)

        # Undraw Cell
        screen.update_cell(_, _, starting_cell_value)

        # Pause and Clear Screen
        time.sleep(.5)

