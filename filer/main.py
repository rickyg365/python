import os



class FileHandler:
    def __init__(self, basepath: str = "data"):
        self.path = basepath
        
        # On Startup
        self.startup()

    def __str__(self) -> str:
        txt = ""
        return txt

    def startup(self):
        # If dir exists
        # Scan Directory
        # Generate dir map
        # 
        return
    
    def generate_map(self):
        return
    


class DirTree:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self) -> str:
        txt = ""
        return txt
    
    def follow_path_by_id(self):
        """
        Given a list of ids in order traverse the tree in given order if it is possible else return error/false
        """
        return


def generate_dir_obj(filepath):
    """
    data: 
        backups
            backup1.txt
            backup2.txt
            backup3.txt
            backup4.txt

        subdata
            test.txt
        
        files:    
            file1.txt
            file2.txt
            file3.txt
            file4.txt
    """

    output_data = {
            "files": []
        }

    for item in os.scandir(filepath):
        path = item.path
        name = item.name

        if item.is_dir():
            # Folder
            output_data[name] = generate_dir_obj(path)
        else:
            # File
            output_data["files"].append(name)

    return output_data


def main():
#     bpath = "data"
#     dir_scan = os.scandir(bpath)
#     print(dir_scan)

#     for obj in dir_scan:
#         current_path = obj.path
#         current_name = obj.name
        
#         if obj.is_dir():
#             # Recurse
#             for new_sub_obj in os.scandir(current_path):



#         file_or_dir = "file" if obj.is_file() else "fold"
#         nice_obj = f"""
# [{file_or_dir}] ~ {obj.path}
# Name: {obj.name} 
# """     
#         print(nice_obj)
    return

def dstr(dict_obj, layer=0):
    new_text = ""
    title_spacing = layer * '   '
    for k, v in dict_obj.items():
        spacing = (layer)*'   '
        
        if k == "files":
            for item in v:
                new_text += f"{spacing} - {item}\n"
            continue

        new_text += f"{title_spacing}({k})\n"
        if type(v) is dict:
            new_text += dstr(v, layer + 1)
            continue
        if type(v) is list:
            for item in v:
                new_text += f"{spacing} - {item}\n"
            continue
        else:
            new_text += f"{spacing}{v}"
    return new_text


if __name__ == '__main__':
    # main()
    all_data = generate_dir_obj("data")
    print("[ Data Directory ]")

    print(dstr(all_data))
    # print(*all_data["backups"]['files'], sep=", ")
