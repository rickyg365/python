import os
import glob

from pathlib import Path

def find_nodes(current_dir):
    node_files = []
    node_dirs = []

    current_nodes = glob.glob1(current_dir, '*')
    
    for node in current_nodes:
        if os.path.isfile(node):
            node_files.append(node)

        if os.path.isdir(node):
            node_dirs.append(node)

    print(node_files)
    print(node_dirs)

    return node_files, node_dirs


def explore_dir(raw_dir='.'):
    """  """
    storage = {}

    # Inputs
    if raw_dir == '.':
        raw_dir = os.getcwd()
    
    # Get root
    root = list(Path(raw_dir).parts)[-1]
    print(f"Root: {root}")

    # Get all first round of nodes/children
    main_files, main_dirs = find_nodes(raw_dir)

    main_queue = [*main_dirs]
    current_parents = [root]

    while main_queue:
        exploring = main_queue.pop()
        current_parents.append(exploring)
        print(exploring)

        new_path = os.path.join(root, exploring)

        new_files, new_dirs = find_nodes(new_path)

        new_storage_section = None

        
        for dir in new_dirs:
            main_queue.append(dir)
        
        for file in new_files:
            ...


        
        current_parents.remove(exploring)

            

    return 



if __name__ == "__main__":
    find_nodes(os.getcwd())
    explore_dir()
