import pyautogui
import time

from utils.rapper import find_n_click, wait_for
# from auto_accept import auto_accept

def start_gamemode(gamemode: str):
    # Play Button
    find_n_click('images/play.png')
    time.sleep(1.5)

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
    time.sleep(1.75)

    # Find Match
    find_n_click("images/find_match.png", confidence=0.75)
    
    # Accept Match
    wait_for('images/accept.png', 15, True)


if __name__ == "__main__":
    # Choose Gamemode
    gamemode = pyautogui.prompt('Select Gamemode:')
    start_gamemode(gamemode)
