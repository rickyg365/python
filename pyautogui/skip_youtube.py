import time

from utils.auto_rapper import AutomationHelperFunction


if __name__ == "__main__":
    helper = AutomationHelperFunction()
    
    repeat = 4
    for _ in range(repeat):
        helper.click("images/skip_full.png", search_time=200)
        time.sleep(1)

