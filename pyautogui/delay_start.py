import pyautogui
import time

from utils.rapper import find_n_click


if __name__ == "__main__":
    # Choose Gamemode
    gamemode = pyautogui.prompt('Select Gamemode:')
    delay = pyautogui.prompt('Select Delay(seconds):')

    # Delay
    d = int(delay)
    time.sleep(d)

    # Play Button
    find_n_click('images/play.png')
    time.sleep(1.5)
    # Gamemode Button
    match gamemode:
        case 'aram':
            find_n_click("images/aram.png")
        case 'normal':
            find_n_click("images/aram.png")
        case 'special':
            find_n_click("images/special.png")
        case _:
            find_n_click("images/aram.png")
    time.sleep(1)

    # Confirm
    find_n_click("images/confirm.png")
    time.sleep(1.75)

    # Find Match
    find_n_click("images/find_match.png", confidence=0.75)
    
    # Accept Match
    repeat = 4
    for _ in range(repeat):
        find_n_click("images/accept.png", search_time=300)
        time.sleep(1)

