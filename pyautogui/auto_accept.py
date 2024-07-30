import pyautogui
import time

from utils.rapper import find_n_click


if __name__ == "__main__":
    repeat = 8
    for _  in range(repeat):
        find_n_click("images/accept.png", search_time=280)
        time.sleep(1)


