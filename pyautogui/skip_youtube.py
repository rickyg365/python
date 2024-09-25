import pyautogui
import time

from utils.rapper import find_n_click


if __name__ == "__main__":
    repeat = 4
    for _ in range(repeat):
        find_n_click("images/skip_full.png", search_time=200, confidence=0.8)
        time.sleep(1)
      

