import pyautogui

from dataclasses import dataclass
from typing import List, Dict, Callable

from utils.file_handler import load_json, save_json
from utils.auto_rapper import AutomationHelperFunction


@dataclass
class AutomationAction(AutomationHelperFunction):
    filename: str=None
    coordinates: List[int]=None
    search_time: int=15
    max_iterations: int=2
    redundancy: int = 0

    def run(self):
        raise NotImplementedError
    
    def create(self):
        raise NotImplementedError

    def export(self):
        raise NotImplementedError


class Button(AutomationAction):
    
    def __iter__(self):
        return iter((self.filename, self.coordinates, self.search_time))
    
    def run(self):
        self.click(filename=self.filename, search_time=self.search_time)
    
    def create(self):
        """
        filename: str
        coordinates: [int, int]
        search_time: int
        """
        self.filename = ""
        image_path = input("image path: ")
        if image_path == "":
            input("Place mouse over Center...")
            x, y = pyautogui.position()
            self.coordinates = [x, y]

        else:
            self.filename = image_path
            self.coordinates = self.get_image(self.filename)
        
        self.search_time = int(self.defaulted_input("Search Time: ", 25))
        
        return self
    
    def export(self):
        return {
            'filename': self.filename,
            'coordinates': self.coordinates,
            'search_time': self.search_time
        }


@dataclass
class Popup(AutomationAction):

    def __iter__(self):
        return iter((self.filename, self.coordinates, self.search_time))

    def run(self):
        """
        Wait for image and click!

        image: str              Image path
        max_iterations: int     Minimum amount of times to search
        redundancy: bool        Keep searching after image found
        """

        for i in range(self.max_iterations):
            result = self.click(self.filename, self.coordinates, self.search_time)
            if result:
                break
            
            print(i)
            pyautogui.sleep(1)

        # In case someone doesnt accept or something or dodges within first 3 min
        for _ in range(self.redundancy):
            print(f"R{_}")
            
            result = self.click(self.filename, self.coordinates, self.search_time)
            pyautogui.sleep(1)
    
    def create(self):
        """
        filename: str
        coordinates: [int, int]
        search_time: int
        max_iterations: int
        redundancy: int
        """
        self.filename = ""
        image_path = input("Image name: ")
        if image_path == "":
            input("Place mouse over Center...")
            x, y = pyautogui.position()
            self.coordinates = [x, y]

        else:
            self.filename = image_path
            self.coordinates = self.get_image(self.filename)

        self.search_time = int(self.defaulted_input("Search Time: ", 25))
        self.max_iterations = int(self.defaulted_input("Max Iterations: ", 2))
        self.redundancy = int(self.defaulted_input("Redundancy: ", 1))
        
        return self
    
    def export(self):
        return {
            'filename': self.filename,
            'coordinates': self.coordinates,
            'search_time': self.search_time,
            "max_iterations": self.max_iterations,
            "redundancy": self.redundancy
        }


class AutomationStep():
    TYPE_MAP = {
        'button': Button,
        'text': Button,
        'popup': Popup
    }

    def __init__(self, datatype: str=None, data: AutomationAction = None):
        if datatype not in self.TYPE_MAP.keys():
            datatype = None
                
        self.datatype = datatype
        self.data = data

        # Meta
        self.pre_delay = 0
        self.post_delay = 1

    def play(self):
        if self.data is None:
            return

        try:
            pyautogui.sleep(self.pre_delay)
            self.data.run()
            pyautogui.sleep(self.post_delay)
        except Exception as e:
            print(e)
    
    def import_raw_data(self, raw_data):
        if self.datatype is None:
            return      
        null_fn = lambda *a, **kw: None  # Helper function that returns None
        # Convert data into python object based on typemap
        object_create_func = self.TYPE_MAP.get(self.datatype, null_fn)

        # Update Object
        self.data = object_create_func(**raw_data)

        return self
    
    def create(self):
        if self.datatype is None:
            return
        
        object_func = self.TYPE_MAP.get(self.datatype, None)

        # Update Object
        self.data = object_func.create()

        return self

    def export(self):
        return {
            'data': self.data if self.data is None else self.data.export(),
            'datatype': self.datatype,
            'pre_delay': self.pre_delay,
            'post_delay': self.post_delay,
        }


class AutomationList:
    def __init__(self, filename: str=None, data=None):
        self.filename = filename
        self.data = data

        if self.filename is not None:
            self.load_data()

    def __str__(self):
        # Data Check #
        has_data = '#' if self.has_data else ' '
        txt = f"Current File [{has_data}]: {self.filename}"
        return txt
    
    def parse_data(self, raw_data):
        if raw_data is None:
            return None

        output_data = []
        for item in raw_data:
            d = item.get('data', None)
            data_type = item.get('datatype', None)

            new_step = AutomationStep(data_type).import_raw_data(d)

            output_data.append(new_step)

        return output_data
    
    def load_data(self, new_filename: str=None):
        if new_filename is not None:
            self.filename = new_filename
        
        raw_data = load_json(self.filename)
        self.data = self.parse_data(raw_data)

    def save_data(self):
        if self.data is None:
            return
        
        export_data = [i.export() for i in self.data]
        save_json(export_data, self.filename)

    def run(self):
        """ Run Automation """
        if self.data is None:
            return
        
        for item in self.data:
            item.play()

    def create(self):
        """ Create a map (list of automation steps) """
        if self.filename is None:
            self.filename = input("Choose filename for map: ")

        new_map = []

        while True:
            new_step_type = input("What type of action [ Button | Popup | >Text< ]: ")

            if new_step_type == 'q':
                break

            if new_step_type in ['button', 'popup']:
                new_map.append(AutomationStep(new_step_type).create())

        self.data = new_map

