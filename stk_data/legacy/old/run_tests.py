import os

from utils.stock_object import Stock

from get_data import get_data
from handle_json import save_json, load_json

"""

"""

def test_get_data():
    new_data = get_data("TSLA", "5d")

    assert type(new_data) is list


def test_save_json(input_data):
    # if test file exist remove it
    if os.path.isfile("data/test/active_test.json"):
        os.remove("data/test/active_test.json")
    
    # try creating a new json
    json_list = []
    for data in input_data:
        json_list.append(data.export())
    save_json("data/test/active_test.json", json_list)

    assert os.path.isfile("data/test/active_test.json")


def test_load_json():
    try:
        load_data = load_json("data/test/loading_test.json")
    except FileNotFoundError:
        raise AssertionError
    assert type(load_data) is list




def main():
    test_data = get_data("TSLA", "5d")
    
    tests = [
        (test_get_data, None),
        (test_save_json, test_data),
        (test_load_json, None)
    ]

    total_test = len(tests)
    failed = 0

    for (test_func, test_param) in tests:
        try:
            if test_param is None:
                test_func()
                continue
            test_func(test_param)
        
        except AssertionError:
            failed += 1

    ratio = ((total_test-failed)/total_test) * 40
    passed_txt = int(ratio) 

    print(f"[{passed_txt * '*':<40}]")
    


if __name__ == "__main__":
    main()
