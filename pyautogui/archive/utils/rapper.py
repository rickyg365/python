import pyautogui

def find_coord(image: str, search_time: int=20, confidence: float=0.85):
    """
    Find Coordinate from image

    image: str          Image path
    search_time: int    Minimum amount of times to search
    confidence: float   Confidence percentage as decimal
    """
    result = None
    # pyautogui.locateOnScreen('someButton.png', region=(0,0, 300, 400))
    try:
        result = pyautogui.locateCenterOnScreen(image=image, minSearchTime=search_time, confidence=confidence)
    except Exception as e:
        pass
    return result

   
def find_n_click(image: str, search_time: int=20, confidence:float=0.85) -> bool:
    """
    Find Coordinate from image and click!

    image: str          Image path
    search_time: int    Minimum amount of times to search
    confidence: float   Confidence percentage as decimal

    return bool         True if image found else False
    """
    # pyautogui.locateOnScreen('someButton.png', region=(0,0, 300, 400))
    result = find_coord(image=image, search_time=search_time, confidence=confidence)
    if result is None:
        return False
    # pyautogui.sleep(wait_time)
    
    pyautogui.click(result.x, result.y)
    return True
    

def wait_for(image: str, max_iterations: int=15, redundancy: bool=False, delay: int=1, confidence: float=0.85):
    """
    Find Coordinate from image and click!

    image: str              Image path
    max_iterations: int     Minimum amount of times to search
    redundancy: bool        Keep searching after image found
    delay: int              Delay after each search/click
    
    return: None
    """
    for i in range(max_iterations):
        result = find_n_click(image, search_time=60, confidence=confidence)
        if result:
            break
        
        print(i)
        pyautogui.sleep(delay)

    # In case someone doesnt accept or something or dodges within first 3 min
    if not redundancy:
        return
    
    for _ in range(3):
        print(f"R{_}")
        
        result = find_n_click(image, search_time=60, confidence=confidence)
        pyautogui.sleep(delay)
    

