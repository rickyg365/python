import os
import json

"""  
Turn into TUI
"""

def save_snippet(snippet_data, filepath: str):
    with open(filepath, 'a') as out_json:
        json.dump(snippet_data, out_json, indent=4)
    return True

def split_file_by_line(filepath: str):
    output = []
    with open(filepath, 'r') as in_file:
        for line in in_file:
            output.append(line)
    return output

def create_snippet(input_path: str, output_path: str="snippets.json", title: str="New Snippet", prefix: str=None, description: str=None):
    """ 
    KEY: Title
    PREFIX: Command to type to envoke
    BODY: what gets expanded out
    DESCRIPTION: description for tooltip
    
    "Start Python File": {
        "prefix": "pystart",
        "body": [
            "import os",
            "",
            "def main():",
            "\treturn",
            "",
            "if __name__ == '__main__':",
            "\tmain()",
            ""
        ],
        "description": "Create Base Python File"
    }
   
    """
    new_data = split_file_by_line(input_path)
    
    new_snippet = {
        title: {
            "prefix": prefix,
            "body": new_data,
            "description": description
        }
    }

    save_snippet(new_snippet, output_path)


def main():
    filepath = "sample_file.py"
    base_name, ext = filepath.split('.')
    output_path = f"snippets/{base_name}.json"
    
    title = "Start a python file"
    prefix = "python_start"
    description = "Start off a python file"

    create_snippet(filepath, output_path, title, prefix, description)


if __name__ == '__main__':
    main()
