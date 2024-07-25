import json
import time

import pyautogui

"""
Add editing keys from a loaded file

Quick Notes
------------------------------------------------------------
[ General ]
# Current mouse position
pyautogui.position()  # (120, 20)

# Screen Resolution
pyautogui.size()  # (1920, 1080)

# Check if x, y is in within screen
pyautogui.onScreen(x, y)  # True|False

# Pause
pyautogui.PAUSE = 2.5

# Fail-safe mode, raise mouse to upper-left
pyautogui.FAILSAFE = True

[Mouse Movement]
pyautogui.moveTo(x, y, duration=num_seconds)  # move mouse to XY over num_second
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position

pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  # drag mouse relative to its current position

[CLICK]
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
# Valid buttons: 'left', 'middle', 'right'

[SCROLL]
pyautogui.scroll(amount_to_scroll, x=moveToX, y=moveToY)

[Individual Button PRESS]
pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')

[Keyboard]
pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)  # useful for entering text, newline is Enter
# valid keys pyautogui.KEYBOARD_KEYS

[HOTKEYS]
pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste

[Individual Button PRESS]
pyautogui.keyDown(key_name)
pyautogui.keyUp(key_name)

[Message Box]
pyautogui.alert('This displays some text with an OK button.')
pyautogui.confirm('This displays text and has an OK and Cancel button.')  # 'OK'
pyautogui.prompt('This lets the user type in a string and press OK.')  # 'This is what I typed in.'

[Locate on Screen]
pyautogui.locateOnScreen('looksLikeThis.png')  # returns (left, top, width, height) of first place it is found, (863, 417, 70, 13)
pyautogui.locateCenterOnScreen('looksLikeThis.png')  # returns center x and y, (898, 423)
"""

def save_json(data, filename: str="data.json"):
    # Returns True or Error
    with open(filename, 'w') as save_buf:
        json.dump(data, save_buf, indent=4)
    return True

def load_json(filename: str):
    data = None

    with open(filename, 'r') as load_buf:
        data = json.load(load_buf)

    return data

if __name__ == "__main__":
    DEFAULT_FILENAME = "default_name_keyfile.json"
    valid_actions = ['file', 'new']
    
    metadata = {
        'num_keys': 0
    }

    while True:
        user_prompt = f"""
Filename: {DEFAULT_FILENAME}
# of Keys: {metadata['num_keys']}

[ Valid Actions ]
file -> Change filename
new -> Input new keys
quit -> Exit
"""
        # First Prompt, display metadata(num_keys)
        action = pyautogui.prompt(user_prompt)

        match action:
        # Change Filename
            case 'file':
                DEFAULT_FILENAME = pyautogui.prompt('New Filename: ')
            
        # Input new key/s
            case 'new':
                # Key Input
                keys = {}
                new_num = 0

                again = True
                while again:
                    # Add name
                    key_name = pyautogui.prompt("Key Name: ")

                    # hold cursor still for 4 sec to save coordinates
                    a, b = pyautogui.position()
                    time.sleep(2.5)
                    c, d = pyautogui.position()
                    
                    x_error = abs(a - c) < 5
                    y_error = abs(b - d) < 5

                    if x_error and y_error:
                        keys[key_name] = a, b
                        new_num += 1
                    else:
                        pyautogui.alert(f"Failed to add {key_name}...")
                        continue

                    again = True if pyautogui.confirm("Add another key?") == 'OK' else False

            case 'quit':
                break

    # Save
    save_or_nah = True if pyautogui.confirm("Save?") == 'OK' else False
    
    if save_or_nah:
        save_json(keys, DEFAULT_FILENAME)
