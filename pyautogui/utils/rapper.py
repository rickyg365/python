import pyautogui

def find_n_click(image: str, search_time: int=20, confidence:float=0.85):
    result = pyautogui.locateCenterOnScreen(image=image, minSearchTime=search_time, confidence=confidence)
    pyautogui.sleep(0.25)
    pyautogui.click(result.x, result.y,)
    

