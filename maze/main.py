import os
from tracemalloc import start
from typing import List


class Grid:
    def __init__(self, width: int, height: int, default_value: any=0):
        self.h = height
        self.w = width

        self.default_value = default_value

        # [[self.default_value for w in range(width)] for h in range(height)]
        self.data = self.generate_grid()

    def __str__(self) -> str:
        txt = ""
        for h, row in enumerate(self.data):
            for w, col_value in enumerate(row):
                # print(w, h)
                txt += f"{col_value}"
            txt += "\n"
        return txt

    def generate_grid(self, value=None):
        if value is None:
            value = self.default_value
        
        return [[value for w in range(self.w)] for h in range(self.h)]
    
    def edit_cell(self, row: int, col: int, new_value: any):
        # Check Row
        if 0 > row >= self.h:
            print(f"row out of range, {row} {self.h}")
            return False
        # Check Col
        if 0 > col <= self.w:
            print(f"col out of range, {col} {self.w}")
            return False
        
        self.data[row][col] = new_value
        return True


# # Blind Search - Don't Know where the endpoint is
# def find_path(grid: Grid):
#     maze = grid.data
#     start_r, start_c = [0, 0]

#     upper_bound_r = len(maze)
#     upper_bound_c = len(maze[0])

#     print(f"Upper Bounds - Column: {upper_bound_c}, Row: {upper_bound_r}")

#     def find_neighbors(row, col):
#         neighbors = []

#         # Down, Left, Top, Right
#         dirs = [
#             [-1, 0],
#             [0, -1],
#             [1, 0],
#             [0, 1],
#         ]

#         # [neighbors.append([row + dr, col + dc]) for dr, dc in dirs]

#         for dr, dc in dirs:
#             # Get New Coordinate
#             new_row = row + dr
#             new_col = col + dc

#             neighbors.append([new_row, new_col])

#         return neighbors
    
#     final_path = ""
#     length_final_path = 0

#     paths = [[start_c, start_r]]
#     seen = {
#         "0_0": maze[0][0]
#     }
#     step = 0

#     while paths:
#         # Get the last node in current list and remove
#         curr_node = paths.pop()

#         # print(paths)
#         print(curr_node)
        
#         gr, gc = curr_node

#         # Break Condition - Final Point Found
#         if maze[gr][gc] == 1:
#             grid.edit_cell(gr, gc, "x")
#             print(grid)
            
#             final_path += f"({gr}, {gc}) [{length_final_path}]"
#             print(seen)
#             return final_path
        
#         final_path += f"({gr}, {gc})-> "
#         length_final_path += 1

#         # Display Grid
#         grid.edit_cell(gr, gc, ".")
#         print(grid)
#         input()

#         new_neighbors = find_neighbors(gr, gc)
#         step += 1

#         # Parse Neighbors - Already Visited, Exceeds Bounds, ...
#         for neighbor in new_neighbors:
#             # Current Coordinate Data
#             new_row, new_col = neighbor
#             new_key = f"{new_row}_{new_col}"

#             # Already Seen
#             if new_key in seen.keys():
#                 continue

#             # Check Row Coordinate Bounds
#             r_over_ubound = new_row >= upper_bound_r
#             r_under_lbound = new_row < 0
            
#             if r_under_lbound or r_over_ubound:
#                 # print(f"Row Coordinate exceeds Row Bounds, 0 < {new_row} < {upper_bound_r - 1}")
#                 continue

#             # Check Column Coordinate Bounds
#             c_over_ubound = new_col >= upper_bound_c
#             c_under_lbound = new_col < 0
            
#             if c_under_lbound or c_over_ubound:
#                 # print(f"Column Coordinate exceeds Row Bounds, 0 < {new_col} < {upper_bound_c - 1}")
#                 continue         

#             # Add to seen and path
#             dist_from_start = ((new_row - start_r)**2 + (new_col - start_c)**2)**0.5
#             seen[new_key] = step
#             # paths.append(neighbor)  # Depth
#             paths.insert(0, neighbor)  # Breadth
    
#     return final_path



# Blind Search - Don't Know where the endpoint is
def find_path(grid: Grid):
    maze = grid.data
    start_r, start_c = [0, 0]

    upper_bound_r = len(maze)
    upper_bound_c = len(maze[0])

    print(f"Upper Bounds - Column: {upper_bound_c}, Row: {upper_bound_r}")

    def find_neighbors(row, col):
        neighbors = []

        # Down, Left, Top, Right
        dirs = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1],
        ]

        # [neighbors.append([row + dr, col + dc]) for dr, dc in dirs]

        for dr, dc in dirs:
            # Get New Coordinate
            new_row = row + dr
            new_col = col + dc

            neighbors.append([new_row, new_col])

        return neighbors
    
    step = 0
    explored_path = ""

    paths = [[start_c, start_r]]
    seen = {
        "0_0": 0
    }

    while paths:
        # Get the last node in current list and remove
        curr_node = paths.pop()

        # print(paths)
        print(curr_node)
        
        gr, gc = curr_node

        # Break Condition - Final Point Found
        if maze[gr][gc] == 1:
            explored_path += f"({gr}, {gc}) [{seen[f'{gr}_{gc}']}]"

            grid.edit_cell(gr, gc, "x")
            print(grid)

            # print(seen)
            return explored_path
        
        explored_path += f"({gr}, {gc})-> "

        # Display Grid
        grid.edit_cell(gr, gc, ".")
        print(grid)
        # input()

        new_neighbors = find_neighbors(gr, gc)
        step += 1

        # Parse Neighbors - Already Visited, Exceeds Bounds, ...
        for neighbor in new_neighbors:
            # Current Coordinate Data
            new_row, new_col = neighbor
            new_key = f"{new_row}_{new_col}"

            # Already Seen
            if new_key in seen.keys():
                continue

            # Check Row Coordinate Bounds
            r_over_ubound = new_row >= upper_bound_r
            r_under_lbound = new_row < 0
            
            if r_under_lbound or r_over_ubound:
                # print(f"Row Coordinate exceeds Row Bounds, 0 < {new_row} < {upper_bound_r - 1}")
                continue

            # Check Column Coordinate Bounds
            c_over_ubound = new_col >= upper_bound_c
            c_under_lbound = new_col < 0
            
            if c_under_lbound or c_over_ubound:
                # print(f"Column Coordinate exceeds Row Bounds, 0 < {new_col} < {upper_bound_c - 1}")
                continue         

            # # Add to seen and path
            # dist_from_start = ((new_row - start_r)**2 + (new_col - start_c)**2)**0.5
            seen[new_key] = step
            # paths.append(neighbor)  # Depth
            paths.insert(0, neighbor)  # Breadth
    
    return explored_path


'''
Notes:
perfers right path
then down
then left
then down
then right


no weights, so path depends on direction order or order in whch we add neighbors to the path
'''

def main():
    blank_value = "*"
    new_grid = Grid(5, 5, "#")
    new_grid.edit_cell(3, 3, 1)
    print(new_grid)

    path = find_path(new_grid)
    
    print(path)
    return

if __name__ == '__main__':
    main()
