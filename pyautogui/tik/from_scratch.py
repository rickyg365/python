import pyautogui

from utils.auto_library import AutomationStep, AutomationList

'''
class GeneralAutomation(CreationTemplate):
    def __init__(self, filename: str=None):
        self.filename = None
        self.data = None
        self.has_data = False
        
        self.load_data(filename)
    
    def __str__(self):
        self.has_data = '#' if self.has_data else ' '
        txt = f"Current File [ ]: {self.filename}"
        return txt

    def load_data(self, filename: str):
        if filename is None:
            return
        
        self.filename = filename
        raw_data = load_json(filename)

        # Update Object
        self.has_data = True
        self.data = self.prepare_data(raw_data)

    def prepare_data(self, raw_data):
        if raw_data is None:
            self.has_data = False
            return None

        output_data = []
        for item in raw_data:
            data = item.get('data', None)
            data_type = item.get('datatype', None)

            new_step = AutomationStep(data_type).import_raw_data(data)
       
            output_data.append(new_step)
        return output_data
    
    def dump_data(self):
        if not self.has_data:
            return

        export_data = [i.export() for i in self.data]

        save_json(export_data, self.filename)

    def run(self):
        if not self.has_data:
            return

        for item in self.data:
            item.play()

    def create(self, filename: str=None):
        """  """
        if filename is None:
            filename = input("Choose filename for map: ")

        new_map = []

        while True:
            new_step = None
            new_step_type = input("What type of action [ Button | Popup | >Text< ]: ")

            match new_step_type:
                case 'b' | 'button':
                    new_step = self.create_button()
                    new_step_type = 'button'
                case 'p' | 'popup':
                    new_step = self.create_popup()
                    new_step_type = 'popup'
                case 'q' | 'quit':
                    break
                case _:
                    pass
            new_map.append(AutomationStep(new_step_type, new_step))
        
        self.filename = filename
        self.data = new_map
        self.has_data = True
'''


if __name__ == '__main__':
    FILENAME = "data/maps/test_map.json"
    
    map = AutomationList()
    map.load_data(FILENAME)

    while True:
        print(f"Current filename: {FILENAME}")
        user_input = input(f"""
[r]un       current automation 
[c]reate    new Automation 
[l]oad      new Automation 
[q]uit     

>>>""")

        match user_input:
            case 'c' | 'create':
                # Create new Automation 
                map.create(FILENAME)
                # Save
                sav = user_input("Save?: ")
                if sav == 'y':
                    map.save_data()

            case 'l' | 'load':
                FILENAME = input("New Filename?: ")
                map.load_data(FILENAME)
            
            case 'r' | 'run':
                map.run()

            case 'q':
                break

            case _:
                pass

