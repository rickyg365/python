from utils.screen_characters import SCREEN_CHARACTERS


class Screen:
    def __init__(self, width: int=20, height: int=10, border: bool=False):
        self.height = height
        self.width = width

        self.data = self.create_data(SCREEN_CHARACTERS.EMPTY.value)
        self.display_data = None
        
        # Track data changes to know if refresh is needed
        self.data_changed = True
        self.border = border


    def __str__(self) -> str:
        if not self.data_changed:
            return self.display_data
        
        display = ""
        if not self.border:
            # 1: No Border
            # for r in self.data:
            #     for c in r:
            #         display += c
            #     display += "\n"
            
            # 2: No Border
            display = "\n".join(["".join(row) for row in self.data])

        # 1: Border
        else:
            display = f"{SCREEN_CHARACTERS.C_TOP_LEFT.value}{(self.width) * SCREEN_CHARACTERS.HORIZONTAL.value}{SCREEN_CHARACTERS.C_TOP_RIGHT.value}\n"
            for r in self.data:
                display += f"{SCREEN_CHARACTERS.VERTICAL.value}"
                for c in r:
                    display += c
                display += f"{SCREEN_CHARACTERS.VERTICAL.value}\n"
            display += f"{SCREEN_CHARACTERS.C_BOT_LEFT.value}{(self.width) * SCREEN_CHARACTERS.HORIZONTAL.value}{SCREEN_CHARACTERS.C_BOT_RIGHT.value}"

        self.display_data = display

        return display

    def create_data(self, fill_char: str=SCREEN_CHARACTERS.EMPTY):
        # #1
        # new_data = []
        # for rows in range(self.height):
        #     new_row = []
        #     for char in range(self.width):
        #         new_row.append(fill_char)
        #     new_data.append(new_row)

        # return new_data 

        # 2
        return [[fill_char for char in range(self.width)] for row in range(self.height)]

    def update_cell(self, row: int, col: int, updated_char: str=SCREEN_CHARACTERS.FILL):
        self.data[row][col] = updated_char
        self.data_changed = True
        return
    
    def get_cell_value(self, row: int, col: int):
        return self.data[row][col]



