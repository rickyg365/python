import pyautogui

from utils.rapper import wait_for, find_n_click


def start_gamemode(gamemode: str):
    # Play Button
    find_n_click('images/play.png')
    pyautogui.sleep(1.5)

    # Gamemode Button
    match gamemode:
        case 'aram':
            find_n_click("images/aram.png")
        case 'auto':
            find_n_click("images/aram.png")
        case 'normal':
            find_n_click("images/aram.png")
        case 'special':
            find_n_click("images/special.png")
        case _:
            find_n_click("images/aram.png")

    # Confirm
    find_n_click("images/confirm.png")
    pyautogui.sleep(1.75)

    # Find Match
    find_n_click("images/find_match.png", confidence=0.75)
    
    # Accept Match
    wait_for('images/accept.png', max_iterations=15, redundancy=True)



def main():
    # Choose Gamemode
    gamemode = pyautogui.prompt('Select Gamemode:')

    if gamemode == 'auto':
        wait_for('images/accept.png', max_iterations=15, redundancy=True)
        return 

    delay = pyautogui.prompt('Select Delay(seconds):')

    if delay != "":
        # Delay
        d = int(delay)
        pyautogui.sleep(d)

    start_gamemode(gamemode)


if __name__ == "__main__":
    main()
