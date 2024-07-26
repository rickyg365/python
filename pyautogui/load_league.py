import pyautogui
import time


def find_n_click(image: str, search_time: int=20, confidence:float=0.85):
    result = pyautogui.locateCenterOnScreen(image=image, minSearchTime=search_time, confidence=confidence)
    pyautogui.sleep(0.5)
    pyautogui.click(result.x, result.y,)



if __name__ == "__main__":
    gamemode = pyautogui.prompt('Select Gamemode:')
    find_n_click('images/play.png')
    time.sleep(1.5)
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

    find_n_click("images/confirm.png")
    time.sleep(2)
    find_n_click("images/find_match.png", confidence=0.75)
    
    repeat = True
    while repeat:
        find_n_click("images/accept.png", search_time=480)
        repeat = True if pyautogui.prompt("Break?") == '' else False

