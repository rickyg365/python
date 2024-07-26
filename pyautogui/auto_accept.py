import pyautogui
import time



def find_n_click(image: str, search_time: int=20, confidence:float=0.85):
    result = pyautogui.locateCenterOnScreen(image=image, minSearchTime=search_time, confidence=confidence)
    pyautogui.sleep(0.5)
    pyautogui.click(result.x, result.y,)



if __name__ == "__main__":
    repeat = 3
    for _  in range(repeat):
        find_n_click("images/accept.png", search_time=240)


