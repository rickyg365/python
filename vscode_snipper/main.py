import os
import json


"""
"Print to console": {
    "prefix": "log",
    "body": [
        "console.log('$1');",
        "$2"
    ],
    "description": "Log output to console"
}
"""
def make_snippet(snippet_name: str, prefix: str, body: str, description: str):
    return




if __name__ == "__main__":
    FILENAME = "generated_snippets.json"
    SAMPLE_DATA = {
        "snippet_name": "Print to console",
        "prefix": "log",
        "body": [
            "console.log('$1');",
            "$2"
        ],
        "description": "Log output to console"
    }

