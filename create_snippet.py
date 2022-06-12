import os
import json

"""  
Turn into TUI
"""


def split_file_by_line(filepath: str):
    output = []
    with open(filepath, 'r') as in_file:
        for line in in_file:
            output.append(line)
    return output

def save_snippet(snippet_data, filepath: str):
    with open(filepath, 'a') as out_json:
        json.dump(snippet_data, out_json, indent=4)
    return True

def create_snippet(title: str, prefix: str, description: str, input_path: str, output_path: str="snippets.json"):
    """ 
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
    KEY: Title
    PREFIX: Command to type to envoke
    BODY: what gets expanded out
    DESCRIPTION: description for tooltip
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
    title = "Start a python file"
    prefix = "python_start"
    in_path = "s.py"
    description = "Start off a python file"
    out_path = "python_snippets.py"

    create_snippet(title, prefix, description, in_path, out_path)


if __name__ == '__main__':
    main()
