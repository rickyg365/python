import os

# Model
from models.drawable import Drawable

# File Handler
from utils.file_handle import save_json, load_json, save_txt, load_txt


if __name__ == "__main__":
    # Load Sample Data
    txt_data = load_txt("data/samples/example.txt")
    json_data = load_json("data/samples/example.json")
    
    # Create Drawable Object
    t_drawable = Drawable(txt_data)
    j_drawable = Drawable(json_data)

    # Test Save Data, can also make it a built in method
    save_txt(t_drawable.export(), "data/samples/example.txt")
    save_json(j_drawable.json(), "data/samples/example.json")

    results = f"""
Text Data (Loaded):
{txt_data}

Json Data (Loaded):
{json_data}

Drawable (from text data):
{t_drawable}

Drawable (from json data):
{j_drawable}
"""
    print(results)
