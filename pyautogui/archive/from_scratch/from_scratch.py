import json
import pyautogui

from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List, Dict, Callable


""" Template """

@dataclass
class Button:
    filename: str=None
    coordinates: List[int]=None  # [0, 0],
    search_time: int=15
    delay: int=1
    
    def __iter__(self):
        return iter((self.filename, self.coordinates, self.search_time))

    def update(self):
        return
    
    def export(self):
        return {
            'filename': self.filename,
            'coordinates': self.coordinates,
            'search_time': self.search_time
        }


class AutomationTemplate(ABC):
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
            return
        
        # Click Coordinates
        pyautogui.click(x, y)

    
    def input_text(self, text: str):
        return
    
    def wait_for(self, data: Button, max_iterations: int, redundancy: int=None):
        """
        Find Coordinate from image and click!

        image: str              Image path
        max_iterations: int     Minimum amount of times to search
        redundancy: bool        Keep searching after image found
        delay: int              Delay after each search/click
        
        return: None
        """

        for i in range(max_iterations):
            result = self.click(*data)
            if result:
                break
            
            print(i)
            pyautogui.sleep(1)

        # In case someone doesnt accept or something or dodges within first 3 min
        if not redundancy:
            return
        
        for _ in range(3):
            print(f"R{_}")
            
            result = self.click(*data)
            pyautogui.sleep(1)
        

class LeagueAuto(AutomationTemplate):
    PLAY_BUTTON = Button('images/play.png', [0, 0] ,search_time=45)
    GAMEMODE = Button('images/aram.png', None, search_time=45)
    CONFIRM = Button('images/confirm.png', None, search_time=45)
    FIND_MATCH = Button('images/find_match.png', None, search_time=45)
    ACCEPT = Button('images/accept.png', None, search_time=60)

    def __init__(self, filepath: str='data/default_button_data.json'):
        self.filepath = filepath

    def load_button_data(self):
        data = None
        with open(self.filepath, 'r') as load_buf:
            data = json.load(load_buf)

        # Place data
        play_data = data.get('play', None)
        gamemode_data = data.get('aram', None)
        confirm_data = data.get('confirm', None)
        find_match_data = data.get('find_match', None)
        accept_data = data.get('accept', None)
        
        self.PLAY_BUTTON = Button(**play_data)
        self.GAMEMODE = Button(**gamemode_data)
        self.CONFIRM = Button(**confirm_data)
        self.FIND_MATCH = Button(**find_match_data)
        self.ACCEPT = Button(**accept_data)
        
    def dump_button_data(self):
        data = {
            'play': self.PLAY_BUTTON.export(),
            'aram': self.GAMEMODE.export(),
            'confirm': self.CONFIRM.export(),
            'find_match': self.FIND_MATCH.export(),
            'accept': self.ACCEPT.export()
        }

        with open(self.filepath, 'w') as save_buf:
            json.dump(data, save_buf, indent=4)

    def load(self):
        # Click Play
        self.click(*self.PLAY_BUTTON)

        # Select Game mode
        self.click(*self.GAMEMODE)

        # Confirm (wait)
        self.click(*self.CONFIRM)

        # Find Match
        self.click(*self.FIND_MATCH)

        # Accept (if no queue timer)
        self.wait_for(self.ACCEPT, 15, 3)

        #? Notify

    def auto_accept(self):
        self.wait_for(self.ACCEPT, 15, 3)



if __name__ == '__main__':
    context = LeagueAuto()

    what_do = pyautogui.prompt("Load Game or Auto Accept:")

    match what_do:
        case 'aram':
            context.load()

        case 'a' | 'auto':
            context.auto_accept()

        case _:
            pass

    # context.dump_button_data()

