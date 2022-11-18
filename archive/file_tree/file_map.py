import os

from pathlib import Path
from typing import List, Dict

from rich import print
from rich.tree import Tree

# Need to use depth for search

"""
Create File Map
"""
"""
# CWD
os.getcwd()

# Make Dir
os.mkdir("test")

# Create multiple deeper Dir
os.makedirs("test/new_test/newer_test")

# Check Path
os.path.exists("test/new_test/newer_test")

# Check Dir
os.path.isdir("test")
os.rmdir("test/new_test/newer_test")

# Check File then remove
os.path.isfile("web_scrap/requirements.txt")
os.remove("web_scrap/requirements.txt")

# Get all txt files
txt_files = list(glob("*.txt"))

# Get absolute path
my_absolute_dirpath = os.path.abspath(os.path.dirname(__file__))

"""

def relative_to_absolute(directory: str) -> str:
    raw_directory_list = directory.split("\\")

    # Parse Periods
    current_path = Path(directory)
    go_back = 0

    if raw_directory_list[0] == ".." or raw_directory_list[0] == ".":
        go_back = raw_directory_list.count("..")

        current_path = Path(os.getcwd())
    
    else:
        return directory
    
    new_directory = "/".join([f"{x}" for x in current_path.parts[:(go_back * -1)]])
    
    if new_directory == ".":
        new_directory = current_path

    return new_directory
    


def get_all(raw_directory=None ,debug=False):
    # In case we get a relative directory
    directory = relative_to_absolute(raw_directory)
    
    # Can directly edit dirs if using topdown in os.walk
    tree_map = {}

    excluded = (".git")
    visited_dirs = []

    # maybe add os.path.exists
    if directory is None or not os.path.exists(directory):
        print("Going with cwd")
        directory = os.getcwd()

    for root, dirs, files in os.walk(directory, topdown=True):
        # print(directory)
        directory_level = root.replace(directory, "")
        directory_level = directory_level.count(os.sep)
        # print(directory_level)
        # Edit dirs to be excluded
        dirs[:] = [d for d in dirs if d not in excluded]
        
        root_name = Path(root).name

        # Add variables into a data structure
        tree_map[root_name] = []

        for file in files:
            tree_map[root_name].append(file)
        
        for dir in dirs:
            if dir not in visited_dirs:
                visited_dirs.append(dir)
                # print(visited_dirs)
                tree_map[root_name].append(f"{dir}")
            else:
                pass
        # for dir in dirs:  
        #     tree_map[root_name] = dir
        
        # Debug
        if debug:
            print(f"Root: {root_name}")
            print(f"Dir: {dirs}")
            print(f"Files: {files}\n")
        
        
    
    return tree_map


def create_file_map(file_map: Dict[str, str], debug:bool=False):
    
    root = list(file_map.keys())[0]
    output_tree = Tree(f"[red]{root.title()}/ [yellow](Root Directory)")

    new_base = output_tree
    
    # Can directly edit dirs if using topdown in os.walk
    for dir, files in file_map.items():
        if dir != root:
            new_base = output_tree.add(f"[red]{dir}/")

        for file in files:
            new_base.add(f"[green]{file}")
        
    # print(file_map)
        
    return output_tree
        

if __name__ == "__main__":
    current_directory = "C:\\Users\\ricky\\Documents\\GitHub\\send"
    raw_file_data = get_all(current_directory)
    file_tree = create_file_map(raw_file_data)
    print()
    print(f"CWD: {os.getcwd()}")
    print(file_tree)
    print()

    print(relative_to_absolute("C:\\Users\\ricky\\Documents\\GitHub"))  # "..\\..\\."
