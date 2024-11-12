
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

if __name__ == "__main__":
    pass
