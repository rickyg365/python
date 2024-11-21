import time

from utils.auto_rapper import AutomationHelperFunction


if __name__ == "__main__":
    helper = AutomationHelperFunction()
    
    while True:
        helper.click("images/skip_full.png", search_time=120)

        u_in = input("Enter to run again or q to quit: ")
        if u_in == 'q':
            break
