import os
import json

"""
Example:

"Print to console": {
    "prefix": "log",
    "body": [
        "console.log('$1');",
        "$2"
    ],
    "description": "Log output to console"
},
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


title
key
description

list of lines

"""


def get_snippet(filepath: str):
    # Firtst 3 lines 
    '''
    title
    key
    description
    '''
    with open(filepath, 'r') as innie:
        title = innie.readline()[1:].strip().split()[1]
        key = innie.readline()[1:].strip().split()[1]
        description = innie.readline()[1:].strip().split()[1]
        body = []

        for line in innie:
            body.append(line.replace("\n", ""))
        
    return {
        "title": title,
        "prefix": key,
        "body": body,
        "description": description
    }


def save(data, path="output.json"):
    with open(path, 'w') as outtie:
        json.dump(data, outtie, indent=4)
    return

def main():
    snippet = get_snippet("snippets/python/test.py") 
    print(snippet)
    save(snippet)
    

if __name__ == '__main__':
    main()
