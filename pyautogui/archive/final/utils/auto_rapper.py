import pyautogui

from typing import List, Dict, Callable

""" 
Simplify PyAutoGUI tasks to basic functions that can be reused 
"""


class AutomationHelperFunction:
    def __init__(self):
        pass

    def defaulted_input(self, display_text: str, default_value=None):
        user_input = input(display_text)

        if user_input == "":
            return default_value
        
        return user_input

    def get_image(self, image_path: str) -> List[int]:
        """
        Screenshot a section of the screen between 2 points
        
        image: str          Image path
        search_time: int    Minimum amount of times to search
        confidence: float   Confidence percentage as decimal
        """
        input("Point 1: Place mouse over Top Left corner...")
        x1, y1 = pyautogui.position()
          
        input("Point 2: Place mouse over Bottom Right corner...")
        x2, y2 = pyautogui.position()

        width = x2 - x1
        height = y2 - y1
        
        pyautogui.screenshot(image_path, (x1, y1, width, height))
        
        # Centered Coordinates
        return x1 + width//2, y1 + height//2

    def find_coord(self, image: str, search_time: int=20, confidence: float=0.85):
        """
        Find Coordinate from image

        image: str          Image path
        search_time: int    Minimum amount of times to search
        confidence: float   Confidence percentage as decimal
        """
        result = None
        
        try:
            result = pyautogui.locateCenterOnScreen(image=image, minSearchTime=search_time, confidence=confidence)
        except Exception as e:
            pass
        return result
    
    def click(self, filename: str=None, coordinates: List[int]=None, search_time: int=15):
        x, y = None, None
        image_path = filename is not None
        has_coordinates = coordinates is not None
        
        # set x, y
        if has_coordinates:
            x, y = coordinates
        
        # Try Image first
        if image_path:
            # Find Image Coordinates
            result = self.find_coord(filename, search_time, confidence=0.85)

            if result is not None:
                x , y = result.x, result.y
        
        if x is None or y is None:
            return False
        
        # Click Coordinates
        pyautogui.click(x, y)
        return True

    
    def input_text(self, text: str):
        return
    
