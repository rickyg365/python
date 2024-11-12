import os
import json


import pyautogui
from utils.rapper import find_coord, find_n_click, wait_for


def save_json(data, filepath: str):
    with open(filepath, 'w') as save_buf:
        json.dump(data, save_buf, indent=4)
    

def load_json(filepath: str):
    data = None
    with open(filepath, 'r') as load_buf:
        data = json.load(load_buf)
    return data


# pyautogui.screenshot()

def get_image(dir_path):
    input("place mouse over top left corner!")
    X1, Y1 = pyautogui.position()

    input("place mouse over bottom right corner!")
    X2, Y2 = pyautogui.position()

    WIDTH = X2 - X1
    HEIGHT = Y2 - Y1

    filename = input("Filename: ")
    
    FILEPATH = f"{dir_path}/{filename}.png"
    
    pyautogui.screenshot(FILEPATH, (X1, Y1, WIDTH, HEIGHT))

    return FILEPATH


def get_image_manual(dir_path):
    pyautogui.displayMousePosition()

    get_int = lambda x: int(input(x))
    X = (get_int("X Coordinate: "))
    Y = (get_int("Y Coordinate: "))

    WIDTH = (get_int("Width: "))
    HEIGHT = (get_int("Height: "))
    
    filename = input("Filename: ")
    FILEPATH = f"{dir_path}/{filename}.png"

    pyautogui.screenshot(FILEPATH, (X, Y, WIDTH, HEIGHT))

    return FILEPATH

def get_coordinates(text):
    input(text)
    return pyautogui.position()


# Automation Inputs



"""
case 't' | 'text':
    type = 'text'
    text = input("Text: ")
    coordinates = get_coordinates("Place mouse over textbox and press enter...")
    delay = int(input("Delay: "))

case 'c' | 'click':
    type = 'click'
    image = get_image(PROJECT_PATH)
    delay = int(input("Delay: "))
    
case 'w' | 'wait':
    type = 'wait'
    image = get_image(PROJECT_PATH)
    iter_count = int(input("Max iteration count: "))
    delay = int(input("Delay: "))

    
case 'text':
    x, y = item.get('coordinates', (0, 0))
    txt = item.get('text', '')
    delay = item.get('delay', 1)

    pyautogui.click(x, y)
    pyautogui.sleep(delay)
    pyautogui.typewrite(f'{txt}\n', interval=0.1)

case 'click':
    img = item.get("image", None)
    delay = item.get('delay', 1)

    find_n_click(img)
    pyautogui.sleep(delay)

case 'wait':
    img = item.get("image", None)
    delay = item.get('delay', 1)
    max_iterations = item.get('iter_count', 1)

    wait_for(img, max_iterations=max_iterations, delay=delay)


"""









class AutomationBlock:
    def __init__(self, type: str, text: str=None, coordinates=None, delay: int=0, image: str=None, iter_count: int=1):
        self.type = type  # 'text' | 'click' | 'wait'
        self.text = text
        self.coordinates = coordinates
        self.delay = delay
        self.image = image
        self.iter_count = iter_count
        
    def __str__(self):
        s = f'{self.type}'
        return s
    
    def play(self):
        raise NotImplementedError
    
    def get_input(self):
        return
    
    def export(self):
        return {
            "type": self.type,
            "coordinates": self.coordinates,
            "text": self.text,
            "image": self.image,
            "delay": self.delay,
            "iter_count": self.iter_count
        }


class Click(AutomationBlock):
    def __init__(self, coordinates=None, delay: int=0, image: str=None, iter_count: int=1):
        super().__init__(type="click", coordinates=coordinates, delay=delay, image=image, iter_count=iter_count)
    
    def __str__(self):
        s = f'{self.type}'
        return s
    
    def play(self):
        if self.image != "":
            find_n_click(self.image)
        else:
            x, y = self.coordinates
            pyautogui.click(x, y)
        pyautogui.sleep(self.delay)
    
    def get_input(self):
        self.image = input("image: ")
        if self.image == "":
            self.coordinates = get_coordinates("Place mouse over point...")
        if self.image == "get":
            self.image = get_image()
        self.delay = int(input("delay: "))
        self.iter_count = int(input("iter_count: "))
        
    def export(self):
        return {
            "type": self.type,
            "coordinates": self.coordinates,
            "image": self.image,
            "delay": self.delay,
            "iter_count": self.iter_count
        }


class Text(AutomationBlock):
    def __init__(self, text: str=None, coordinates=None, delay: int=0):
        super().__init__(type="text", text=text, coordinates=coordinates, delay=delay)
    
    def __str__(self):
        s = f'{self.type}'
        return s
    
    def play(self): 
        x, y = self.coordinates
    
        pyautogui.click(x, y)
        pyautogui.sleep(self.delay)
        pyautogui.typewrite(f'{self.text}\n', interval=0.1)

    def get_input(self):
        self.text = input("Text: ").strip()
        self.delay = int(input("delay: "))
        self.coordinates = get_coordinates("Place mouse over textbox and press enter...")

    def export(self):
        return {
            "type": self.type,
            "text": self.text,
            "coordinates": self.coordinates,
            "delay": self.delay,
            "iter_count": self.iter_count
        }


class WaitClick(AutomationBlock):
    def __init__(self, coordinates=None, delay: int=0, image: str=None, iter_count: int=60):
        super().__init__(type="click", coordinates=coordinates, delay=delay, image=image, iter_count=iter_count)
    
    def __str__(self):
        s = f'{self.type}'
        return s
    
    def play(self):
        wait_for(self.image, max_iterations=self.iter_count, delay=self.delay)

    def get_input(self):
        self.image = input("image: ")
        self.delay = int(input("delay: "))
        self.iter_count = int(input("iter_count: "))

    def export(self):
        return {
            "type": self.type,
            "coordinates": self.coordinates,
            "image": self.image,
            "delay": self.delay,
            "iter_count": self.iter_count
        }

class DelayText(AutomationBlock):
    def __init__(self, text: str, coordinates=None, delay: int=0):
        super().__init__(type="text", text=text, coordinates=coordinates, delay=delay)
    
    def __str__(self):
        s = f'{self.type}'
        return s
    
    def play(self):
        # find_n_click(self.image)
        # pyautogui.sleep(self.delay)
        ...

    def get_input(self):
        ...

    def export(self):
        return {
            "type": self.type,
            "text": self.text,
            "coordinates": self.coordinates,
            "delay": self.delay,
            "iter_count": self.iter_count
        }




BLOCK_LIST = []
while True:
    create_prompt = input("New Block?: ")
    if create_prompt == "q":
        break

    # Create New Block
    new_block = None
    b_type = input("What kind of block [ click | text | wait ]: ")

    match b_type:
        case "c" | "click":
            new_block = Click()

        case 't' | 'text':
            new_block = Text()

        case 'w' | 'wait':
            new_block = WaitClick()
    
    new_block.get_input()

    BLOCK_LIST.append(new_block)


EXPORT_LIST = []
for block in BLOCK_LIST:
    block.play()
    EXPORT_LIST.append(block.export())

save_json(EXPORT_LIST, "sample.json")
print("- Done -")



