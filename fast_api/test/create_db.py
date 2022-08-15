import os
import json

sample_data = {
        "id": 1,
        "name": "Fake Name",
        "post_id": 5,
        "path": "fake/path/"
        }

with open("data/test/fake_data.json". 'w') as save_data:
    json.dump(sample_data, save_data, indent=4)


def main():
    pass

if __name__ == '__main__':
    main()

