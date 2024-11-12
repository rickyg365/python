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
        find_n_click(self.image)
        pyautogui.sleep(self.delay)
    

    def export(self):
        return {
            "type": self.type,
            "coordinates": self.coordinates,
            "image": self.image,
            "delay": self.delay,
            "iter_count": self.iter_count
        }


class Text(AutomationBlock):
    def __init__(self, text: str, coordinates=None, delay: int=0):
        super().__init__(type="text", text=text, coordinates=coordinates, delay=delay)
    
    def __str__(self):
        s = f'{self.type}'
        return s
    
    def play(self):
        find_n_click(self.image)
        pyautogui.sleep(self.delay)
    

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
    

    def export(self):
        return {
            "type": self.type,
            "text": self.text,
            "coordinates": self.coordinates,
            "delay": self.delay,
            "iter_count": self.iter_count
        }



def play_automation(automation_map):
    for item in automation_map:
        t = item['type']

        match t:
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
            case _:
                pass
        

def create_automation(dir_path: str):
    # Ordered list
    new_map = []
    
    automation_name = input("Automation name: ")
    PROJECT_PATH = f"{dir_path}/{automation_name}"

    os.makedirs(PROJECT_PATH, exist_ok=True)

    while True:
        d = {}
        t = input("Type(text/click/wait): ")
        
        match t:
            case 't' | 'text':
                d['type'] = 'text'
                d["text"] = input("Text: ")
                d["coordinates"] = get_coordinates("Place mouse over textbox and press enter...")
                d["delay"] = int(input("Delay: "))

            case 'c' | 'click':
                d['type'] = 'click'
                d["image"] = get_image(PROJECT_PATH)
                d["delay"] = int(input("Delay: "))
                
            case 'w' | 'wait':
                d['type'] = 'wait'
                d["image"] = get_image(PROJECT_PATH)
                d["iter_count"] = int(input("Max iteration count: "))
                d["delay"] = int(input("Delay: "))
            case _:
                pass
        new_map.append(d)

        again = input("Again?: ")
        if again == 'n':
            break
        
    save_it = input("Save automation?: ")
    if save_it == 'y':
        save_json(new_map, f"{PROJECT_PATH}/auto_map.json")

    return new_map,  f"{PROJECT_PATH}/auto_map.json"

def edit_automations(auto_map):
    for item in auto_map:
        display = ""
        for k, v in item.items():
            display += f"\n{k}: {v}"
        # display += "\n"
        print(display)
    
        edit = input("Edit item?: ")

        if edit != "y":
            continue

        # Edit Entry
        while True:
            display = ""
            for k, v in item.items():
                display += f"\n{k}: {v}"
            # display += "\n"
            print(display)
            
            u_in = input("What entry to edit?: ")
            u_val = input("New value: ")

            if u_in == 'q':
                break

            convert_int = ["iter_count", "delay"]
            
            if u_in in convert_int:
                u_val = int(u_val)

            if u_in == "coordinates":
                u_val = u_val.split(" ")

            item[u_in] = u_val

        
    return auto_map


if __name__ == "__main__":
    DIR_PATH = "maps"
    # Create Automation
    # AUTOMATION, FILEPATH = create_automation(DIR_PATH)
    # edit_automations(AUTOMATION)
    
    # save_it = input("Save automation?: ")
    # if save_it == 'y':
    #     save_json(AUTOMATION, FILEPATH)

    # Load Automation
    # ppath = input("Project Path: ")
    ppath = "maps/sample/auto_map.json"
    AUTOMATION = load_json(ppath)
    # play_automation(AUTOMATION)    
    edit_automations(AUTOMATION)
    save_it = input("Save automation?: ")
    if save_it == 'y':
        save_json(AUTOMATION, ppath)
    
    while True:
        try_it = input("Try out automation?: ")
        if try_it == 'n':
            break
        play_automation(AUTOMATION)
    
