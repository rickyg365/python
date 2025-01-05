import os

from typing import Callable, Dict, List

def clear_screen():
    os.system('cls')



class Screen:
    DEFAULT_FILL = ' '
    def __init__(self, width: int=6, height: int=4, default_data=None):
        self.default = self.DEFAULT_FILL if default_data is None else default_data

        self.width = width
        self.height = height
        self.data = self.build_data()

    def __str__(self):
        s = self.build_text()
        return s
    
    def build_text(self):
        txt = ''
        for i in range(self.height):
            row = ''
            for j in range(self.width):
                curr = self.data[i][j]
                row += f"{curr}"
            txt += f"{row}\n"
        return txt
                
    def build_data(self, custom_data=None):
        data = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                current_data = self.default if custom_data is None else custom_data
                row.append(current_data)
            data.append(row)
        
        return data
    
    def update_pixel(self, x, y, new_pixel: str):
        # TBI pixel cache
        self.data[y][x] = new_pixel
    
    def export(self):
        return {
            'default': self.default,
            'width': self.width,
            'height': self.height,
            'data': self.data
        }
    

# class CollisionScreen(Screen):
#     DEFAULT_COLLISION_MAP = {
#         '0': 0,
#         '1': 1,
#         '2': 2
#     }
#     def __init__(self, width = 6, height = 4, default_data = None, default_collision_data = None):
#         # super().__init__(width, height, default_data)
#         # Not using super because we redefined build_data, to create both maps at the same time
#         self.default = self.DEFAULT_FILL if default_data is None else default_data
        
#         self.width = width
#         self.height = height
#         self.data, self.collision_layer = self.build_data()


#     def build_data(self, default_data='', collision_map=None):
#         data = []
#         collision_data = []
#         for i in range(self.height):
#             row = []
#             collision_row = []
#             for j in range(self.width):
#                 # Handle Map Data
#                 current_data = default_data
#                 row.append(current_data)

#                 # Handle Collision Data
#                 current_collision = 0
#                 if collision_map is not None:
#                     current_collision = collision_map.get(data, 0)
#                 collision_row.append(current_collision)
#             data.append(row)
#             collision_data.append(collision_row)
        
#         return data, collision_data

#     def create_collision_layer_from_data_map(self, map_data, collision_map: Dict):
#         collision_data = []
#         for row in map_data:
#             row = []
#             for item in row:
#                 current_data = collision_map.get(item, 0)
#                 row.append(current_data)
#             collision_data.append(row)
#         return collision_data



if __name__ == "__main__":
    WIDTH = 8 
    HEIGHT = 6
    
    s = Screen(WIDTH, HEIGHT, default_data=' ')
    # cs = CollisionScreen(WIDTH, HEIGHT, default_data='*')

    while True:
        print(s)
        input('>>> ')
        
        # print(cs)
        # input('>>> ')

