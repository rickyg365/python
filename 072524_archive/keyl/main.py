import os
import keyboard

from keyboard import KeyboardEvent

"""
Libraries
- keyboard: https://github.com/boppreh/keyboard#api
"""

def test_event(event: KeyboardEvent):
    print(f"""
Event: {event}
Name: {event.name}
Type: {event.event_type}
{event.name} Key was pressed {event.event_type}
""")


def key_pressed(event: KeyboardEvent):
    print(f"{event.name} Key was pressed!")

def update_log(event: KeyboardEvent, current_log: str):
    custom_keys = {
        "enter": "\n",
        "space": " ",
        "backspace": "[bksp]",
        "tab": "\t",
        "shift": "[shift]",
        "right shift": "[shift]",
        "alt": "[alt]",
        "right alt": "[alt]",
        "ctrl": "[ctrl]",
        "right ctrl": "[ctrl]",
    }
    update_status = False
    if event.event_type == "down":
        update_status = True
        # Backspace Case
        if event.name == "backspace":
            return current_log[:-1], update_status

        current_log += f"{custom_keys.get(event.name, event.name)}"
    return current_log, update_status


def main():
    key_log = ""
    
    while True:
        event = keyboard.read_event()
        key_log, update_status = update_log(event, key_log)

        if event.name == "esc":
            break

        if update_status:
            os.system("cls")
            print(f"{key_log}", flush=True)
            print("Press [esc] to quit!", flush=True)
    
    
if __name__ == "__main__":
    main()

