import os

"""
BL
|
'---'  
TL
.---.
|   
BR
    |
'---'
TR
.---.
    |   
 


.---.
|   |
'---'
DATA = 3 char
has_up
has_down
has_left
has_right








.---.
|   |
'---'
.---.
|   |
'---'


.---+---+---+---.
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
'---+---+---+---'

.---+---+---+---.
| * | * | * | * |
+---+---+---+---+
| * | * | * | * |
+---+---+---+---+
| * | * | * | * |
+---+---+---+---+
| * | * | * | * |
'---+---+---+---'

.---=---=---=---.
| *   *   *   * |
+               +
| *   *   *   * |
+               +
| *   *   *   * |
+               +
| *   *   *   * |
'---+---+---+---'


.---+---+---+---.
| @ |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
'---+---+---+---'


.---+---+---+---.
|               |
+   +---+---+   +
|   |       |   |
+   +       +   +
|   |       |   |
+   +---+---+   +
|               |
'---+---+---+---'




.---+---+---+---.
| S |           |
+   +---+---+   +
|       |       |
+---+   +   +   +
|   |       |   |
+   +   +---+   +
|       |       |
'---+---+ E +---'

"""

class Cell:
    def __init__(self, data: str=None, width: int=3, height: int=1):
        self.width = width
        self.height = height

        self.data = data

        self.has_up = False
        self.has_down = False
        self.has_right = False
        self.has_left = False
        
        if data is not None:
            rows = data.split('\n')
            self.width = len(rows[0])
            self.height = len(rows)
            # if isinstance(data[0], list):
            #     self.height = len(data)
            #     self.width = len(data[0])
        
    def __str__(self):
        s = self.build_cell()
        return s
    
    def build_top(self):
        return f".{'-'*self.width}."
    
    def build_data(self):
        return f"|{self.data}|"
    
    def build_bottom(self):
        return f"'{'-'*self.width}'" 
    
    def build_cell(self):
        top = self.build_top()

        data = self.build_data()
        bottom = self.build_bottom()

        return f"""{top}
{data}
{bottom}"""





# class Screen:
#     EMPTY_CHAR = '|'
#     def __init__(self, width: int=40, height: int= 30):
#         self.height = height
#         self.width = width

#         self.data = self.build_data(entry_data=self.EMPTY_CHAR)

#     def __str__(self):
#         s = self.generate_str()
#         return s
    
#     def build_data(self, entry_data: str=None):
#         return [[entry_data for entry in range(self.width)] for row in range(self.height)]
    
#     def generate_str(self):
#         # python converts list into str for us!
#         return '\n'.join([''.join(r) for r in self.data])



if __name__ == "__main__":
    WIDTH, HEIGHT = os.get_terminal_size()

    new_cell = Cell()
    print(new_cell)






