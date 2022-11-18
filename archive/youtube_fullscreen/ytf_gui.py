import PySimpleGUI as sg
import pandas.io.clipboard as pyperclip

from youtube_link_converter import get_fullscreen_url

"""
Program: Youtube fullscreen url converter
"""

sg.theme('BlueMono')   # Add a touch of color

# All the stuff inside your window.
# [sg.Text("", key="output-text", justification="center")],
layout = [  [sg.Text('Enter Youtube URL'), sg.InputText(key="start_url", do_not_clear=False)],
            [sg.Button('Get Fullscreen'), sg.Button('Cancel')] ]


config = {
    "element_justification": "center",
    "finalize": True
}

if __name__ == '__main__':
    # Create the Window
    window = sg.Window('Youtube URL Converter', layout, **config)

    # Event Loop to process "events" and get the "values" of the inputs
    event, values = window.read()

    if event not in (sg.WIN_CLOSED, 'Cancel'):
        # Parse Data
        start_url = values["start_url"]
        final_url = get_fullscreen_url(start_url)

        # Copy to Clipboard
        pyperclip.copy(final_url)

        # Update Display
        # window['output-text'].update(final_url)

    window.close()