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
        

def create_automation():
    # Ordered list
    new_map = []
    
    automation_name = input("Automation name: ")
    PROJECT_PATH = f"images/{automation_name}"

    os.makedirs(PROJECT_PATH, exist_ok=True)

    while True:
        d = {}
        t = input("Type(text/click): ")
        
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
    
    while True:
        try_it = input("Try out automation?: ")
        if try_it == 'n':
            break
        play_automation(new_map)
        
    save_it = input("Save automation?: ")
    if save_it == 'y':
        save_json(new_map, f"{PROJECT_PATH}/auto_map.json")

    return new_map


if __name__ == "__main__":
    # Create Automation
    AUTOMATION = create_automation()

    # Load Automation
    # ppath = input("Project Path: ")
    # ppath = "images/start_up/auto_map.json"
    # AUTOMATION = load_json(ppath)
    play_automation(AUTOMATION)







