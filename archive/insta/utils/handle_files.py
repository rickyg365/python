import os
import sys
import shutil


def get_args(default_value: str="thv"):
    args = sys.argv

    # if length != 2: Return Default
    if len(args) == 2:
        return sys.argv[1]
    
    # Default
    return default_value


# Handle Files
def group_by_subname(target: str, dir_path: str):
    # Create new final dir (if not already exists)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    # Get all file names, from main source
    for item in os.listdir():
        # Split each name w/ "_"
        t  = item.split("_")[0]
        
        if t != target:
            continue

        # if split[0] == target: add to new dir
        # Move file
        try:
            shutil.move(item, dir_path)
        except shutil.Error as shutil_error:
            # print(shutil_error)
            rewrite = input(f"Rewrite {item}?: ")
            if rewrite != "y":
                continue
            
            new_name = input(">>> ")
            shutil.move(item, f"{dir_path}/{new_name}")
            
        print(f"Move: {item} -> {dir_path}/")

    return






def main():
    return

if __name__ == '__main__':
    main()
