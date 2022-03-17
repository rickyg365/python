import pyautogui
import webbrowser

from typing import List

"""
Notes:


"""

def open_app_by_name(application_name: str, interval:float=.18):
    """ Using pyautogui to manually input application name in windows key menu """
    keys = ['win', *list(application_name), 'enter']
    # print(keys)
    pyautogui.typewrite(keys, interval=interval)

# Open new urls
def open_urls(urls: List[str], new_window: bool=True, browser: str='chrome'):
    """ Opens """
    # Set because we are using to test for membership
    valid_browsers = {'chrome', 'firefox'}

    if new_window and browser in valid_browsers:
        open_app_by_name(browser)

    for url in urls:
        webbrowser.open_new(url)


if __name__ == '__main__':
    pass
